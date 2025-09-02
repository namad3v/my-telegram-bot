from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

# Get bot token from environment variable (Render secret)
TOKEN = os.getenv("YOUR_BOT_TOKEN")

# --- Commands ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["📝 Register", "📞 Contact"], ["❌ Cancel"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Welcome! Choose an option:", reply_markup=reply_markup)

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Process canceled! You can now use other commands.")

# --- Button Clicks ---
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📝 Register":
        await update.message.reply_text("📋 Registration process started...")
    elif text == "📞 Contact":
        await update.message.reply_text("📞 Contact: @NamadevR911")
    elif text == "❌ Cancel":
        await cancel(update, context)  # reuse cancel function
    else:
        await update.message.reply_text("⚠️ Unknown option. Please choose from the menu.")

# --- Main ---
def main():
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cancel", cancel))

    # Handle button clicks (text messages)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    app.run_polling()

if __name__ == "__main__":
    main()
