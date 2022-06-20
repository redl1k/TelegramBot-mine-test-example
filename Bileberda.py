async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="С пюрешкой")
    keyboard.add(button_1)
    button_2 = "Без пюрешки"
    keyboard.add(button_2)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

    @dp.message_handler(commands="start")
    def cmd_start(message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Привет"]
        keyboard.add(*buttons)

        @bot.message_handler(commands="start")
        async def cmd_start(message: types.Message):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ["С пюрешкой", "Без пюрешки"]
            keyboard.add(*buttons)
            await message.answer("Как подавать котлеты?", reply_markup=keyboard)

            @bot.message_handler(commands="start")
            def cmd_start(message):
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                buttons = ["Привет"]
                keyboard.add(*buttons)
                bot.reply_to(message, "Привет бро!\nНапиши /reg, чтобы зарегистрироваться:)")

                @dp.message_handler(commands="start")
                async def cmd_start(message: types.Message):
                    keyboard = types.ReplyKeyboardMarkup()
                    button_1 = types.KeyboardButton(text="С пюрешкой")
                    keyboard.add(button_1)
                    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

                    @bot.message_handler(commands="start")
                    def echo_all(message):
                        keyboard = types.ReplyKeyboardMarkup()
                        button_1 = types.KeyboardButton(text="Привет")
                        keyboard.add(button_1)
                        bot.reply_to(message, "Привет бро!\nНапиши /reg, чтобы зарегистрироваться:)",
                                     reply_markup=types.ReplyKeyboardRemove())

                        @bot.message_handler(content_types=['text'])
                        def handler(message):
                            if message.text == " Привет":
                                bot.send_message(message.chat.id, "Привет!")
                            if message.text == " Как дела?":
                                bot.send_message(message.chat.id, "Отлично!")

                                @bot.message_handler(content_types=['text'])
                                keyboard = types.InlineKeyboardMarkup()
                                key_1 = types.InlineKeyboardButton(text='Привет', callback_data='priv')
                                keyboard.add(key_1)
                                bot.send_message(message.from_user.id, text='Привет',reply_markup=keyboard)

                                @bot.message_handler(content_types=['text'])
                                def inline_key(a):
                                    if a.text == "Меню":
                                        mainmenu = types.InlineKeyboardMarkup()
                                        key1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='key1')
                                        key2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='key2')
                                        mainmenu.add(key1, key2)
                                        bot.send_message(a.chat.id, 'Это главное меню!', reply_markup=mainmenu)

                                @bot.callback_query_handler(func=lambda call: True)
                                def callback_inline(call):
                                    if call.data == "mainmenu":
                                        mainmenu = types.InlineKeyboardMarkup()
                                        key1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='key1')
                                        key2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='key2')
                                        mainmenu.add(key1, key2)
                                        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id,
                                                                      reply_markup=mainmenu)
                                    elif call.data == "key1":
                                        next_menu = types.InlineKeyboardMarkup()
                                        key3 = types.InlineKeyboardButton(text='Кнопка 3', callback_data='key3')
                                        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
                                        next_menu.add(key3, back)
                                        bot.edit_message_text('Это меню уровня 2, для кнопки1!', call.message.chat.id,
                                                              call.message.message_id,
                                                              reply_markup=next_menu)
                                    elif call.data == "key2":
                                        next_menu2 = types.InlineKeyboardMarkup()
                                        key4 = types.InlineKeyboardButton(text='Кнопка 4', callback_data='key4')
                                        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
                                        next_menu2.add(key4, back)
                                        bot.edit_message_text('Это меню уровня 2, для кнопки2!', call.message.chat.id,
                                                              call.message.message_id,
                                                              reply_markup=next_menu2)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'yess':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Чтобы наша клава маленькая была
        item_reg = types.KeyboardButton('/reg')
        markup_reply.add(item_reg)
        bot.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
                         reply_markup=markup_reply
                         )
    bot.answer_callback_query(callback_query_id=call.id)

    @bot.message_handler(commands=['dnevnik'])
    def dnevnik(message):
        if message.text == '/dnevnik':
            markup_inline = types.InlineKeyboardMarkup()
            item_ocenki = types.InlineKeyboardButton(text='Оценки', callback_data='ocenki')
            item_zadolj = types.InlineKeyboardButton(text='Задолженности', callback_data='zadolj')
            item_KT = types.InlineKeyboardButton(text='Ближайшие КТ', callback_data='KT')
            markup_inline.add(item_ocenki, item_zadolj, item_KT)
            bot.reply_to(message, "*Нажми на кнопку*\n"
                                  "И выбери что тебя интересует)",
                         reply_markup=markup_inline)










def reg_age(message):
	global age
	age = message.text
	while age == 0:
		try:
			age = int(message.txt)
		except Exception:
			bot.send_message(message.from_user.id, 'Введи цифрами!')

#	bot.send_message(message.from_user.id, 'Тебе'+srt(age)+'лет? И тебя зовут: '+name+' '+surname+' ?')
	keyboard = types.InlineKeyboardMarkup()
	key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
	keyboard.add(key_yes)
	key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
	keyboard.add(key_no)
	question='Тебе ' +str(age)+ ' лет?\nИ тебя зовут: '+name+' '+surname+' ?'
	bot.send_message(message.from_user.id, text = question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback_worker(call):
	if call.data == 'yes':
		bot.send_message(call.message.chat.id, "Приятно познакомиться! Теперь запишу в БД!" )
	elif call.data =='no':
		bot.send_message(call.message.chat.id, "Попробуем еще раз!")
		bot.send_message(call.message.chat.id, 'Давай познакомимся!\nКак тебя зовут?')#message.from_user.id
		bot.register_next_step_handler(call.message, reg_name)
