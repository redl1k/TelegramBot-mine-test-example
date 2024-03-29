from settings import TG_TOKEN, TG_API_URL
import telebot
from telebot import types
import sqlite3
bot = telebot.TeleBot("Ur bot Token")
Privet = ['Hello', 'Hi', 'qq', 'ку', 'Привет', 'привет', 'прив', 'хай', 'хэллоу', "Ку", "Прив"]

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text in Privet:
        bot.reply_to(message, "Привет бро!\nНапиши /reg, чтобы зарегистрироваться:)")

    elif message.text == '/reg':
        # connect DB and create table
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS login_id( 
		        id INTEGER 
		    )""")
        connect.commit()

        # Проверка на существование в бд этого айди
        people_id = message.chat.id
        cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
        data = cursor.fetchone()
        if data is None:
            # Добавление значения в поля
            bot.send_message(message.from_user.id, 'Давай познакомимся!\nКак тебя зовут?')
            bot.register_next_step_handler(message, reg_name)
            user_id = [message.chat.id]
            cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
            connect.commit()
        else:
            bot.send_message(message.chat.id, 'Такой пользователь уже существует')


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, reg_surname)


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Из какой ты группы?')
    bot.register_next_step_handler(message, reg_group)

def reg_group(message):
    global group
    group = message.chat.id
    text1 = message.text
    bot.send_message(message.from_user.id, 'Спасибо, я запомнил что ты из ' + text1 + '.')

    #        bot.send_message(age, 'Возраст должен быть числом, введи ещё раз.')
    #          # askSource
    #        return
    #    bot.send_message(age, 'Спасибо, я запомнил что тебе ' + text1 + ' лет.'
    # bot.send_message(message.from_user.id, 'Тебе'+srt(age)+'лет? И тебя зовут: '+name+' '+surname+' ?')
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = ('Проверь введеные данные:\n'
                'Тебя зовут: ' + name + ' ' + surname + ' \n'
                                                        'И ты из группы:' + text1 + '?')
    bot.send_message(message.chat.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, "Приятно познакомиться! Теперь запишу в БД!")
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, "Попробуем еще раз!")
        bot.send_message(call.message.chat.id, 'Давай познакомимся!\nКак тебя зовут?')  # message.from_user.id
        bot.register_next_step_handler(call.message, reg_name)


bot.polling()
