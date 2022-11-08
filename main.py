import telebot
from telebot import types

bot = telebot.TeleBot('5735245682:AAEO_28-cGEsbNwA1-d1-V1wmI_tEgV1ui4')

#greeting
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    yes = types.KeyboardButton('Расскажи')
    no = types.KeyboardButton('Нет, уже знаю')
    markup.add(yes, no)
    mess = f'<b>Привет, {message.from_user.first_name}!</b> Я помогу тебе пообщаться с подсознанием. Хочешь узнать как?'
    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')


#manual
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Нет, уже знаю":
        bot.send_message(message.chat.id, "Тогда начнем! Выбери интересующую тебя тему:")
    elif message.text == "Расскажи":
        bot.send_message(message.chat.id, "Я буду задавать тебе вопросы и показывать картинки. Подробно рассмотри ее "
                                      "и подумай как она сотносится с вопросом. Напиши первое что приходит в голову. "
                                      "Помни, нет правильных или неправильных ответов. Не думай больше 30 секунд. "
                                      "Приступим?")

@bot.message_handler()
def send_text(message):
    print(message.text)
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, 'Привет, неизвестный!')
    elif message.text.lower() == 'photo':
        bot.send_photo(message.chat.id, open('03.jpg', 'rb'))


bot.polling(none_stop=True)