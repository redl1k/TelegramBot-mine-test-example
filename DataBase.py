import telebot
import sqlite3

#bot
bot = telebot.TeleBot("Ur bot Token") #1 bot osnova
#bot = telebot.TeleBot("Ur bot Token") #2 bot Test

@bot.message_handler(commands=['start'])
def start(message):
    #connect DB and create table
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id( 
        id INTEGER 
    )""")

    connect.commit()

    #Проверка на существование в бд этого айди
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        #Добавление значения в поля
        used_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", used_id)
        connect.commit()
    else:
        bot.send_message(message.chat.id, 'Такой пользователь уже существует')


@bot.message_handler(commands=['delete'])
def delete(message):
    # connect DB
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    #delete id from table
    people_id = message.chat.id
    cursor.execute(f"DELETE FROM login_id WHERE id = {people_id}")
    connect.commit()






#polling
bot.polling()
