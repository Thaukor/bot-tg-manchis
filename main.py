import telegram
import telegram.ext

from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler, ConversationHandler, Filters, JobQueue
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import requests
import re

RANDOM_SHIBA_API = "http://shibe.online/api/shibes"
RANDOM_CAT_API = "https://apilist.fun/out/randomcat"

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

def get_image_url(url: str) -> str:
    """Consigue URL de una imagen"""
    contents = requests.get(url).json()
    img: str = contents['file']
    return img

def get_shiba_url(url: str) -> str:
    """Consigue URL de una imagen"""
    contents = requests.get(url).json()
    img: str = contents[0]
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

def random_cat(update: Update, context: CallbackContext) -> None:
    """Envía un gato aleatorio"""
    url = get_image_url(RANDOM_CAT_API)
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url, caption="Sonidos de manchi observadora")

def random_shiba(update: Update, context: CallbackContext) -> None:
    url = get_shiba_url(RANDOM_SHIBA_API)
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url, caption="Sonidos de manchi observadora")

# Handler del comando start. Cuando alguien escriba /start, esta función se ejecutará
start_handler = CommandHandler("start", start)
# Registrar handler
dispatcher.add_handler(start_handler)

random_cat_handler = CommandHandler('cat', random_cat)
dispatcher.add_handler(random_cat_handler)

random_shiba_handler = CommandHandler('shiba', random_shiba)
dispatcher.add_handler(random_shiba_handler)

# Recibir actualizaciones de Telegram
updater.start_polling()

# Para escuchar por señales, por ejemplo CTRL + C
updater.idle()