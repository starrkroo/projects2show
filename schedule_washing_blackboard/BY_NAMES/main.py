from helper import *
from time import sleep
from os.path import exists
import telebot
import datetime
import schedule

# token = '1392582115:AAHR69NR7CwM74t5GsayoVhyfT8ZJagWdfo'
token = '5004517336:AAGrJtzhVDlXHHddwmIe5IfKrt_37vab1Yg'
client = telebot.TeleBot(token)

users = []
if exists('users.txt'):
    with open('users.txt') as file_reader:
        for string in file_reader.readlines():
            users.append(string)

def get_month_of(month_number):
    if isinstance(month_number, int): month_number = str(month_number)
    months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентрябрь", "Октябрь", "Ноябрь", "Декабрь"]
    return {str(value+1): key for value, key in enumerate(months)}[month_number]

def generate_data():
    all_values = interface()
    current_month, current_date = datetime.datetime.today().month, datetime.datetime.today().day

    if datetime.date(datetime.datetime.today().year, current_month, current_date).weekday() > 5:
        return "Сегодня никто не работает, так как сегодня выходной день"

    current_worker = all_values.get("{}:{}".format(str(current_date), str(current_month))).split(':')
    data = 'Сегодня дежурит {}'.format(
        current_worker[0]
    )

    return data


def send_messages():
    telegram_chat_id = -654521825
    client.send_message(telegram_chat_id, "hello")
    # data = generate_data()
    # for user in users:
        # client.send_message(user, data)

if __name__ == '__main__':
    send_messages()

