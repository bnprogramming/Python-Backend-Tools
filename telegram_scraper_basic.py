import functools
import threading

import telebot

from bs4_utils import Browser
from logger import logger

API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)


class TelegramScrapper:
    def __init__(self):
        self.link_button = telebot.types.InlineKeyboardButton(text='More Info')
        self.chat_id = None
        self.browser = None
        self.tele_scrapper = None

    @staticmethod
    def print_function_decorator(name):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                logger.info(f" Scraping ({name}) Started . . .")

                func(*args, **kwargs)

                logger.info(f" Scraping ({name}) Finished")

            return wrapper

        return decorator


# Button Callbacks handler
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    timer_thread = None
    if call.data == "":
        timer_thread = threading.Thread(target=None)

    timer_thread.start()
    timer_thread.join()


# Command message handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Bot is Working .... be patient 🙏')
    tele_scrapper.chat_id = message.chat.id
    tele_scrapper.browser = Browser()


# Polling ...
def start_bot():
    bot.polling()


if __name__ == '__main__':
    tele_scrapper = TelegramScrapper()
    logger.info("Please send /Start command in bot")
    bot_thread = threading.Thread(target=start_bot, )
    bot_thread.start()
