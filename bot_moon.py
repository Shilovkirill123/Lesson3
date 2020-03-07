from telegram.ext import Updater , CommandHandler , MessageHandler, Filters 
import ephem
from datetime import datetime, date, timedelta

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater("958204140:AAHA21y19NDgyyzTYNJH4WsqQ9mfvY1X-3c", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("next_full_moon", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):

    user_text = update.message.text
    user_text=user_text.split()
    user_text=user_text[1]
    print(user_text)
    a=ephem.next_full_moon(user_text)
    print(a)
    
    update.message.reply_text(f'Ближайшее полнолуние будет: {a}')
    




def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

main()