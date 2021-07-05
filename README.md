# cotacao-bot-telegram
* PORTUGUESE (PT-BR) BOT

Bot simples que mostra taxa de câmbio e hora (com base na timezone 'America/Bahia')

Bibliotecas usadas:

- pyTelegramBotAPI (3.8.1)
- requests (2.25.1)
- pytz (2021.1)

Lembre-se que o token está registrado em 'apikey.py', este importado como 'apikey' para o código. O arquivo não está incluido no repositório. Se tentar rodar este bot na sua máquina, lembre-se de criar apikey.py como um arquivo e registrar o token lá dentro. Também não se esqueça de colocar 'apikey.py' dentro do .gitignore se estiver trabalhando em um repositório Git para não dar commit no arquivo, visto que ele possui seu token do Telegram.


Você pode testar o bot em @inf032_cotacao_bot (em execução no PythonAnywhere).

Instalando na sua máquina:

escolha a pasta de preferência

> git clone https://github.com/lucaslopez25/cotacao-bot-telegram

tenha ao menos o pip instalado (para testar basta executar 'pip --version')
faça:

> pip install virtualenv
> virtualenv botenv

Se seu sistema for Windows (funciona tanto no PowerShell quanto no CMD)

> botenv\Scripts\activate

Mas se o seu for Unix...

> source botenv/bin/activate

Agora crie o arquivo apikey.py usando (se o seu sistema for Unix, mas se for Windows, faça via interface gráfica, botão esquerdo > novo > arquivo de texto, renomear para apikey.py)

> touch apikey.py

escreva dentro do arquivo o seguinte

> API_KEY = 'TOKEN'

* onde TOKEN é o token secreto dado pelo BotFather (https://t.me/botfather) quando você cria um novo bot. Para mais informações, leia a documentação https://core.telegram.org/bots

faça:

> pip install -r requirements.txt
> python main.py

Seu bot está pronto para uso e operando normalmente.

OBRIGADO GALERA DO https://github.com/eternnoir/pyTelegramBotAPI só alegria!!!!

* ENGLISH DESCRIPTION

Simple bot that can show currency exchange rates and time (based on tz 'America/Bahia')

Libraries:
- pyTelegramBotAPI (3.8.1)
- requests (2.25.1)
- pytz (2021.1)

Please note that the Api Key is registered on 'apikey.py', imported as 'apikey', which is not included on the repository.
If you try this bot at home remember to create apikey.py as a separate file and put the token in there. Remember to put it
on .gitignore if you are working in a git repo in order to not commit the file.

You can test it at @inf032_cotacao_bot (running on Python Anywhere).

Installing at home:

choose folder of preference

> git clone https://github.com/lucaslopez25/cotacao-bot-telegram

have at least pip installed

> pip install virtualenv
> virtualenv botenv

if in windows (works either in PowerShell or in CMD)

> botenv\Scripts\activate

if in unix based system

> source botenv/bin/activate

create archive apikey.py using

>touch apikey.py

inside the archive you should write

>API_KEY = 'TOKEN'

* TOKEN is the token given by BotFather (https://t.me/botfather) when you create a new bot. Please refer to https://core.telegram.org/bots for more details

do:

>pip install -r requirements.txt
>python main.py

Enter in contact with your bot on Telegram and see it in action. The API_KEY may be reutilized for other bots.
