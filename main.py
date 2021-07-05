import telebot
from telebot import types

import apikey as apikey
import currencies as currencies
import datetime, pytz, requests
import currency as currency
import requests

bot = telebot.TeleBot(apikey.API_KEY, parse_mode=None)

passo = 0
is_cotacao_on = False
current_currency = currency.Currency()

def is_it_on_currencies(text):
    if any(text in item for item in currencies.CURRENCIES):
        return True
    else:
        return False

@bot.message_handler(commands=['start', 'iniciar'])
def starting_message(message):
    bot.send_message(
        message.chat.id, 
        "Este é o Cotação Bot. Você pode utilizar as seguintes funções:\n" + 
        "/ajuda\n" +
        "/sobre\n" +
        "/agora\n" +
        "/cotacao\n"
    )

@bot.message_handler(commands=['ajuda'])
def helping_message(message):
    bot.send_message(
        message.chat.id,
        "Manual de Uso BOT COTAÇÃO:\n" +
        "Opção /iniciar ou /start – exibe o menu inicial para o usuário\n" +
        "Opção /ajuda – mostra essa mensagem.\n" +
        "Opção /sobre – informação sobre o bot e o que ele está fazendo no momento.\n" +
        "Opção /agora – informa o horário e a data de acordo com \n" +
        "Opção /cambio – informa a cotação entre duas moedas da escolha do usuário."
    )

@bot.message_handler(commands=['sobre'])
def informing_message(message):
    bot.send_message(
        message.chat.id,
        "BOT Cotação INF032:\n" +
        "Este bot é feito como um trabalho universitário e como um meio de estudo da linguagem de programação Python. Seu objetivo é servir como um centro de informação financeira de forma interativa e conveniente.\n" +
        "\nNo momento presente este bot apenas informa o câmbio."
    )

@bot.message_handler(commands=['agora'])
def timenow_message(message):

    agora = datetime.datetime.now(pytz.timezone('America/Bahia'))
    bot.send_message(
        message.chat.id,
        agora.strftime(
            "Baseado em Salvador, Bahia, Brasil\n" +
            "Hora certa: %H:%M\n" +
            "Data: %d/%m/%y"
        )
    )

@bot.message_handler(commands=['cambio'])
def currency_converting_message(message):
    global is_cotacao_on
    bot.send_message(
        message.chat.id,
        "Ótimo, vamos começar."
    )
    teclado = types.ReplyKeyboardMarkup(row_width=1)
    for item in currencies.CURRENCIES:
        moeda = item[0]
        button = types.KeyboardButton(moeda)
        teclado.add(button)
    bot.send_message(
        message.chat.id,
        "Escolha uma moeda:",
        reply_markup=teclado
    )
    is_cotacao_on = True
    
@bot.message_handler(func=lambda message: True)
def generic_message_handler(message):
    global passo
    global current_currency
    global is_cotacao_on
    if is_cotacao_on == True and passo == 0:
        for item in currencies.CURRENCIES:
            if message.text in item[0]:
                current_currency.set_first_currency(item[1])
    
        teclado = types.ReplyKeyboardMarkup(row_width=1)
        for item in currencies.CURRENCIES:
            moeda = item[0]
            button = types.KeyboardButton(moeda)
            teclado.add(button)
        bot.send_message(
            message.chat.id,
            "Diga-me a moeda a qual deseja saber o valor:",
            reply_markup=teclado
            )
        passo = passo + 1
    elif is_cotacao_on == True and passo == 1:
        for item in currencies.CURRENCIES:
            if message.text in item[0]:
                current_currency.set_second_currency(item[1])
        request = requests.get(current_currency.get_url())
        dados = request.json()
        bot.send_message(
            message.chat.id,
            "Sucesso! A cotação atual do {} em relação ao {} é:\n".format(current_currency.get_long_name(current_currency.first_currency), current_currency.get_long_name(current_currency.second_currency)) +
            "{} {} compram {} 1.0000 no valor máximo\n".format(
                current_currency.second_currency, 
                dados[current_currency.first_currency + current_currency.second_currency]["high"],
                current_currency.first_currency) +
            "{} {} compram {} 1.0000 no valor mínimo\n".format(
                current_currency.second_currency, 
                dados[current_currency.first_currency + current_currency.second_currency]["low"],
                current_currency.first_currency)
        )
        passo = 0
        is_cotacao_on = False
        current_currency.reset()
        starting_message(message)
    else:
        bot.send_message(
            message.chat.id,
            "Desculpe-me, não entendi."
        )

print('starting bot...')
bot.polling()