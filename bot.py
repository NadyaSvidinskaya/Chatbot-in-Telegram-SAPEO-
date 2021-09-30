import telebot  # Импортируем библеотеку для Телеграма
from telebot import types  # Импортируем типы из модуля, чтобы создать кнопки в чат-боте
from config import token

# Создаём объект бота с импользование токена. Токен получаем через чат-бот в Телеграме BotFather
bot = telebot.TeleBot(token)

# Название кнопок и их содержимое
rcpeo = 'На сайте Республиканского ресурсного центра САПЭО https://rcpeo.bspu.by/ вы можете ознакомиться с предстоящими мероприятиями, а так же просмотреть информацию и '\
        'материалы по уже прошедшим онлайн-мероприятиям, консультациям и конференциям'
timetable = 'Вы можете ознакомиться с расписанием консультаций на текущий месяц по ссылке - https://rcpeo.bspu.by/wp-content/uploads/2021/09/sentyabr-2021-a.pdf'
announcement = 'Анонс предстоящих мероприятий, в которых вы можете принять участия как в качестве докладчика, так и в качестве слушателя https://rcpeo.bspu.by/anons-meropriyatij/'
contacts = 'Вы можете связаться с нами по телефону:8 (017) 311 23 99, ' \
           'внутренний тел.: 171,' \
           'или можете написать нам на e-mail: eo@bspu.by'
schedule = 'График работы:' \
           'понедельник-четверг: 8:30-12:30, 13:15-17:30,' \
           'пятница: 8:30-12:30, 13:15-16:15'

# Декоратор для обработки сообщений
@bot.message_handler(content_types=['text'])
# Метод для обработки сообщений
def get_text_message(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Добрый день! '
                                      'Вы попали в чат-бот Республиканского ресурсного центра "Сетевая академия педагогики электронного обучения."')

# Создание кнопок
        keyboard = types.InlineKeyboardMarkup()
        key_rcpeo = types.InlineKeyboardButton(text='Сайт САПЭО', callback_data='rcpeo')
        keyboard.add(key_rcpeo)   # Добавление кнопки на экран
        key_timetable = types.InlineKeyboardButton(text='Расписание консультаций', callback_data='timetable')
        keyboard.add(key_timetable)
        key_announcement = types.InlineKeyboardButton(text='Анонс мероприятий', callback_data='announcement')
        keyboard.add(key_announcement)
        key_contacts = types.InlineKeyboardButton(text='Контакты', callback_data='contacts')
        keyboard.add(key_contacts)
        key_schedule = types.InlineKeyboardButton(text='График работы', callback_data='schedule')
        keyboard.add(key_schedule)

# Выводим все кнопки на экран и оставляем сообщение
        bot.send_message(message.from_user.id, text='Выберите интересующую вас информацию', reply_markup=keyboard)




    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напишите, пожалуйста, Привет, чтобы продолжить.')
    else:
        bot.send_message(message.from_user.id, 'Извините, я Вас не понимаю, напишите, пожалуйста, /help, чтобы продолжить. Спасибо.')

# Декоратор для работы кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'rcpeo':
        bot.send_message(call.message.chat.id, rcpeo)
    elif call.data == 'timetable':
        bot.send_message(call.message.chat.id, timetable)
    elif call.data == 'announcement':
        bot.send_message(call.message.chat.id, announcement)
    elif call.data == 'contacts':
        bot.send_message(call.message.chat.id, contacts)
    elif call.data == 'schedule':
        bot.send_message(call.message.chat.id, schedule)

# Запуск чат-бота
bot.polling(none_stop=True, interval=0)




