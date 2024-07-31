import telebot
import tempfile
import json
from PIL  import ImageGrab 
import os
import psutil
import webbrowser
import pyautogui
import subprocess
import time
import threading

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    API_TOKEN = config['API_TOKEN']
    ALLOWED_USERS = config['ALLOWED_USERS']
    PROGRAM_PATHS = config['PROGRAM_PATHS']

bot = telebot.TeleBot(API_TOKEN)

def send_uptime(message):
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_string = format_uptime(uptime_seconds)
    bot.send_message(message.chat.id, f'🕒 Время работы ПК: {uptime_string}')

def format_uptime(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f'{int(days)} дней, {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд'