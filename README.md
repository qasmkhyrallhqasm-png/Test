# 🐍 بوت تعليم برمجة بايثون على Telegram

بوت تلغرام تعليمي لتعلم لغة برمجة Python بطريقة تفاعلية وممتعة.

## ✨ المميزات

- 📚 دروس تفاعلية شاملة
- 🧪 اختبارات تقييم لكل درس
- 🏆 نظام نقاط ومستويات
- 💻 محرر كود مباشر
- 📊 تتبع التقدم
- 📖 أوامر بايثون الشائعة

## 🚀 البدء السريع

### المتطلبات
- Python 3.8+
- حساب Telegram
- Telegram Bot Token

### التثبيت المحلي

```bash
# استنساخ المستودع
git clone https://github.com/qasmkhyrallhqasm-png/Test.git
cd Test

# إنشاء بيئة افتراضية
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# تثبيت المكتبات
pip install -r requirements.txt

# إنشاء ملف .env
cp .env.example .env

# تعديل .env بإضافة بيانات البوت
# TOKEN=your_bot_token
# ADMIN_ID=your_admin_id

# تشغيل البوت
python bot.py
```

## 📱 النشر على Railway

### الخطوات:

1. **إنشاء حساب على Railway**
   - اذهب إلى https://railway.app
   - اضغط "Deploy Now"

2. **ربط المستودع**
   - اختر GitHub
   - اختر المستودع `Test`

3. **إضافة متغيرات البيئة**
   - في لوحة Railway، اذهب إلى "Variables"
   - أضف:
     ```
     TOKEN=your_telegram_bot_token
     ADMIN_ID=your_admin_id
     DEV_USERNAME=qasmkhyrallhqasm-png
     DEV_CHANNEL=https://t.me/prgtop
     ```

4. **النشر**
   - اضغط "Deploy"
   - انتظر انتهاء التثبيت
   - تحقق من الأدوات في Dashboard

## 🎓 محتوى الدروس

1. 🐍 مقدمة في بايثون
2. 📦 المتغيرات والبيانات
3. 🔢 العمليات الحسابية
4. 🎯 الجمل الشرطية
5. 🔄 الحلقات التكرارية
6. 📋 القوائس (Lists)
7. 📝 التوابع (Functions)
8. 💾 التعامل مع الملفات
9. 🧩 معالجة الأخطاء
10. 🎓 الشهادة والإكمال

## 🤖 أوامر البوت

- `/start` - بدء البوت
- `📚 الدروس` - قائمة الدروس
- `❓ المساعدة` - التعليمات
- `📊 التقدم` - عرض التقدم

## 📝 هيكل المشروع

```
Test/
├── bot.py              # البرنامج الرئيسي
├── requirements.txt    # المكتبات المطلوبة
├── .env.example       # متغيرات البيئة النموذجية
├── .gitignore         # ملفات Git المستثناة
├── Procfile           # إعدادات Heroku/Railway
├── railway.toml       # إعدادات Railway
├── index.html         # واجهة الويب
└── README.md          # هذا الملف
```

## 🔧 استكشاف الأخطاء

### البوت لا يستجيب
- تحقق من TOKEN في ملف .env
- تأكد من أن البوت يعمل على Railway
- تحقق من السجلات (Logs) في Dashboard

### خطأ في قاعدة البيانات
- احذف ملف `python_bot.db`
- أعد تشغيل البوت

### خطأ في الاتصال بـ API
- تحقق من الاتصال بالإنترنت
- تأكد من صحة TOKEN

## 🔐 الأمان

- لا تشارك TOKEN الخاص بك
- استخدم ملف .env لحفظ البيانات الحساسة
- لا ترفع .env إلى Git

## 📚 الموارد المفيدة

- [توثيق Python](https://docs.python.org/3/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Railway Documentation](https://docs.railway.app/)

## 🤝 المساهمة

نرحب بالمساهمات! يمكنك:
- إضافة دروس جديدة
- تحسين الواجهة
- إصلاح الأخطاء
- اقتراح ميزات جديدة

## 📞 التواصل

- 👨‍💻 المطور: [@qasmkhyrallhqasm-png](https://t.me/qasmkhyrallhqasm-png)
- 📢 القناة: [prgtop](https://t.me/prgtop)

## 📄 الترخيص

هذا المشروع مفتوح المصدر ومتاح للاستخدام الحر.

---

**صُنع بـ ❤️ من قبل @qasmkhyrallhqasm-png**
