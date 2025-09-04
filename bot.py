from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# Get bot token from environment variable (Render secret)
TOKEN = os.getenv("YOUR_BOT_TOKEN")

# --- Commands ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Inline Keyboard (with links)
    inline_keyboard = [
        [InlineKeyboardButton("📡 Website", url="https://your-website.com")],
        [InlineKeyboardButton("📞 Contact", url="https://t.me/NamadevR911")],
        [InlineKeyboardButton("📲📲 Channel", url="https://t.me/your_channel")]
    ]
    inline_markup = InlineKeyboardMarkup(inline_keyboard)

    # Reply Keyboard (normal buttons)
    reply_keyboard = [
        ["📡 Website", "📞 Contact"],
        ["📲📲 Channel"]
    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

    # Send message with both keyboards
    await update.message.reply_text(
        "Welcome! Choose an option:",
        reply_markup=inline_markup
    )
    await update.message.reply_text(
        "Or use the quick buttons below 👇",
        reply_markup=reply_markup
    )

# --- Main ---
def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Still keep Callback handler (if you add future callback buttons)
    app.add_handler(CallbackQueryHandler(lambda u, c: u.callback_query.answer()))

    app.run_polling()

if __name__ == "__main__":
    main()
