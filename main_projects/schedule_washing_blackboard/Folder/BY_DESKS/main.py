from helper import *
from time import sleep
from os.path import exists
import telebot
import datetime
import schedule

token = ''
client = telebot.TeleBot(token)

users = []
if exists('users.txt'):
    with open('users.txt') as file_reader:
        for string in file_reader.readlines():
            users.append(string)

def get_month_of(month_number):
    if isinstance(month_number, int): month_number = str(month_number)
    monthes = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентрябрь", "Октябрь", "Ноябрь", "Декабрь"]
    return {str(value+1): key for value, key in enumerate(monthes)}[month_number]

def generate_data():
    all_values = interface()
    current_month, current_date = datetime.datetime.today().month, datetime.datetime.today().day

    if datetime.date(datetime.datetime.today().year, current_month, current_date).weekday() > 5:
        return "Сегодня никто не работает, так как сегодня выходной день"

    # desk:pair taken values
    current_workers = all_values.get("{}:{}".format(str(current_date), str(current_month))).split(':')
    #data = 'Сегодня( {} {} ) дежурит {} парта на {} ряду'.format(
    data = 'Сегодня дежурит {} парта на {} ряду'.format(
        current_workers[1], # row
        current_workers[0]  # pair
    )

    return data

def send_messages():
    data = generate_data()
    for user in users:
        client.send_message(user, data)

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

@client.message_handler(content_types = ['text'])
def get_text(message):
    data = generate_data()
    users__file = [k[:len(k)-1:] for k in open('users.txt').readlines()]

    if message.text.lower() == '/start' and str(message.chat.id) not in users__file:
        users.append(message.chat.id)
        with open('users.txt', 'a') as user_fill:
            user_fill.write(str(message.chat.id) + '\n')
        client.send_message(message.chat.id, "Окей. так, тебе каждый день будут отправляться данные по дежурству в 19:00. кря\nну или ты сам попроси командой /get")
    elif message.text.lower() == '/start' and str(message.chat.id) in users__file:
        client.send_message(message.chat.id, "вы уже в базе")

    if message.text.lower() == '/delme' and message.chat.id < 0:    pass
    elif message.text.lower() == '/delme' and str(message.chat.id) in users__file:
        users.pop(users.index(message.chat.id))
        with open('users.txt', 'a') as users_reborn:
            for user in users:
                users_reborn.write(str(user) + '\n')
        client.send_message(message.chat.id, "Done")
        previous_message_id = message.message_id
    elif message.text.lower() == '/delme' and str(message.chat.id) not in users__file:
        client.send_message(message.chat.id, "Вас нет в базе")

    if message.text.lower() == '/get' and str(message.chat.id) in users__file:
        client.send_message(message.chat.id, data)
    elif message.text.lower() == '/get' and str(message.chat.id) not in users__file:
        print("{} not in {}".format(message.chat.id, users__file))
        client.send_message(message.chat.id, "Вас нет в базе")

if __name__ == '__main__':
    # schedule.every().day.at("07:32").do(send_messages)
    # schedule.every().day.at("23:07").do(send_messages)
    # Thread(target=schedule_checker).start()

    send_messages()

    # while True:
    #    client.polling(none_stop=True)

