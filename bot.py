import requests
import json
import time
import sqlite3
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==================== معلومات البوت ====================
TOKEN = os.getenv("TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID", "0")
DEV_USERNAME = os.getenv("DEV_USERNAME", "devQasm")
DEV_CHANNEL = os.getenv("DEV_CHANNEL", "https://t.me/prgtop")
URL = f"https://api.telegram.org/bot{TOKEN}"

if not TOKEN:
    print("❌ خطأ: TOKEN غير موجود في ملف .env")
    exit(1)

# ==================== قاعدة البيانات ====================
if os.path.exists('python_bot.db'):
    os.remove('python_bot.db')

conn = sqlite3.connect('python_bot.db', check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    points INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    xp INTEGER DEFAULT 0,
    completed_lessons TEXT DEFAULT '',
    join_date TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    code_example TEXT,
    quiz_question TEXT,
    quiz_options TEXT,
    quiz_answer TEXT,
    xp_reward INTEGER DEFAULT 10
)''')

c.execute('''CREATE TABLE IF NOT EXISTS python_commands (
    command TEXT PRIMARY KEY,
    description TEXT,
    example TEXT
)''')

conn.commit()

# ==================== إضافة دروس بايثون ====================
lessons_data = [
    (1, "🐍 مقدمة في بايثون", 
     """<b>📚 ما هي لغة بايثون؟</b>

بايثون هي لغة برمجة عالية المستوى، سهلة التعلم، وتستخدم في:
• تطوير الويب
• تحليل البيانات
• الذكاء الاصطناعي
• أتمتة المهام

<b>✨ مميزات بايثون:</b>
• سهلة القراءة والكتابة
• مجانية ومفتوحة المصدر
• مكتبات ضخمة
• مجتمع كبير للمساعدة""",
     """<b>💻 أول برنامج في بايثون:</b>

<code>print("مرحباً بك في عالم البرمجة!")</code>

<b>🔍 شرح الكود:</b>
• print() - دالة للطباعة
• النص داخل "" - يتم طباعته""",
     "ما هي دالة الطباعة في بايثون؟",
     "print()|input()|len()|str()",
     "print()",
     15),
    
    (2, "📦 المتغيرات والبيانات", 
     """<b>📚 ما هي المتغيرات؟</b>

المتغيرات هي أماكن لتخزين البيانات في الذاكرة.

<b>📊 أنواع البيانات الأساسية:</b>
• int - الأعداد الصحيحة (10, 20, 100)
• float - الأعداد العشرية (3.14, 2.5)
• str - النصوص ("سلام", "Python")
• bool - القيم المنطقية (True, False)

<b>💡 أمثلة:</b>
<code>name = "قاسم"        # نص
age = 25              # عدد صحيح
price = 99.99         # عدد عشري
is_student = True     # منطقي</code>""",
     """<b>💻 أمثلة عملية:</b>

<code># تعريف المتغيرات
x = 10
y = 20
z = x + y

# طباعة النتيجة
print("ناتج الجمع:", z)

# تغيير قيمة المتغير
x = 50
print("القيمة الجديدة:", x)</code>""",
     "أي من التالي يعتبر نوع بيانات نصي في بايثون؟",
     "int|float|str|bool",
     "str",
     15),
    
    (3, "🔢 العمليات الحسابية", 
     """<b>📚 العمليات الحسابية في بايثون:</b>

<b>➕ عمليات الجمع والطرح:</b>
• + (جمع)
• - (طرح)
• * (ضرب)
• / (قسمة)

<b>🧮 أمثلة:</b>
<code>result1 = 10 + 5    # النتيجة: 15
result2 = 20 - 8    # النتيجة: 12
result3 = 7 * 6     # النتيجة: 42
result4 = 15 / 3    # النتيجة: 5.0</code>

<b>📌 عمليات متقدمة:</b>
• // (قسمة صحيحة)
• % (باقي القسمة)
• ** (الأس)</code>""",
     """<b>💻 برنامج حساب متوسط الدرجات:</b>

<code># درجات الطالب
grade1 = 85
grade2 = 90
grade3 = 78

# حساب المجموع والمتوسط
total = grade1 + grade2 + grade3
average = total / 3

# طباعة النتائج
print("المجموع:", total)
print("المتوسط:", average)</code>""",
     "ما هو ناتج العملية 15 // 4 في بايثون؟",
     "3.75|3|4|3.0",
     "3",
     15),
    
    (4, "🎯 الجمل الشرطية", 
     """<b>📚 الجمل الشرطية (if-else)</b>

الجمل الشرطية تتحكم في تنفيذ الكود بناءً على شروط معينة.

<b>🔹 تركيب if:</b>
<code>if condition:
    # الكود المنفذ عند تحقق الشرط</code>

<b>🔹 تركيب if-else:</b>
<code>if condition:
    # الكود عند تحقق الشرط
else:
    # الكود عند عدم تحقق الشرط</code>

<b>🔹 تركيب if-elif-else:</b>
<code>if condition1:
    # شرط 1
elif condition2:
    # شرط 2
else:
    # باقي الحالات</code>""",
     """<b>💻 مثال: نظام الدرجات</b>

<code># إدخال درجة الطالب
score = 85

# تحديد التقدير
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# طباعة النتيجة
print(f"تقديرك هو: {grade}")</code>""",
     "أي من التالي يمثل جملة شرطية صحيحة في بايثون؟",
     "if x > 5:|if x > 5 then:|if (x > 5):|if x > 5: then",
     "if x > 5:",
     20),
]

for lesson in lessons_data:
    c.execute("INSERT OR IGNORE INTO lessons (id, title, content, code_example, quiz_question, quiz_options, quiz_answer, xp_reward) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", lesson)
conn.commit()

# ==================== أوامر بايثون الشائعة ====================
python_commands = [
    ("print()", "طباعة النصوص والقيم", 'print("Hello World")'),
    ("input()", "أخذ إدخال من المستخدم", 'name = input("ادخل اسمك: ")'),
    ("len()", "معرفة طول النص أو القائمة", 'length = len("Python")'),
    ("type()", "معرفة نوع البيانات", 'data_type = type(10)'),
]

for cmd, desc, ex in python_commands:
    c.execute("INSERT OR IGNORE INTO python_commands (command, description, example) VALUES (?, ?, ?)", (cmd, desc, ex))
conn.commit()

# ==================== دوال مساعدة ====================
def send_message(chat_id, text, reply_markup=None, parse_mode="HTML"):
    payload = {"chat_id": chat_id, "text": text, "parse_mode": parse_mode}
    if reply_markup:
        payload["reply_markup"] = json.dumps(reply_markup)
    try:
        return requests.post(f"{URL}/sendMessage", json=payload, timeout=30).json()
    except Exception as e:
        print(f"❌ خطأ في إرسال الرسالة: {e}")
        return None

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_user(user_id):
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    if row:
        return {"user_id": row[0], "username": row[1], "first_name": row[2], 
                "points": row[3], "level": row[4], "xp": row[5], 
                "completed_lessons": row[6], "join_date": row[7]}
    else:
        c.execute("INSERT INTO users (user_id, username, first_name, join_date) VALUES (?, ?, ?, ?)",
                  (user_id, "", "", get_current_time()))
        conn.commit()
        return get_user(user_id)

def get_main_keyboard():
    return {
        "inline_keyboard": [
            [{"text": "📚 الدروس", "callback_data": "lessons"}],
            [{"text": "⚙️ الإعدادات", "callback_data": "settings"},
             {"text": "💾 حفظ", "callback_data": "save"}]
        ]
    }

def get_back_button():
    return {"inline_keyboard": [[{"text": "🔙 رجوع", "callback_data": "back_to_main"}]]}

# ==================== تشغيل البوت ====================
print("="*60)
print("🐍 بوت تعليم برمجة بايثون - يعمل الآن")
print(f"👨‍💻 المطور: @{DEV_USERNAME}")
print("="*60)

offset = None

while True:
    try:
        response = requests.get(f"{URL}/getUpdates", params={"timeout": 60, "offset": offset}).json()
        updates = response.get("result", [])
        
        for u in updates:
            offset = u["update_id"] + 1
            
            if "message" in u:
                msg = u["message"]
                chat_id = msg["chat"]["id"]
                user_id = msg["from"]["id"]
                text = msg.get("text", "")
                first_name = msg["from"].get("first_name", "مستخدم")
                username = msg["from"].get("username", "")
                
                if text == "/start":
                    user = get_user(user_id)
                    c.execute("UPDATE users SET username = ?, first_name = ? WHERE user_id = ?", (username, first_name, user_id))
                    conn.commit()
                    
                    welcome_text = f"""🐍 <b>مرحباً بك {first_name}!</b>

📚 <b>ماذا ستتعلم؟</b>
✓ أساسيات البرمجة
✓ المتغيرات والبيانات
✓ الجمل الشرطية والحلقات
✓ التوابع والقوائم
✓ التعامل مع الملفات
✓ معالجة الأخطاء

⭐ <b>المستوى:</b> {user['level']}
💰 <b>النقاط:</b> {user['points']}

استخدم الأزرار للبدء!"""
                    
                    send_message(chat_id, welcome_text, reply_markup=get_main_keyboard())
            
            elif "callback_query" in u:
                cq = u["callback_query"]
                user_id = cq["from"]["id"]
                data = cq["data"]
                message_id = cq["message"]["message_id"]
                chat_id = cq["message"]["chat"]["id"]
                
                if data == "back_to_main":
                    user = get_user(user_id)
                    welcome_text = f"""🐍 <b>القائمة الرئيسية</b>

⭐ <b>المستوى:</b> {user['level']}
💰 <b>النقاط:</b> {user['points']}

اختر ما تريد:"""
                    requests.post(f"{URL}/editMessageText", json={
                        "chat_id": chat_id,
                        "message_id": message_id,
                        "text": welcome_text,
                        "parse_mode": "HTML",
                        "reply_markup": json.dumps(get_main_keyboard())
                    }).json()
                
                elif data == "lessons":
                    lesson_text = """📚 <b>الدروس المتاحة:</b>

1️⃣ 🐍 مقدمة في بايثون
2️⃣ 📦 المتغيرات والبيانات
3️⃣ 🔢 العمليات الحسابية
4️⃣ 🎯 الجمل الشرطية

اختر درس لقراءته"""
                    requests.post(f"{URL}/editMessageText", json={
                        "chat_id": chat_id,
                        "message_id": message_id,
                        "text": lesson_text,
                        "parse_mode": "HTML",
                        "reply_markup": json.dumps(get_back_button())
                    }).json()
        
    except Exception as e:
        print(f"❌ خطأ: {e}")
        time.sleep(5)
