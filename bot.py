import telebot
import os
from fuzzywuzzy import fuzz
from telebot import types
from aiogram import types
bot = telebot.TeleBot('5983790703:AAEojaK1tyvoq5IfdWmuO6dWcfieYMK4xto')

# @bot.message_handler(commands=['start'])
# def start(message):
#     mess = f'Hello. Welcome to our Employment Agency, <b>{message.from_user.first_name} <u> {message.from_user.last_name} </u></b>'
#     bot.send_message(message.chat.id, mess, parse_mode='html')
#
#
# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, 'Wow, that is a cool photo')
#
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Visit the website", url="https://jetexpo.info/"))
#     bot.send_message(message.chat.id, "Go to the site", reply_markup=markup)

# @bot.message_handler(commands=['help'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     website = types.InlineKeyboardButton('Web site')
#     start = types.KeyboardButton('Start')
#     markup.add(website, start)
#     bot.send_message(message.chat.id, "Go to the site", reply_markup=markup)
#
# # @bot.message_handler()
# # def get_user_text(message):
# #     if message.text == "Hello":
# #         bot.send_message(message.chat.id, "Hi", parse_mode='html')
# #     elif message.text == "id":
# #         bot.send_message(message.chat.id, f"Your ID:{message.from_user.id}", parse_mode='html')
# #     elif message.text == "photo":
# #         photo = open('ays.jpg', 'rb')
# #         bot.send_photo(message.chat.id, photo)
# #     else:
# #         bot.send_message(message.chat.id, " I can not understand you", parse_mode='html')
#
# @bot.message_handler(content_types=['photo', 'document'])
# def handler_file(message):
#     from pathlib import Path
#     Path(f'files/{message.chat.id}/').mkdir(parents=True, exist_ok=True)
#     if message.content_type == 'photo':
#         file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
#         downloaded_file = bot.download_file(file_info.file_path)
#         src = f'files/{message.chat.id}/' + file_info.file_path.replace('photos/', '')
#         with open(src, 'wb') as new_file:
#             new_file.write(downloaded_file)
#     elif message.content_type == 'document':
#         file_info = bot.get_file(message.document.file_id)
#         downloaded_file = bot.download_file(file_info.file_path)
#
#         src = f'files/{message.chat.id}/' + message.document.file_name
#         with open(src, 'wb') as new_file:
#             new_file.write(downloaded_file)

# Загружаем список фраз и ответов в массив
mas = []
if os.path.exists('data/boltun.txt'):
    f=open('data/boltun.txt', 'r', encoding='UTF-8')
    for x in f:
        if(len(x.strip()) > 2):
            mas.append(x.strip().lower())
    f.close()
# С помощью fuzzywuzzy вычисляем наиболее похожую фразу и выдаем в качестве ответа следующий элемент списка
def answer(text):
    try:
        text=text.lower().strip()
        if os.path.exists('data/boltun.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mas:
                if('u: ' in q):
                    # С помощью fuzzywuzzy получаем, насколько похожи две строки
                    aa=(fuzz.token_sort_ratio(q.replace('u: ',''), text))
                    if(aa > a and aa!= a):
                        a = aa
                        nn = n
                n = n + 1
            s = mas[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'
# Команда «Старт»
@bot.message_handler(commands=["start"])
def start(m, res=False):
        bot.send_message(m.chat.id, 'Я на связи. Напиши мне Привет )')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Запись логов
    f = open('data/' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    s = answer(message.text)
    f.write('u: ' + message.text + '\n' + s + '\n')
    f.close()
    # Отправка ответа
    bot.send_message(message.chat.id, s)


bot.polling(none_stop=True, interval=0)
