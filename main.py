import telebot

import apikey as apikey
import currencies as currencies
import datetime, pytz, requests

bot = telebot.TeleBot(apikey.API_KEY, parse_mode=None)

@bot.message_handler(commands=['start', 'iniciar'])
def starting_message(message):
    bot.reply_to(
        message, 
        "Este é o Cotação Bot. Você pode utilizar as seguintes funções:\n" + 
        "/ajuda\n" +
        "/sobre\n" +
        "/agora\n" +
        "/cotacao\n"
    )

@bot.message_handler(commands=['ajuda'])
def helping_message(message):
    bot.reply_to(
        message,
        "Manual de Uso BOT COTAÇÃO:\n" +
        "Opção /iniciar ou /start – exibe o menu inicial para o usuário\n" +
        "Opção /ajuda – mostra essa mensagem.\n" +
        "Opção /sobre – informação sobre o bot e o que ele está fazendo no momento.\n" +
        "Opção /agora – informa o horário e a data de acordo com \n" +
        "Opção /cotacao – informa a cotação entre duas moedas da escolha do usuário."
    )

@bot.message_handler(commands=['sobre'])
def informing_message(message):
    bot.reply_to(
        message,
        "BOT Cotação INF032:\n" +
        "Este bot é feito como um trabalho universitário e como um meio de estudo da linguagem de programação Python. Seu objetivo é servir como um centro de informação financeira de forma interativa e conveniente.\n" +
        "\nNo momento presente este bot apenas informa o câmbio."
    )

@bot.message_handler(commands=['agora'])
def timenow_message(message):

    agora = datetime.datetime.now(pytz.timezone('America/Bahia'))
    bot.reply_to(
        message,
        agora.strftime(
            "Baseado em Salvador, Bahia, Brasil\n" +
            "Hora certa: %H:%M\n" +
            "Data: %d/%m/%y"
        )
    )

print('starting bot...')
bot.polling()