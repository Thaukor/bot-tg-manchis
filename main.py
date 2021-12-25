import telegram
import telegram.ext

from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler, ConversationHandler, Filters, JobQueue
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

updater = None
with open('token', 'r') as token:
    updater = Updater(token=token.read(), use_context=True)
dispatcher = updater.dispatcher

help_text = """Inserte ayuda del bot aquí"""
def help(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=help_text
    )

updater.start_polling()

# Para escuchar por señales, por ejemplo CTRL + C
updater.idle()