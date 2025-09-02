from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

# Get bot token from environment variable (Render secret)
TOKEN = os.getenv("YOUR_BOT_TOKEN")

# --- Commands ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📝 Register", callback_data="register")],
        [InlineKeyboardButton("📞 Contact", url="https://t.me/NamadevR911")],
        [InlineKeyboardButton("❌ Cancel", callback_data="cancel")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Choose an option:", reply_markup=reply_markup)

# --- Button Callbacks ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge button press
    data = query.data

    if data == "register":
        await query.message.reply_text("📋 Registration process started...")
    elif data == "cancel":
        await query.message.reply_text("❌ Process canceled! You can now use other commands.")

# --- Main ---
def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Button handler
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, button_handler))
    app.add_handler(CommandHandler("cancel", start))
    app.add_handler(CommandHandler("register", start))
    app.add_handler(CommandHandler("contact", start))
    app.add_handler(MessageHandler(filters.ALL, button_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
