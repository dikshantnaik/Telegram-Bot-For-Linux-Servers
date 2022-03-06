import telepot as tp
from telepot.loop import MessageLoop
import time
import os
from dotenv import load_dotenv
from view import *

load_dotenv()
# ADD YOUR TELEGRAM BOT TOKEN HERE 
TOKEN = os.getenv("TOKEN")
print(TOKEN)
def handle(data):
    content_type, chat_type, chat_id = tp.glance(data)
    print(chat_id)
    msg = data['text']
    if content_type == 'text':
        if msg == "ping" or msg=="Ping":
            print("Ping recived")
            bot.sendMessage(chat_id,PingPC())
        elif "meet.google.com" in msg:
            bot.sendMessage(chat_id,"Joining in 10 Sec")
            joinMeet(msg)
        elif "play" in msg or "Play" in msg:
            play_what = msg[5:]
            bot.sendMessage(chat_id,"Playing "+play_what)
            PlayMusic(play_what)
        elif "logout" in msg or "Logout" in msg:
            bot.sendMessage(chat_id,"Loging offf")
            Logout()

        elif "shutdown" in msg or "Shutdown" in msg:
            bot.sendMessage(chat_id,"Shuding Down..Bye Bye ")
            os.system("shutdown now")

        elif "open" in msg or "Open" in msg:
            if msg[5:] == "code":
                os.system("code")
                bot.sendMessage(chat_id,"Opening")
        elif "suspend" in msg or "suspend" in msg or "sleep" in msg or "Sleep" in msg:
            os.system("systemctl suspend")
            bot.sendMessage(chat_id,"Slepping")
        elif "battery" in msg or "Battery" in msg:
             bot.sendMessage(chat_id,Battery())
            
        else:
            bot.sendMessage(chat_id,"Hey There Get Started ")


bot = tp.Bot(TOKEN)
print ('Listening ...')
MessageLoop(bot, handle).run_as_thread()
# Sends a default message to my number When the Script is AutoStartes
bot.sendMessage(711549194,"Hey Dikshant,Your Pc has been Started ")


while 1:
    # RUN FOR ETERNITY..hehe
    time.sleep(10)