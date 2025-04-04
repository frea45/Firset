from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# تعریف زبان‌ها و متون
texts = {
    "en": {
        "start": "Hello! Welcome to my bot.",
        "button_text": "Visit our website",
        "support_text": "Support",
        "choose_language": "Please choose your language",
        "language_selected": "Language selected!",
    },
    "fa": {
        "start": "سلام! به ربات من خوش آمدید.",
        "button_text": "وب‌سایت ما",
        "support_text": "پشتیبانی",
        "choose_language": "لطفا زبان خود را انتخاب کنید",
        "language_selected": "زبان انتخاب شد!",
    }
}

# تنظیم زبان پیش‌فرض
default_language = "en"  # زبان پیش‌فرض به انگلیسی است

api_id = "3335796"
api_hash = "138b992a0e672e8346d8439c3f42ea78"
bot_token = "7136875110:AAFzyr2i2FbRrmst1sklkJPN7Yz2rXJvSew"

# ذخیره انتخاب زبان کاربر
user_languages = {}

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    user_id = message.from_user.id

    # اگر کاربر هنوز زبان انتخاب نکرده باشد
    if user_id not in user_languages:
        # نمایش دکمه‌های انتخاب زبان
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("English", callback_data="en")],
            [InlineKeyboardButton("فارسی", callback_data="fa")]
        ])
        await message.reply_text(
            texts[default_language]["choose_language"], 
            reply_markup=keyboard
        )
    else:
        # اگر زبان انتخاب کرده باشد، پیام خوشامدگویی ارسال می‌کنیم
        language = user_languages[user_id]
        start_text = texts[language]["start"]
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(texts[language]["button_text"], url="https://example.com")],
            [InlineKeyboardButton(texts[language]["support_text"], url="https://t.me/support")]
        ])
        await message.reply_text(start_text, reply_markup=keyboard)

@app.on_callback_query(filters.regex("^(en|fa)$"))
async def language_selection(client, callback_query):
    user_id = callback_query.from_user.id
    selected_language = callback_query.data

    # ذخیره زبان انتخابی کاربر
    user_languages[user_id] = selected_language

    # ویرایش پیام انتخاب زبان و جایگزینی با پیام خوشامدگویی (start)
    language = selected_language
    start_text = texts[language]["start"]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(texts[language]["button_text"], url="https://example.com")],
        [InlineKeyboardButton(texts[language]["support_text"], url="https://t.me/support")]
    ])

    # ویرایش پیام انتخاب زبان و حذف پیام "choose_language"
    await callback_query.message.edit_text(
        start_text, 
        reply_markup=keyboard
    )

    # ارسال پاسخ با پیام دو زبانه برای انتخاب زبان
    language_selected_message = texts[language]["language_selected"]
    await callback_query.answer(text=language_selected_message, show_alert=False)

if __name__ == "__main__":
    app.run()
