import telegram
import telegram.ext

from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler, ConversationHandler, Filters, JobQueue
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

updater = None
with open('token', 'r') as token:
    updater = Updater(token=token.read(), use_context=True) # Leer token
dispatcher = updater.dispatcher # Facilitar acceso a dispatcher

help_text = """Inserte ayuda del bot aquí"""
def help(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=help_text
    )

def start(update: Update, context: CallbackContext) -> None:
    # Enviar mensaje.
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Sonidos de manchi exigente"
    )

# Handler del comando start. Cuando alguien escriba /start, esta función se ejecutará
start_handler = CommandHandler("start", start)
# Registrar handler
dispatcher.add_handler(start_handler)


# Recibir actualizaciones de Telegram
updater.start_polling()

# Para escuchar por señales, por ejemplo CTRL + C
updater.idle()