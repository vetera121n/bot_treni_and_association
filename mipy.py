import telebot

bot = telebot.TeleBot('5795143339:AAH0X_gwJx8PSRTxo4pas_Xq-EY5UKe-E2Y')

# Команды
@bot.message_handler(commands=['start']) # Принимает команду /start и отвечает
def start(message):
    mess = f'ёу чё каво!? <b>{message.from_user.first_name} , <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['help']) # Принимает команду /help
def help(message):
    mess = f'<b> Не чувак, давай сам! </b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['message']) # Принимает команду ...
def help(message):
    bot.send_message(message.chat.id, message, parse_mode='html')

# Сообщения
@bot.message_handler(content_types=['text']) # Принимает Текст и отвечает
def get_user_text(message):
    if message.text.lower() == 'my id' or message.text.lower() == 'мой id':
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, твой ID: {message.from_user.id}', parse_mode='html')
    elif message.text == 'photo':
        photo = open('img\кот_программист.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else: # Если не известный запрос
        bot.send_message(message.chat.id, 'Не понятен мне твой запрос', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Воуу!! что за фото!?')

bot.polling(none_stop=True) # Отвечает за беспрерывную работу бота(пока запущена программа)