
import sqlite3
import telebot

from telebot import types

bot = telebot.TeleBot('6985479517:AAFFGyf05rSMfCaVazex3ldGAmivND4APiM')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет!!! Мой создатель Kuftinov-Studios", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Расписание')
        btn2 = types.KeyboardButton('Текст 2')
        btn3 = types.KeyboardButton('Текст 3')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Выбери один из текстов', reply_markup=markup)


    elif message.text == 'Расписание':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Понедельник')
        btn2 = types.KeyboardButton('Вторник')
        btn3 = types.KeyboardButton('Среда')
        btn4 = types.KeyboardButton('Четверг')
        btn5 = types.KeyboardButton('Пятница')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, 'Выберите день недели', reply_markup=markup)

    elif message.text == 'Понедельник':
        bot.send_message(message.from_user.id, 'Алгебра', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Русский язык', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Русский язык', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Физика', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Физика', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'История', parse_mode='Markdown')


    elif message.text == 'Вторник':
        bot.send_message(message.from_user.id, 'Геометрия', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Алгебра', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Литература', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Физкультура', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'ОБЖ', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Обществознание', parse_mode='Markdown')

    elif message.text == 'Среда':
        bot.send_message(message.from_user.id, 'Алгебра', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'История', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Русский язык', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Физика', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Химия', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Химия', parse_mode='Markdown')
    elif message.text == 'Четверг':
        bot.send_message(message.from_user.id, 'Геометрия', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Теория вероянтности', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Инжинерный практикум', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Физика', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Обществознание', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Информатика', parse_mode='Markdown')
    elif message.text == 'Пятница':
        bot.send_message(message.from_user.id, 'Биология', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Литература', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Алгебра', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Информатика', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Информатика', parse_mode='Markdown')
        bot.send_message(message.from_user.id, 'Проектная деятельность', parse_mode='Markdown')




bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть