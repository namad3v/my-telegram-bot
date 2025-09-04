from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
import os

# Get bot token from environment variable (Render secret)
TOKEN = os.getenv("YOUR_BOT_TOKEN")

# --- Links ---
WEBSITE_URL = "https://your-website.com"
CONTACT_URL = "https://t.me/NamadevR911"
CHANNEL_URL = "https://t.me/your_channel"

# --- Commands ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Inline Keyboard (with links)
    inline_keyboard = [
        [InlineKeyboardButton("📡 Website", url=WEBSITE_URL)],
        [InlineKeyboardButton("📞 Contact", url=CONTACT_URL)],
        [InlineKeyboardButton("📲📲 Channel", url=CHANNEL_URL)]
    ]
    inline_markup = InlineKeyboardMarkup(inline_keyboard)

    # Reply Keyboard (persistent buttons below chat)
    reply_keyboard = [
        ["📡 Website", "📞 Contact"],
        ["📲📲 Channel"]
    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Welcome! Choose an option:",
        reply_markup=inline_markup
    )
    await update.message.reply_text(
        "Or use the quick buttons below 👇",
        reply_markup=reply_markup
    )

# --- Reply Button Handler ---
async def reply_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📡 Website":
        await update.message.reply_text(f"🌐 Open Website: {https://calphs0.free.nf/?i=1}")
    elif text == "📞 Contact":
        await update.message.reply_text(f"📞 Contact here: {https://t.me/NamadevR911}")
    elif text == "📲📲 Channel":
        await update.message.reply_text(f"📲 Join Channel: {https://t.me/mrimproperGamer01}")

# --- Main ---
def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Reply button text handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_handler))

    # Inline callback handler
    app.add_handler(CallbackQueryHandler(lambda u, c: u.callback_query.answer()))

    app.run_polling()

if __name__ == "__main__":
    main()
