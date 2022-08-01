############################# 
#
# BOT made by Vlascenko Alexander
#
#############################

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from credits import bot_token
import eisbach

bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Herzlich Willkommen! Auf den Befehl '/temp', wird die aktuelle Temperatur des Eisbachs angezeigt.")

def temp(update, context):
    tempObject = eisbach.Eisbach()
    temperatur = tempObject.getTemperatur()
    context.bot.send_message(update.effective_chat.id, str(temperatur))


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

temp_handler = CommandHandler("temp", temp)
dispatcher.add_handler(temp_handler)

updater.start_polling()
updater.idle()