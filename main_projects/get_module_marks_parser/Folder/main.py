import helper
import telebot
import datetime
import sqlite3
from time import sleep
from telebot import types
from huepy import *
from config import *


token = Config.TOKEN
client = telebot.TeleBot(token, threaded=False)

conn = sqlite3.connect('main.db')
cursor = conn.cursor()

my_id = "749909723"
# my_id = "0"

# boolean variable to check if user want to make registration
to_regist = False

# helper.paste_in_db(my_id, "Махмудов", "Омар", "Махмудович", "01420")

ids = [k for k in helper.get_all_(ids=True)]

ID_AND_USER = {
    ids[i]: helper.students[i] for i in range(len(ids))
}

def get_id_of(query_name: str):
    for id, name in ID_AND_USER.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if helper.get_student(query_name) == name:
            return id

    return -1

def lost_users():
    """
        Пользователи, которые не ввели свои id при режиме ожидания
    """
    for k in range(1, 4):
        print(ID_AND_USER[f'empty{k}'])

def fill_in_file(data):
    """
        Рассылка сообщений всем пользователям
    """
    with open("data.txt", 'a') as f:
        f.write(data)

def send_all(message):
    for user in ids:
        try:
            if "empty" not in user:
                client.send_message(str(user), message)
        except telebot.apihelper.ApiTelegramException:
            pass


errors = {
    "0x00000001": "Ошибка построения исходного сообщения. Отправляется пустое сообщение",
    "0x00000002": "Вас нет в базе айдишников студентов. Чтобы зарегистрироваться введите команду /start",
}


@client.message_handler(commands=['help', 'start'])
def create_reply_buttons(message):
    # либо пользователь регается, либо его приветствуют по команде /start
    global to_regist
    if str(message.chat.id) not in ids:
        client.send_message(message.chat.id, """Вам нужно зарегистрироваться. Введите свое ФИО и пароль, руководствуясь следующим экземпляром:
--> Иванов Иван Иванович 00110
И после регистрации заново введите команду /start, если не будет допущено ошибок при регистрации""")
        to_regist = True
        return
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
    start_button = types.KeyboardButton("/start")
    standart_button = types.KeyboardButton("/info")

    markup_reply.add(start_button, standart_button)
    client.send_message(
        message.chat.id, 
        "Привет, {}\nЧтобы продолжить жмякай сюда /info".format(),
        reply_markup = markup_reply)


@client.message_handler(commands=['get_info', 'info'])
def get_user_query(message):
    # обработка отправки запросов через встроенные клавиши (которые под вводом)
    print(orange("<{}> {} ({})".format(datetime.datetime.now(), message.from_user.first_name, message.from_user.id)))

    if message.from_user.id == my_id:
        client.send_message(message.from_user.id, 
            """Ваши команды, сир: 
/get <name> -- получить данные о <name>
/get mean <name> -- получить среднее арифметическое баллов у <name>
/get find <name> -- найти пользователя в базе данных
/get users -- отобразить всех пользователей
/get -- получить данные о себе
/get mean -- получить среднее арифемтическое баллов о себе"""
            )
    markup_inline = types.InlineKeyboardMarkup(row_width=1)
    item_all = types.InlineKeyboardButton(text = "🩸 Модульные".upper(), callback_data = "all")
    item_mean = types.InlineKeyboardButton(text = "🩸 Средние модульные (зачет/незачет)".upper(), callback_data = "mean")

    markup_inline.add(item_all, item_mean)
    client.send_message(message.chat.id, "Выбери:", 
        reply_markup = markup_inline
    )

@client.callback_query_handler(func = lambda call: True)
def answer(call):
    defined_errors = []
    data_send = ''

    if '/get' in call.message.text.lower(): return

    if str(call.message.chat.id) in ID_AND_USER.keys():
        data = helper.generate_response(ID_AND_USER[str(call.message.chat.id)])
        
        if data == {}:
            defined_errors.append("0x00000001")

        data_send = data

        if len(defined_errors) == 0:
            if call.data == 'all':
                for k in data_send.keys():
                    taken = data_send[k]
                    taken = [k for k in taken if k != '' and k.isdigit()]
                    given = taken
                    data_send[k] = given
                client.send_message(call.message.chat.id, '\n\n'.join(helper.correct_show(data_send).split('\n')))
                return
            elif call.data == 'mean':
                data_send = {
                    list(data.keys())[i]:
                    ''.join([k for k in data[list(data.keys())[i]] if not k.isdigit() and k != '']) 
                            if ''.join([k for k in data[list(data.keys())[i]] if not k.isdigit() and k != '']) != '' else "НЕ ВЫСТАВЛЕНО"
                    for i in range(len(data))
                }
                    # mean = lambda x: (
                    #     sum([int(k) for k in x if k != 0 and k.isdigit()]) \
                    #         /                                               \
                    #     len([k for k in x if k != '' and k.isdigit()]))
                    # data_send = {
                    #         list(data.keys())[i]: 
                    #             str(round(mean(data[list(data.keys())[i]]), 1)) + " (зачет)" if round(mean(data[list(data.keys())[i]]), 1) >= 51 else str(round(mean(data[list(data.keys())[i]]), 1)) + " (незачет)"
                    #     for i in range(len(data))
                    # }           

    elif str(call.message.chat.id) not in ID_AND_USER.keys():
        defined_errors.append("0x00000002")

    if len(defined_errors) != 0:
        client.send_message(call.message.chat.id, '\n'.join([k + ' ' + errors[k] for k in defined_errors]))
    elif len(defined_errors) == 0:
        data_send = '\n\n'.join(str(helper.correct_show(data_send)).split('\n'))
        client.send_message(call.message.chat.id, data_send)

