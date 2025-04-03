from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# تعریف زبان‌ها و متون
texts = {
    "en": {
        "start": "Hello! Welcome to my bot.",
        "button_text": "Visit our website",
        "support_text": "Support",
        "choose_language": "Please choose your language",
        "language_selected": "Language selected!"
    },
    "fa": {
        "start": "سلام! به ربات من خوش آمدید.",
        "button_text": "وب‌سایت ما",
        "support_text": "پشتیبانی",
        "choose_language": "لطفا زبان خود را انتخاب کنید",
        "language_selected": "زبان انتخاب شد!"
    }
}

# تنظیم زبان پیش‌فرض
default_language = "en"  # زبان پیش‌فرض به انگلیسی است

api_id = "3335796"
api_hash = "138b992a0e672e8346d8439c3f42ea78"
bot_token = "5088657122:AAEPiacGAxa-9fQ19keruQua74tf2-Ljktk"

app = Client("trump_voice_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token) 



# ذخیره انتخاب زبان کاربر در فایل (این‌جا به عنوان مثال از فایل استفاده می‌کنیم)
user_languages = {}

@app.on_message(filters.command("start"))
async def start_command(client, message):
    user_id = message.from_user.id

    # بررسی اینکه آیا کاربر قبلاً زبان خود را انتخاب کرده است
    if user_id not in user_languages:
        # اگر زبان انتخاب نکرده، پیام زبان را ارسال کن
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("English", callback_data="en")],
            [InlineKeyboardButton("فارسی", callback_data="fa")]
        ])
        await message.reply_text(
            texts[default_language]["choose_language"], 
            reply_markup=keyboard
        )
    else:
        # اگر زبان انتخاب کرده، پیام خوشامدگویی ارسال کن
        language = user_languages[user_id]
        start_text = texts[language]["start"]
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(texts[language]["button_text"], url="https://example.com")],
            [InlineKeyboardButton(texts[language]["support_text"], url="https://t.me/support")]
        ])
        await message.reply_text(start_text, reply_markup=keyboard)

@app.on_callback_query()
async def language_selection(client, callback_query):
    user_id = callback_query.from_user.id
    selected_language = callback_query.data

    # ذخیره زبان انتخابی کاربر
    user_languages[user_id] = selected_language

    # ارسال پاسخ سریع به کاربر به زبان انتخابی
    await callback_query.answer(texts[selected_language]["language_selected"])

    # پس از انتخاب زبان، پیام خوشامدگویی ارسال کن
    start_text = texts[selected_language]["start"]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(texts[selected_language]["button_text"], url="https://example.com")],
        [InlineKeyboardButton(texts[selected_language]["support_text"], url="https://t.me/support")]
    ])
    await callback_query.message.edit_text(start_text, reply_markup=keyboard)

app.run()
