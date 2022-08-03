import glob
import json
import os

import requests
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import telegram

from ..viber import viber_bot


class TelegramBot():
    def __init__(self, bot_token, channel_name):
        self.channel_name=channel_name
        self.bot = telegram.Bot(token=bot_token)
        self.updater = Updater(bot_token, use_context=True)
        self.viber_handler=viber_bot.ViberSender(server_url='https://0c6f-178-36-10-40.eu.ngrok.io',
                                                  auth_token='4f88462e4fb2aba1-1e7d4b58ff9485ae-2cda7320cb96f082',)
        # self.updater.dispatcher.add_handler(MessageHandler(Filters.all, self.pass_message))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.text, self.pass_message))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.photo, self.pass_photo))

        self.updater.start_polling()


    def pass_photo(self, update: Update, context: CallbackContext):
        files = glob.glob('imgs/*')
        for f in files:
            os.remove(f)
        file = self.bot.getFile(update.message.photo[-1])
        obj = context.bot.get_file(file)
        # obj_url = f'imgs/{file.file_unique_id}.jpg'
        obj_url = f'imgs/{file.file_unique_id}.jpg'
        obj.download(obj_url)

        photo_to_send=f'https://django-viber-telegram-bot.herokuapp.com/media/{obj_url}'
        # photo_to_send='https://django-viber-telegram-bot.herokuapp.com/media/imgs/temp_.jpg'
        msg_text = update.message.text if update.message.text else ''

        a=5
        # self.bot.send_photo(chat_id=self.channel_name,
        #                     photo=photo_to_send,
        #                     caption=msg_text
        #                     )

        self.viber_handler.send_picture(msg_text,
                                   photo_to_send)

        # os.remove(obj_url)


    def pass_message(self, update: Update, context: CallbackContext):
        msg_text=update.message.text if update.message.text else ''
        if msg_text:
            self.bot.send_message(chat_id=self.channel_name, text=update.message.text, parse_mode=telegram.ParseMode.HTML)
            self.viber_handler.send_text_message(msg_text)