def update_variables(username, user_id, user_password):
    # обновление переменных когда подключается юзер
    ID_AND_USER.update({str(user_id): username})
    ids.append(str(user_id))
    helper.USERS.update({username: str(user_password)})

@client.message_handler(content_types = ['text'])
def TAPI(message):
    # my_id = '1'
    global to_regist
    if '/get' not in message.text.lower() and to_regist:
        username = message.text.split()
        try:
            username[3]
        except:
            client.send_message(message.chat.id, "Я что плохо объяснил Тебе как правильно заполнять форму?")
            return
        connection = helper.make_query(username[0] + ' ' + username[1] + ' ' + username [2], username[3])
        if connection.url != helper.url:
            helper.paste_in_db(
                str(message.chat.id),
                username[0],
                username[1],
                username[2],
                username[3]
            )
            print(green("<{}> {}").format(datetime.datetime.now(), message.text))
            client.send_message(message.chat.id, "Вы зарегистрированы!")
            update_variables(username[0] + ' ' + username[1] + ' ' + username [2], message.chat.id, username[3])
            to_regist = False
        else:
            client.send_message(message.chat.id, "Перепроверьте отправленные данные")

        connection.close()
        return

    # if '/get' not in message.text.lower() or '/get' in message.text.lower() and message.chat.id != my_id:
    if '/' in message.text.lower() and str(message.chat.id) != my_id:
        client.send_message(message.chat.id, message.text)
        return

    keywords = ['mean', 'users', 'find']
    student = ''
    current_keyword = ''.join([k for k in message.text.lower().split() if k in keywords])
    defined_errors = []
    data_send = '' # output data to send user

    if '/get' in message.text.lower() and str(message.chat.id) == my_id: #or len(message.text.lower()) > len('/get'):
        if len([k for k in keywords if k in message.text.lower()]):
            # generate new student's name
            student = message.text.split(current_keyword)[1].strip()
        else:
            student = message.text.split("/get")[1].strip()

        if helper.get_student(student) == -1:
            client.send_message(message.chat.id, "Такого пользователя нет в базе данных")
            return

        # generates main output table
        data = helper.generate_response(student)

        # if user is not in list, not exist
        if data == {}:
            defined_errors.append('0x00000001')
        
        if len(defined_errors) == 0:
            # getting those keywords
            if current_keyword == 'mean':
                mean = lambda x: (
                    sum([int(k) for k in x if k != 0 and k.isdigit()]) \
                        /                                               \
                    len([k for k in x if k != '' and k.isdigit()]))
                data_send = {
                    list(data.keys())[i]: 
                    str(round(mean(data[list(data.keys())[i]]), 1)) + " (зачет)" if round(mean(data[list(data.keys())[i]]), 1) >= 51 else str(round(mean(data[list(data.keys())[i]]), 1)) + " (незачет)"
                for i in range(len(data))}
            elif current_keyword == 'users':
                all_users = helper.get_all_(students = True, passwords = True, ids = True)
                # NOTE: почему выводятся не все пользователи?
                users = [str(all_users[k]) for k in range(len(all_users))]
                client.send_message(message.chat.id, '\n'.join(users))
                return
            elif current_keyword == 'find':
                data_send = data
                data_send = str(helper.find(str(get_id_of(student)))) + '\n\n\n' + '\n\n'.join(helper.correct_show(data_send).split('\n'))
                client.send_message(message.chat.id, data_send)
                return
            else:
                data_send = data


            data_send = '\n\n'.join(str(helper.correct_show(data_send)).split('\n'))


    if helper.get_student(student) not in ID_AND_USER.values():
        defined_errors.append("0x00000002")

    if len(defined_errors) != 0:
        client.send_message(message.chat.id, '\n'.join([k + " " + errors[k] for k in defined_errors]))
    elif len(defined_errors) == 0:
        try:
            client.send_message(message.chat.id, data_send)
        except:
            client.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    message = '''
    Обновление 2.1.1



Чтобы начать работать с ботом, напишите или нажмите /start

ВАЖНОЕ ЗАМЕЧАНИЕ: бот работает в бета режиме

Все свежие обновления будут приходить всем рассылкой. 
'''
    # send_all(message)


    # https://ru.stackoverflow.com/questions/711998/%D0%9D%D0%B5%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D1%82%D0%BE%D0%BA-bot-polling
    # https://habr.com/ru/post/448310/
    # what is mean proxy? if nothing works, try using proxy

    # client.polling(none_stop=True)

    while True:
        try:
            client.polling(none_stop=True)

        except Exception as e:
            print(e)  # или просто print(e) если у вас логгера нет,
            sleep(15)

    cursor.close()
    conn.close()

