import telebot
import helper


# TODO: создать счетчик времени, каждый день в 12 ночи очищать стек сообщений
# TODO: как сделать так чтобы помимо фотографии, брался текст прикрепленный к фотке
# TODO: просто написать функцию, которая будет записывать в последнюю очередьредактированное сообщение


token = '1392582115:AAHR69NR7CwM74t5GsayoVhyfT8ZJagWdfo'
client = telebot.TeleBot(token)

CHAT_ID = -1001197674663
# testing data
CHAT_ID = -1001441977086

# id: name
USERS_INFO = {helper.STUDENT_IDS[i]: helper.STUDENT_NAMES.split('\n')[1:][i].strip()
              for i in range(len(helper.STUDENT_IDS))}

# id: messages
USERS_STORED_MESSAGES = {
    helper.STUDENT_IDS[i]: [] for i in range(len(helper.STUDENT_IDS))
}

USERS_INFO = {"1360742497": "Mom", "749909723": "Me"}
USERS_STORED_MESSAGES = {
    "1360742497": [],
    "749909723": [],
}

@client.message_handler(content_types = ['text', 'photo'])
def index_function(message):
    IMAGE_COUNTER = 0
    if message.chat.type == "supergroup" and message.chat.id == CHAT_ID:
        # if photo sent
        if message.photo is not None:
            photo_id = message.photo[-1].file_id
            print(message.photo)
            file_info = client.get_file(photo_id)
            downloaded_file = client.download_file(file_info.file_path)
            with open(f"stored_images/image{IMAGE_COUNTER}.jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
                IMAGE_COUNTER += 1

        # if text sent
        if message.chat.id == CHAT_ID:
            last_message_id = message.from_user.id
            print(last_message_id)
            if str(last_message_id) in USERS_STORED_MESSAGES:
                USERS_STORED_MESSAGES[str(last_message_id)].append(
                    message.text
                )


        print(USERS_STORED_MESSAGES)


    #if (int)(message.chat.id) == abs(chat_id):
    #    print("yes")

if __name__ == '__main__':
    while True:
       client.polling(none_stop=True)