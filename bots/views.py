from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from bots import credentials
from bots.telegram_bot.telegram_bot import TelegramBot


def index(request):
    # TelegramBot(bot_token=credentials.bot_token, channel_name='@Test_army')
    return HttpResponse("index")