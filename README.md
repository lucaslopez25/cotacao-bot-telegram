# cotacao-bot-telegram
* PORTUGUESE (PT-BR) BOT

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
