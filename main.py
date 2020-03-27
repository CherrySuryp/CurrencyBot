import telebot
from telebot import types
import requests
import currency  # Currency parser

bot_token = open("BOT_ACCESS").read()
bot = telebot.TeleBot(bot_token)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
EUR = types.KeyboardButton("EUR💶")
USD = types.KeyboardButton("USD💵")
CZK = types.KeyboardButton("CZK")
own = types.KeyboardButton("Другое")
markup.add(EUR, USD, CZK, own)


@bot.message_handler(commands=['start'])
def sendMessage(message):
    if message.chat.id == 295794680:
        bot.send_message(message.chat.id, "Здравствуй, создатель")
    else:
        bot.send_message(message.chat.id, "Привет, <b>{0.first_name}</b>!".format(message.from_user, bot.get_me),
                         parse_mode='html')
    bot.send_message(message.chat.id, "Я могу прислать тебе актуальный курс валют!", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text == "EUR💶":
        bot.send_message(message.chat.id, currency.EUR(), reply_markup=markup)
    elif message.text == "USD💵":
        bot.send_message(message.chat.id, currency.USD(), reply_markup=markup)
    elif message.text == "CZK":
        bot.send_message(message.chat.id, currency.CZK(), reply_markup=markup)
    elif message.text == "Другое":
        msg = bot.send_message(message.chat.id,
                               "Окей! Введите нужную вам котировку\nПример: <b>EUR</b>, <b>USD</b>, <b>RUB</b>",
                               parse_mode='html', reply_markup=)
        bot.register_next_step_handler(msg, own)


def own(message):
    text = message.text
    """CURRENCY CHOICE"""
    url = 'https://api.exchangeratesapi.io/latest?base=' + text
    values = dict(eval(requests.get(url).text))
    if str(values.keys()) == "dict_keys(['error'])":
        bot.send_message(message.chat.id, str(
            "<b>Упс...</b>\n"
            "Кажется такой котировки не существует или же мое API ее не поддерживает\n"
            "Проверьте правильность введенных данных"),
                         parse_mode='html',
                         reply_markup=markup)
    else:
        cur = values['rates']
        bot.send_message(message.chat.id, str("Курс " + text + " равен " + str(round(cur["RUB"], 2)) + " рубля"),
                         reply_markup=markup)
    print("hello")



bot.polling(none_stop=True)
