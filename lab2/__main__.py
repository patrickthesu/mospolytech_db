import telebot

from scraper import get_students_groups_list
from parser import schedule_parser
from models import Connection
from config import TELEGRAM_BOT_TOKEN


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['polytech'])
def send_polytech_link(message):
    bot.reply_to(message, 'e.mospolytech.ru')
    

@bot.message_handler(commands=['help'])
def send_day_schedule(message):
    bot.reply_to(message, '''This is help message...''')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, '''This is help message...''')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    conn = Connection()
    conn.reinstall()

    groups_list = []
    for group in conn.get_groups_list():
        schedule_parser(group[1], group[0])
        #groups_list.append(group[1])

    #schedule_parser(group_name)
