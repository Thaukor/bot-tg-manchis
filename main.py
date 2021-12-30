import telegram
import telegram.ext

from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler, ConversationHandler, Filters, JobQueue
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import requests
import re

RANDOM_CAT_API = ""

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

def get_image_url(url: str) -> str: # Conseguir el url de una imagen
    contents = requests.get(url).json()
    img: str = contents['url']
    return img

def get_random(url: str) -> str:
    """Recibe imágenes hasta conseguir una con la extensión permitida"""
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    img: str = ''
    attempts_max = 1000
    atmps = 0
    while file_extension not in allowed_extension:
        img = get_image_url(url)
        file_extension = re.search("([^.]*)$",url).group(1).lower()
        if atmps > attempts_max:
            break
        atmps += 1
    return img

def random(update: Update, context: CallbackContext) -> None:
    """Envía un gato random"""

# Handler del comando start. Cuando alguien escriba /start, esta función se ejecutará
start_handler = CommandHandler("start", start)
# Registrar handler
dispatcher.add_handler(start_handler)


# Recibir actualizaciones de Telegram
updater.start_polling()

# Para escuchar por señales, por ejemplo CTRL + C
updater.idle()