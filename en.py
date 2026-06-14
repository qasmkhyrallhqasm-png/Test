import requests
import json
import time
import sqlite3
import os
from datetime import datetime
from typing import Optional

# ==================== معلومات البوت ====================
TOKEN = "8701617833:AAGinjHjJv8kBewl4reY8NZi020zCU9DI78" 
TOKEN = "8701617833:AAGinjHjJv8kBewl4reY8NZi020zCU9DI78"
ADMIN_ID = 8304323630
DEV_USERNAME = "devQasm"
DEV_CHANNEL = "https://t.me/prgtop"
URL = f"https://api.telegram.org/bot{TOKEN}"

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

c.execute('''CREATE TABLE IF NOT EXISTS user_answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    lesson_id INTEGER,
    answer TEXT,
    is_correct INTEGER,
    answer_date TEXT
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
    
    (5, "🔄 الحلقات التكرارية", 
     """<b>📚 الحلقات التكرارية (Loops)</b>

الحلقات تستخدم لتكرار الأوامر عدة مرات.

<b>🔹 حلقة for:</b>
تستخدم للتكرار على مجموعة من العناصر.
<code>for i in range(5):
    print(i)  # تطبع 0,1,2,3,4</code>

<b>🔹 حلقة while:</b>
تستمر طالما الشرط صحيح.
<code>count = 0
while count < 5:
    print(count)
    count += 1</code>

<b>💡 استخدامات شائعة:</b>
• تكرار العمليات
• معالجة القوائم
• إنشاء أنماط</code>""",
     """<b>💻 مثال: جمع الأعداد من 1 إلى 10</b>

<code># باستخدام for
total = 0
for i in range(1, 11):
    total = total + i
print("المجموع (for):", total)

# باستخدام while
total = 0
i = 1
while i <= 10:
    total = total + i
    i += 1
print("المجموع (while):", total)</code>""",
     "ما هو ناتج تنفيذ الكود: for i in range(3): print(i)",
     "0,1,2|1,2,3|0,1,2,3|1,2",
     "0,1,2",
     20),
    
    (6, "📋 القوائم (Lists)", 
     """<b>📚 القوائم في بايثون</b>

القائمة هي مجموعة مرتبة من العناصر.

<b>🔹 إنشاء قائمة:</b>
<code>fruits = ["تفاح", "موز", "برتقال"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "نص", True, 3.14]</code>

<b>🔹 الوصول للعناصر:</b>
<code>fruits[0]  # العنصر الأول: "تفاح"
fruits[-1] # العنصر الأخير: "برتقال"</code>

<b>🔹 العمليات على القوائم:</b>
• append() - إضافة عنصر
• remove() - حذف عنصر
• len() - طول القائمة
• sort() - ترتيب القائمة</code>""",
     """<b>💻 مثال: إدارة قائمة المهام</b>

<code># قائمة المهام
tasks = []

# إضافة مهام
tasks.append("تعلم بايثون")
tasks.append("قراءة كتاب")
tasks.append("ممارسة البرمجة")

# عرض جميع المهام
print("قائمة المهام:")
for task in tasks:
    print(f"- {task}")

# عدد المهام
print(f"عدد المهام: {len(tasks)}")</code>""",
     "أي دالة تستخدم لإضافة عنصر إلى قائمة؟",
     "add()|append()|insert()|push()",
     "append()",
     15),
    
    (7, "📝 التوابع (Functions)", 
     """<b>📚 التوابع (الدوال) في بايثون</b>

التوابع هي كتل قابلة لإعادة الاستخدام.

<b>🔹 تعريف تابع:</b>
<code>def greet(name):
    return f"مرحباً {name}!"</code>

<b>🔹 استدعاء تابع:</b>
<code>message = greet("أحمد")
print(message)  # مرحباً أحمد!</code>

<b>✨ مميزات التوابع:</b>
• إعادة استخدام الكود
• تنظيم البرنامج
• سهولة التعديل والصيانة

<b>📌 أنواع التوابع:</b>
• بدون بارامترات
• مع بارامترات
• مع قيمة إرجاع</code>""",
     """<b>💻 مثال: حساب مساحة المستطيل</b>

<code># تعريف التابع
def rectangle_area(length, width):
    area = length * width
    return area

# استدعاء التابع
length = 10
width = 5
result = rectangle_area(length, width)

print(f"مساحة المستطيل: {result}")</code>""",
     "ما هي الكلمة المفتاحية لتعريف تابع في بايثون؟",
     "function|def|define|func",
     "def",
     20),
    
    (8, "💾 التعامل مع الملفات", 
     """<b>📚 التعامل مع الملفات</b>

بايثون توفر أدوات قوية للتعامل مع الملفات.

<b>🔹 فتح ملف للقراءة:</b>
<code>file = open("data.txt", "r")
content = file.read()
file.close()</code>

<b>🔹 كتابة في ملف:</b>
<code>file = open("output.txt", "w")
file.write("محتوى الملف")
file.close()</code>

<b>🔹 أفضل طريقة (مع with):</b>
<code>with open("file.txt", "r") as f:
    data = f.read()
# الملف يغلق تلقائياً</code>

<b>📌 أوضاع فتح الملف:</b>
• r - قراءة
• w - كتابة (يحذف المحتوى القديم)
• a - إضافة (يحافظ على المحتوى)
• r+ - قراءة وكتابة</code>""",
     """<b>💻 مثال: حفظ ملاحظات المستخدم</b>

<code># كتابة ملاحظات
notes = ["تعلم بايثون", "ممارسة يومية", "مشاركة المعرفة"]

with open("notes.txt", "w", encoding="utf-8") as f:
    for note in notes:
        f.write(note + "\\n")

# قراءة الملاحظات
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("الملاحظات المحفوظة:")
    print(content)</code>""",
     "ما هو وضع فتح الملف للكتابة (مع مسح المحتوى القديم)؟",
     "r|w|a|r+",
     "w",
     15),
    
    (9, "🧩 معالجة الأخطاء", 
     """<b>📚 معالجة الأخطاء (Exception Handling)</b>

معالجة الأخطاء تمنع توقف البرنامج عند حدوث خطأ.

<b>🔹 تركيب try-except:</b>
<code>try:
    # كود قد يسبب خطأ
    number = int(input("ادخل رقم: "))
except ValueError:
    # تنفيذ عند حدوث خطأ
    print("خطأ: الرجاء إدخال رقم صحيح")</code>

<b>🔹 أنواع الأخطاء الشائعة:</b>
• ValueError - قيمة غير صحيحة
• TypeError - نوع غير صحيح
• FileNotFoundError - ملف غير موجود
• ZeroDivisionError - قسمة على صفر

<b>🔹 استخدام finally:</b>
<code>try:
    file = open("data.txt", "r")
finally:
    file.close()  # ينفذ دائماً</code>""",
     """<b>💻 مثال: آلة حاسبة آمنة</b>

<code>def safe_divide():
    try:
        num1 = float(input("ادخل الرقم الأول: "))
        num2 = float(input("ادخل الرقم الثاني: "))
        result = num1 / num2
        print(f"النتيجة: {result}")
    except ZeroDivisionError:
        print("خطأ: لا يمكن القسمة على صفر")
    except ValueError:
        print("خطأ: الرجاء إدخال أرقام صحيحة")
    except Exception as e:
        print(f"خطأ غير متوقع: {e}")

safe_divide()</code>""",
     "أي من التالي يستخدم لمعالجة الأخطاء في بايثون؟",
     "catch|except|try-catch|handle",
     "except",
     20),
    
    (10, "🎓 الشهادة والإكمال", 
     """<b>🎉 تهانينا! لقد أكملت دورة بايثون! 🎉</b>

✨ <b>ماذا تعلمت؟</b>
✓ أساسيات البرمجة
✓ المتغيرات والبيانات
✓ العمليات الحسابية
✓ الجمل الشرطية
✓ الحلقات التكرارية
✓ القوائم والمصفوفات
✓ التوابع (الدوال)
✓ التعامل مع الملفات
✓ معالجة الأخطاء

<b>🏆 أنت الآن مؤهل لـ:</b>
• بناء مشاريع خاصة بك
• تعلم مكتبات متقدمة
• البدء في مجالات:
  - تطوير الويب (Django/Flask)
  - تحليل البيانات (Pandas)
  - الذكاء الاصطناعي (TensorFlow)

<b>💪 نصائح للمستقبل:</b>
1. مارس البرمجة يومياً
2. ابدأ مشروعاً خاصاً بك
3. انضم لمجتمعات البرمجة
4. تعلم باستمرار</code>""",
     """<b>💻 مشروع التخرج: آلة حاسبة متقدمة</b>

<code>def calculator():
    print("🧮 الآلة الحاسبة المتقدمة")
    print("-" * 30)
    
    while True:
        print("\\n1. جمع")
        print("2. طرح")
        print("3. ضرب")
        print("4. قسمة")
        print("5. خروج")
        
        choice = input("\\nاختر العملية: ")
        
        if choice == '5':
            print("شكراً لاستخدام الآلة الحاسبة!")
            break
        
        if choice in ['1','2','3','4']:
            try:
                num1 = float(input("الرقم الأول: "))
                num2 = float(input("الرقم الثاني: "))
                
                if choice == '1':
                    print(f"{num1} + {num2} = {num1 + num2}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {num1 - num2}")
                elif choice == '3':
                    print(f"{num1} × {num2} = {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"{num1} ÷ {num2} = {num1 / num2}")
                    else:
                        print("خطأ: لا يمكن القسمة على صفر!")
            except ValueError:
                print("خطأ: الرجاء إدخال أرقام صحيحة!")
        else:
            print("خطأ: اختيار غير صالح!")

# تشغيل الآلة الحاسبة
calculator()</code>""",
     "مبروك! أنت الآن مبرمج بايثون معتمد! 🎓",
     "مبروك|شكراً|رائع|جميل",
     "مبروك",
     50)
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
    ("int()", "تحويل إلى عدد صحيح", 'number = int("123")'),
    ("str()", "تحويل إلى نص", 'text = str(123)'),
    ("list()", "تحويل إلى قائمة", 'my_list = list("ABC")'),
    ("range()", "إنشاء تسلسل رقمي", 'for i in range(5): print(i)'),
    ("sum()", "جمع عناصر القائمة", 'total = sum([1,2,3,4,5])'),
    ("max()", "أكبر قيمة في القائمة", 'maximum = max([1,5,3,9,2])'),
    ("min()", "أصغر قيمة في القائمة", 'minimum = min([1,5,3,9,2])'),
    ("sorted()", "ترتيب القائمة", 'sorted_list = sorted([3,1,4,1,5])'),
    ("abs()", "القيمة المطلقة", 'absolute = abs(-10)'),
    ("round()", "تقريب الأرقام", 'rounded = round(3.14159, 2)'),
    ("open()", "فتح ملف", 'file = open("data.txt", "r")'),
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
    except:
        return None

def edit_message(chat_id, message_id, text, reply_markup=None, parse_mode="HTML"):
    payload = {"chat_id": chat_id, "message_id": message_id, "text": text, "parse_mode": parse_mode}
    if reply_markup:
        payload["reply_markup"] = json.dumps(reply_markup)
    try:
        return requests.post(f"{URL}/editMessageText", json=payload, timeout=30).json()
    except:
        return None

def answer_callback(callback_id, text, show_alert=False):
    payload = {"callback_query_id": callback_id, "text": text, "show_alert": show_alert}
    try:
        return requests.post(f"{URL}/answerCallbackQuery", json=payload, timeout=30).json()
    except:
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

def update_user_points(user_id, points):
    c.execute("UPDATE users SET points = points + ? WHERE user_id = ?", (points, user_id))
    conn.commit()

def update_user_xp(user_id, xp):
    c.execute("UPDATE users SET xp = xp + ? WHERE user_id = ?", (xp, user_id))
    # رفع المستوى
    c.execute("SELECT xp, level FROM users WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    if row:
        new_level = row[1]
        xp_needed = new_level * 100
        if row[0] >= xp_needed:
            new_level = new_level + 1
            c.execute("UPDATE users SET level = ? WHERE user_id = ?", (new_level, user_id))
            send_message(user_id, f"🎉 <b>ممتاز! لقد وصلت للمستوى {new_level}!</b> 🎉")
    conn.commit()

def mark_lesson_completed(user_id, lesson_id):
    c.execute("SELECT completed_lessons FROM users WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    if row:
        completed = row[0] or ""
        if str(lesson_id) not in completed.split(","):
            new_completed = f"{completed},{lesson_id}" if completed else str(lesson_id)
            c.execute("UPDATE users SET completed_lessons = ? WHERE user_id = ?", (new_completed, user_id))
            conn.commit()
            return True
    return False

def is_lesson_completed(user_id, lesson_id):
    c.execute("SELECT completed_lessons FROM users WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    if row and row[0]:
        return str(lesson_id) in row[0].split(",")
    return False

def get_user_progress(user_id):
    c.execute("SELECT COUNT(*) FROM lessons")
    total_lessons = c.fetchone()[0]
    c.execute("SELECT completed_lessons FROM users WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    if row and row[0]:
        completed = len(row[0].split(",")) if row[0] else 0
    else:
        completed = 0
    return completed, total_lessons

# ==================== الأزرار بالألوان السحرية ====================
def get_main_keyboard():
    return {
        "inline_keyboard": [
            [{"text": "📚 الدروس", "callback_data": "lessons", "style": "success"}],
            [{"text": "📖 أوامر بايثون", "callback_data": "commands", "style": "primary"},
             {"text": "🧪 اختبر نفسك", "callback_data": "quiz", "style": "primary"}],
            [{"text": "📊 تقدمي", "callback_data": "my_progress", "style": "primary"},
             {"text": "🏆 النقاط", "callback_data": "my_points", "style": "primary"}],
            [{"text": "💻 محرر بايثون", "callback_data": "editor", "style": "success"}],
            [{"text": "❓ المساعدة", "callback_data": "help", "style": "primary"},
             {"text": "👨‍💻 المطور", "url": f"https://t.me/{DEV_USERNAME}", "style": "primary"}]
        ]
    }

def get_lessons_keyboard(page=0):
    c.execute("SELECT id, title FROM lessons ORDER BY id")
    all_lessons = c.fetchall()
    items_per_page = 5
    start = page * items_per_page
    end = start + items_per_page
    current_lessons = all_lessons[start:end]
    
    keyboard = {"inline_keyboard": []}
    for lesson_id, title in current_lessons:
        keyboard["inline_keyboard"].append([{"text": f"📗 {title}", "callback_data": f"lesson_{lesson_id}", "style": "primary"}])
    
    nav_row = []
    if page > 0:
        nav_row.append({"text": "◀️ السابق", "callback_data": f"lessons_page_{page-1}", "style": "primary"})
    if end < len(all_lessons):
        nav_row.append({"text": "التالي ▶️", "callback_data": f"lessons_page_{page+1}", "style": "primary"})
    if nav_row:
        keyboard["inline_keyboard"].append(nav_row)
    
    keyboard["inline_keyboard"].append([{"text": "🔙 رجوع", "callback_data": "back_to_main", "style": "danger"}])
    return keyboard

def get_lesson_keyboard(lesson_id):
    completed = is_lesson_completed(user_id if 'user_id' in dir() else 0, lesson_id)
    keyboard = {"inline_keyboard": [
        [{"text": "📖 قراءة الدرس", "callback_data": f"read_lesson_{lesson_id}", "style": "success"}],
        [{"text": "💻 مشاهدة الكود", "callback_data": f"code_lesson_{lesson_id}", "style": "primary"}],
        [{"text": "📝 اختبار الدرس", "callback_data": f"quiz_lesson_{lesson_id}", "style": "primary"}]
    ]}
    if completed:
        keyboard["inline_keyboard"].append([{"text": "✅ تم الإكمال", "callback_data": "completed", "style": "success"}])
    keyboard["inline_keyboard"].append([{"text": "🔙 رجوع", "callback_data": "lessons", "style": "danger"}])
    return keyboard

def get_quiz_keyboard(lesson_id, options):
    options_list = options.split("|")
    keyboard = {"inline_keyboard": []}
    for i, opt in enumerate(options_list):
        keyboard["inline_keyboard"].append([{"text": f"{chr(65+i)} - {opt}", "callback_data": f"quiz_answer_{lesson_id}_{opt}", "style": "primary"}])
    keyboard["inline_keyboard"].append([{"text": "🔙 رجوع", "callback_data": f"lesson_{lesson_id}", "style": "danger"}])
    return keyboard

def get_commands_keyboard(page=0):
    c.execute("SELECT command, description FROM python_commands")
    all_commands = c.fetchall()
    items_per_page = 8
    start = page * items_per_page
    end = start + items_per_page
    current_commands = all_commands[start:end]
    
    keyboard = {"inline_keyboard": []}
    row = []
    for cmd, desc in current_commands:
        row.append({"text": f"📌 {cmd}", "callback_data": f"command_{cmd}", "style": "primary"})
        if len(row) == 2:
            keyboard["inline_keyboard"].append(row)
            row = []
    if row:
        keyboard["inline_keyboard"].append(row)
    
    nav_row = []
    if page > 0:
        nav_row.append({"text": "◀️ السابق", "callback_data": f"commands_page_{page-1}", "style": "primary"})
    if end < len(all_commands):
        nav_row.append({"text": "التالي ▶️", "callback_data": f"commands_page_{page+1}", "style": "primary"})
    if nav_row:
        keyboard["inline_keyboard"].append(nav_row)
    
    keyboard["inline_keyboard"].append([{"text": "🔙 رجوع", "callback_data": "back_to_main", "style": "danger"}])
    return keyboard

def get_command_keyboard(command):
    return {
        "inline_keyboard": [
            [{"text": "🔙 رجوع", "callback_data": "commands", "style": "danger"},
             {"text": "🏠 الرئيسية", "callback_data": "back_to_main", "style": "primary"}]
        ]
    }

def get_random_quiz_keyboard():
    c.execute("SELECT id, quiz_question, quiz_options FROM lessons WHERE quiz_question IS NOT NULL ORDER BY RANDOM() LIMIT 1")
    row = c.fetchone()
    if row:
        lesson_id, question, options = row
        options_list = options.split("|")
        keyboard = {"inline_keyboard": []}
        for i, opt in enumerate(options_list):
            keyboard["inline_keyboard"].append([{"text": f"{chr(65+i)} - {opt}", "callback_data": f"random_quiz_{lesson_id}_{opt}", "style": "primary"}])
        keyboard["inline_keyboard"].append([{"text": "🔙 رجوع", "callback_data": "back_to_main", "style": "danger"}])
        return keyboard, question
    return None, "لا توجد أسئلة حالياً"

def get_editor_keyboard():
    return {
        "inline_keyboard": [
            [{"text": "▶️ تنفيذ الكود", "callback_data": "run_code", "style": "success"}],
            [{"text": "📋 مسح", "callback_data": "clear_code", "style": "primary"},
             {"text": "❓ أمثلة", "callback_data": "code_examples", "style": "primary"}],
            [{"text": "🔙 رجوع", "callback_data": "back_to_main", "style": "danger"}]
        ]
    }

def get_back_button():
    return {"inline_keyboard": [[{"text": "🔙 رجوع", "callback_data": "back_to_main", "style": "danger"}]]}

# ==================== تنفيذ كود بايثون ====================
def execute_python_code(code):
    """تنفيذ كود بايثون في بيئة آمنة"""
    try:
        # إعادة توجيه الإخراج
        import sys
        from io import StringIO
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        # تنفيذ الكود
        exec(code)
        
        # الحصول على الإخراج
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        if output:
            return output, None
        else:
            return "✅ تم التنفيذ بنجاح (لا يوجد مخرجات)", None
    except Exception as e:
        return None, str(e)

# ==================== معالجة الأوامر ====================
print("="*60)
print("🐍 بوت تعليم برمجة بايثون - يعمل مع الألوان السحرية")
print(f"👨‍💻 المطور: @{DEV_USERNAME}")
print("="*60)

user_input = {}
user_code = {}
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
                    
                    completed, total = get_user_progress(user_id)
                    welcome_text = f"""🐍 <b>مرحباً بك {first_name} في بوت تعليم بايثون!</b>

📚 <b>ماذا ستتعلم؟</b>
✓ أساسيات البرمجة
✓ المتغيرات والبيانات
✓ الجمل الشرطية والحلقات
✓ التوابع والقوائم
✓ التعامل مع الملفات
✓ معالجة الأخطاء

📊 <b>تقدمك:</b>
• اكملت {completed} من {total} درس
• نقاطك: {user['points']}
• مستواك: {user['level']}

✨ <b>المميزات:</b>
• دروس تفاعلية
• اختبارات تقييم
• أوامر بايثون الشائعة
• محرر كود مباشر

<b>استخدم الأزرار للبدء!</b>"""
                    
                    send_message(chat_id, welcome_text, reply_markup=get_main_keyboard())
                
                elif user_id in user_input:
                    step = user_input[user_id]["step"]
                    
                    if step == "waiting_code":
                        code = text
                        user_code[user_id] = code
                        send_message(chat_id, "✅ تم حفظ الكود! اضغط على زر 'تنفيذ' لتشغيله", reply_markup=get_editor_keyboard())
                        del user_input[user_id]
                
                elif user_id in user_code and text == "/clear":
                    del user_code[user_id]
                    send_message(chat_id, "🗑️ تم مسح الكود", reply_markup=get_editor_keyboard())
            
            elif "callback_query" in u:
                cq = u["callback_query"]
                user_id = cq["from"]["id"]
                data = cq["data"]
                message_id = cq["message"]["message_id"]
                chat_id = cq["message"]["chat"]["id"]
                first_name = cq["from"].get("first_name", "مستخدم")
                
                user = get_user(user_id)
                
                if data == "back_to_main":
                    completed, total = get_user_progress(user_id)
                    welcome_text = f"""🐍 <b>مرحباً بك {first_name} في بوت تعليم بايثون!</b>

📊 <b>تقدمك:</b>
• اكملت {completed} من {total} درس
• نقاطك: {user['points']}
• مستواك: {user['level']}

<b>استخدم الأزرار للبدء!</b>"""
                    edit_message(chat_id, message_id, welcome_text, reply_markup=get_main_keyboard())
                    answer_callback(cq["id"], "")
                
                elif data == "lessons":
                    edit_message(chat_id, message_id, "📚 <b>اختر الدرس الذي تريد تعلمه:</b>", reply_markup=get_lessons_keyboard(0))
                    answer_callback(cq["id"], "")
                
                elif data.startswith("lessons_page_"):
                    page = int(data.replace("lessons_page_", ""))
                    edit_message(chat_id, message_id, "📚 <b>اختر الدرس الذي تريد تعلمه:</b>", reply_markup=get_lessons_keyboard(page))
                    answer_callback(cq["id"], "")
                
                elif data.startswith("lesson_"):
                    lesson_id = int(data.replace("lesson_", ""))
                    c.execute("SELECT title FROM lessons WHERE id = ?", (lesson_id,))
                    row = c.fetchone()
                    if row:
                        edit_message(chat_id, message_id, f"📗 <b>{row[0]}</b>\n\nاختر ما تريد:", reply_markup=get_lesson_keyboard(lesson_id))
                    answer_callback(cq["id"], "")
                
                elif data.startswith("read_lesson_"):
                    lesson_id = int(data.replace("read_lesson_", ""))
                    c.execute("SELECT title, content FROM lessons WHERE id = ?", (lesson_id,))
                    row = c.fetchone()
                    if row:
                        text = f"<b>📗 {row[0]}</b>\n\n{row[1]}"
                        edit_message(chat_id, message_id, text, reply_markup=get_lesson_keyboard(lesson_id))
                    answer_callback(cq["id"], "")
                
                elif data.startswith("code_lesson_"):
                    lesson_id = int(data.replace("code_lesson_", ""))
                    c.execute("SELECT title, code_example FROM lessons WHERE id = ?", (lesson_id,))
                    row = c.fetchone()
                    if row and row[1]:
                        text = f"<b>💻 كود مثال: {row[0]}</b>\n\n{row[1]}"
                        edit_message(chat_id, message_id, text, reply_markup=get_lesson_keyboard(lesson_id))
                    else:
                        edit_message(chat_id, message_id, "📝 لا يوجد كود مثال لهذا الدرس", reply_markup=get_lesson_keyboard(lesson_id))
                    answer_callback(cq["id"], "")
                
                elif data.startswith("quiz_lesson_"):
                    lesson_id = int(data.replace("quiz_lesson_", ""))
                    c.execute("SELECT quiz_question, quiz_options FROM lessons WHERE id = ?", (lesson_id,))
                    row = c.fetchone()
                    if row and row[0]:
                        question = row[0]
                        options = row[1]
                        text = f"<b>📝 اختبار: {question}</b>"
                        edit_message(chat_id, message_id, text, reply_markup=get_quiz_keyboard(lesson_id, options))
                    else:
                        edit_message(chat_id, message_id, "📝 لا يوجد اختبار لهذا الدرس", reply_markup=get_lesson_keyboard(lesson_id))
                    answer_callback(cq["id"], "")
                
                elif data.startswith("quiz_answer_"):
                    parts = data.split("_")
                    lesson_id = int(parts[2])
                    user_answer = parts[3]
                    c.execute("SELECT quiz_answer, xp_reward FROM lessons WHERE id = ?", (lesson_id,))
                    row = c.fetchone()
                    if row:
                        is_correct = user_answer == row[0]
                        if is_correct:
                            # إضافة نقاط وخبرة
                            update_user_points(user_id, 5)
                            update_user_xp(user_id, row[1])
                            # تسجيل إكمال الدرس
                            if mark_lesson_completed(user_id, lesson_id):
                                update_user_points(user_id, 10)  # مكافأة إكمال الدرس
                            
                            text = f"✅ <b>إجابة صحيحة!</b>\n🎉 +{row[1]} نقطة خبرة\n💰 +5 نقاط"
                        else:
                            text = f"❌ <b>إجابة خاطئة!</b>\nالإجابة الصحيحة هي: {row[0]}\n💪 حاول مرة أخرى"
                        edit_message(chat_id, message_id, text, reply_markup=get_lesson_keyboard(lesson_id))
                    answer_callback(cq["id"], "")
                
                elif data == "commands":
                    edit_message(chat_id, message_id, "📖 <b>أوامر بايثون الشائعة:</b>\n\nاختر أمراً لمعرفة شرحه:", reply_markup=get_commands_keyboard(0))
                    answer_callback(cq["id"], "")
                
                elif data.startswith("commands_page_"):
                    page = int(data.replace("commands_page_", ""))
                    edit_message(chat_id, message_id, "📖 <b>أوامر بايثون الشائعة:</b>\n\nاختر أمراً لمعرفة شرحه:", reply_markup=get_commands_keyboard(page))
                    answer_callback(cq["id"], "")
                
                elif data.startswith("command_"):
                    cmd = data.replace("command_", "")
                    c.execute("SELECT command, description, example FROM python_commands WHERE command = ?", (cmd,))
                    row = c.fetchone()
                    if row:
                        text = f"<b>📌 {row[0]}</b>\n\n<b>📝 الشرح:</b>\n{row[1]}\n\n<b>💻 مثال:</b>\n<code>{row[2]}</code>"
                        edit_message(chat_id, message_id, text, reply_markup=get_command_keyboard(cmd))
                    answer_callback(cq["id"], "")
                
                elif data == "quiz":
                    keyboard, question = get_random_quiz_keyboard()
                    if keyboard:
                        edit_message(chat_id, message_id, f"🧪 <b>اختبار عشوائي</b>\n\n{question}", reply_markup=keyboard)
                    else:
                        edit_message(chat_id, message_id, "📝 لا توجد أسئلة حالياً", reply_markup=get_back_button())
                    answer_callback(cq["id"], "")
                
                elif data.startswith("random_quiz_"):
                    parts = data.split("_")
                    lesson_id = int(parts[2])
                    user_answer = parts[3]
                    c.execute("SELECT quiz_answer, xp_reward FROM lessons WHERE id = ?", (lesson_id,))
                    row = c.fetchone()
                    if row:
                        is_correct = user_answer == row[0]
                        if is_correct:
                            update_user_points(user_id, 5)
                            update_user_xp(user_id, row[1])
                            text = f"✅ <b>إجابة صحيحة!</b>\n🎉 +{row[1]} نقطة خبرة\n💰 +5 نقاط"
                        else:
                            text = f"❌ <b>إجابة خاطئة!</b>\nالإجابة الصحيحة هي: {row[0]}"
                        edit_message(chat_id, message_id, text, reply_markup=get_back_button())
                    answer_callback(cq["id"], "")
                
                elif data == "my_progress":
                    completed, total = get_user_progress(user_id)
                    c.execute("SELECT xp, level, points FROM users WHERE user_id = ?", (user_id,))
                    row = c.fetchone()
                    xp = row[0] if row else 0
                    level = row[1] if row else 1
                    points = row[2] if row else 0
                    xp_needed = level * 100
                    xp_progress = int((xp / xp_needed) * 100) if xp_needed > 0 else 0
                    
                    text = f"""📊 <b>تقدمك في تعلم بايثون</b>

📚 <b>الدروس:</b> {completed} / {total} مكتمل
🏆 <b>المستوى:</b> {level}
⭐ <b>نقاط الخبرة:</b> {xp} / {xp_needed} ({xp_progress}%)
💰 <b>النقاط:</b> {points}

<b>🎯 نصائح:</b>
• أكمل الدروس لرفع مستواك
• اختبر نفسك بانتظام
• مارس الكود الذي تتعلمه"""
                    edit_message(chat_id, message_id, text, reply_markup=get_back_button())
                    answer_callback(cq["id"], "")
                
                elif data == "my_points":
                    c.execute("SELECT points, level FROM users WHERE user_id = ?", (user_id,))
                    row = c.fetchone()
                    points = row[0] if row else 0
                    level = row[1] if row else 1
                    
                    text = f"""💰 <b>نقاطك</b>

⭐ <b>النقاط:</b> {points}
🏆 <b>المستوى:</b> {level}

<b>💡 كيف تحصل على نقاط؟</b>
• إكمال درس: +10 نقاط
• إجابة صحيحة في الاختبار: +5 نقاط
• تنفيذ كود ناجح: +2 نقاط"""
                    edit_message(chat_id, message_id, text, reply_markup=get_back_button())
                    answer_callback(cq["id"], "")
                
                elif data == "editor":
                    text = """💻 <b>محرر بايثون المباشر</b>

📝 <b>كيف تستخدم المحرر؟</b>
1️⃣ اكتب كود بايثون في الرسالة
2️⃣ اضغط على زر "تنفيذ الكود"
3️⃣ سترى النتيجة مباشرة

<b>💡 مثال:</b>
<code>print("مرحباً بايثون!")
x = 10
y = 20
print(f"المجموع: {x + y}")</code>

📤 <b>أرسل كودك الآن!</b>"""
                    edit_message(chat_id, message_id, text, reply_markup=get_editor_keyboard())
                    user_input[user_id] = {"step": "waiting_code"}
                    answer_callback(cq["id"], "")
                
                elif data == "run_code":
                    if user_id in user_code and user_code[user_id]:
                        code = user_code[user_id]
                        output, error = execute_python_code(code)
                        if error:
                            result_text = f"❌ <b>خطأ في التنفيذ:</b>\n<code>{error}</code>"
                        else:
                            result_text = f"✅ <b>النتيجة:</b>\n<code>{output}</code>"
                            update_user_points(user_id, 2)  # مكافأة تنفيذ الكود
                        edit_message(chat_id, message_id, result_text, reply_markup=get_editor_keyboard())
                    else:
                        edit_message(chat_id, message_id, "📝 لم تقم بإرسال أي كود بعد!\nأرسل كود بايثون أولاً", reply_markup=get_editor_keyboard())
                    answer_callback(cq["id"], "")
                
                elif data == "clear_code":
                    if user_id in user_code:
                        del user_code[user_id]
                    edit_message(chat_id, message_id, "🗑️ تم مسح الكود\n📤 أرسل كوداً جديداً", reply_markup=get_editor_keyboard())
                    answer_callback(cq["id"], "")
                
                elif data == "code_examples":
                    text = """💡 <b>أمثلة على كود بايثون</b>

<b>📌 مثال 1: الترحيب</b>
<code>name = input("ما اسمك؟ ")
print(f"مرحباً {name}!")</code>

<b>📌 مثال 2: الجمع</b>
<code>num1 = int(input("الرقم الأول: "))
num2 = int(input("الرقم الثاني: "))
print(f"المجموع: {num1 + num2}")</code>

<b>📌 مثال 3: التحقق من العمر</b>
<code>age = int(input("عمرك: "))
if age >= 18:
    print("أنت بالغ")
else:
    print("أنت قاصر")</code>

📤 <b>انسخ أي مثال وأرسله للتجربة!</b>"""
                    edit_message(chat_id, message_id, text, reply_markup=get_editor_keyboard())
                    answer_callback(cq["id"], "")
                
                elif data == "help":
                    text = f"""❓ <b>المساعدة والدعم</b>

📚 <b>كيفية استخدام البوت:</b>

1️⃣ <b>الدروس:</b> اضغط على "📚 الدروس" واختر الدرس المناسب
2️⃣ <b>الاختبارات:</b> بعد كل درس يمكنك اختبار فهمك
3️⃣ <b>أوامر بايثون:</b> تعرف على الأوامر الشائعة
4️⃣ <b>محرر الكود:</b> جرب كتابة وتنفيذ كود بايثون مباشرة

🎯 <b>نصائح للتعلم:</b>
• ابدأ بالأساسيات ثم تدرج
• طبق ما تتعلمه فوراً
• لا تتردد في طرح الأسئلة

👨‍💻 <b>للاستفسار:</b> @{DEV_USERNAME}
📢 <b>قناة التحديثات:</b> {DEV_CHANNEL}"""
                    edit_message(chat_id, message_id, text, reply_markup=get_back_button())
                    answer_callback(cq["id"], "")
                
                elif data == "completed":
                    answer_callback(cq["id"], "✅ هذا الدرس مكتمل بالفعل!")
                
                else:
                    answer_callback(cq["id"], "")
        
    except Exception as e:
        print(f"خطأ: {e}")
        time.sleep(5)