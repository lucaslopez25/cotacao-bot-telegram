import constants as constants
import apikey as apikey
from telegram.ext import * 
import answers as answers

print ("STARTING BOT...")

def start_command(update, context):
    update.message.reply_text('Digite algo para começar!')

def helpme_command(update, context):
    update.message.reply_text('')

def info_command(update, context):
    update.message.reply_text("BOT Cotação INF032:\n" + 
    "Conversor de moedas e variação do valor em tempo real\n" +
    "Este bot é feito como um trabalho universitário e\n" + 
    "como um meio de estudo da linguagem de programação Python.\n" + 
    "Seu objetivo é informar os valores das moedas em relação ao Real\n" + 
    "e a outras moedas e as variações de valor de forma\n" + 
    "interativa e conveniente.")

def handle_message(update, context):
    texto = str(update.message.text).lower()
    resposta = answers.generic_answers(texto)

    update.message.reply_text(resposta)

def error(update, context):
    print(f"A seguinte mensagem {update} causou o seguinte erro:\n" +
    "{context.error}")

def main():
    updater = Updater(apikey.API_KEY, use_context=True)
    remetente = updater.dispatcher

    remetente.add_handler(CommandHandler("iniciar", start_command))
    remetente.add_handler(CommandHandler("ajuda", helpme_command))
    remetente.add_handler(CommandHandler("sobre", info_command))
    remetente.add_handler(MessageHandler(Filters.text, handle_message))
    remetente.add_error_handler(error)

    updater.start_polling()
    updater.idle()

print ("BOT STARTED")
main()



