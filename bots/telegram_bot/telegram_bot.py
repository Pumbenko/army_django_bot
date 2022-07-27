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
        self.updater.dispatcher.add_handler(MessageHandler(Filters.all, self.pass_message))

        self.updater.start_polling()



    def pass_message(self, update: Update, context: CallbackContext):
        a=5
        try:
            file = self.bot.getFile(update.message.photo[-1].file_id)
            obj = context.bot.get_file(file)
            obj_url=f'static/media/{file.file_unique_id}.jpg'
            obj.download(obj_url)
        except:
            obj_url=''

        a=6
        viber_handler=viber_bot.ViberSender(server_url='https://0c6f-178-36-10-40.eu.ngrok.io',
                                                  auth_token='4f88462e4fb2aba1-1e7d4b58ff9485ae-2cda7320cb96f082',)

        # self.bot.send_message(chat_id=self.channel_name, text=update.message.text, parse_mode=telegram.ParseMode.HTML)

        file = self.bot.getFile(update.message.photo[-1].file_id)
        obj = context.bot.get_file(file)
        obj_url=f'static/media/imgs/{file.file_unique_id}.jpg'
        obj.download(obj_url)
        files={'photo':open(f'https://django-viber-telegram-bot.herokuapp.com/media/imgs/{file.file_unique_id}.jpg', 'rb')}
        a=5
        msg_text=update.message.text if update.message else ' '


        requests.post(f'https://api.telegram.org/bot{self.bot.token}/sendPhoto?chat_id=@Test_army&caption={msg_text}', files=files)

        a=5
        # self.bot.send_photo(chat_id=self.channel_name,
        #                          photo=f'https://4822-178-36-10-40.eu.ngrok.io/{obj_url}'
        #                     )
        a=5

        # viber_handler.send_text_message(msg_text)

        viber_handler.send_picture(msg_text, f'https://django-viber-telegram-bot.herokuapp.com/media/imgs/{file.file_unique_id}.jpg')
        # viber_handler.send_picture(msg_text, update.channel_post.link)

        # update.message.reply_text(f'Your message has been successfully sent to desired channel! {update.message.text}')





