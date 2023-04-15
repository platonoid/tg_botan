from flask import Flask, request
import os
from dotenv import load_dotenv
from telegram.ext import CommandHandler, MessageHandler, filters, Application, CallbackContext, ContextTypes
import logging
import telegram
from telegram import Update
import requests


response = requests.get('https://eu.api.riotgames.com/val/ranked/v1/leaderboards/by-act/34093c29-4306-43de-452f-3f944bde22be?size=21&startIndex=0&api_key=RGAPI-d1d78cdc-c814-40c2-bc36-485fbbdeacab')
response2 = requests.get('https://eu.api.riotgames.com/val/content/v1/contents?locale=ru-RU&api_key=RGAPI-d1d78cdc-c814-40c2-bc36-485fbbdeacab')

version = response2.json()
v = version["version"]
lol = response.json()
val = []
load_dotenv()
app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

addon = Application.builder().token('6084013080:AAGX8y5i-XAv514ZvUU5PzC45A8iZorLVW0').build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a Chamber, please talk to me!")


async def totalplayers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    total = response.json()
    players = total["totalPlayers"]
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Hi, let me think, now we have {players} players')


async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    board1 = []
    board2 = []
    leaders = response.json()
    player = leaders["players"]
    for i in range(len(player)):
        board1.append(player[i]["rankedRating"])
    for i in range(len(player)):
        board2.append(player[i]["numberOfWins"])
    for i in range(len(player)):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Интернет не анонимен {i + 1} : {board1[i]} - {board2[i]}')


async def characters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    board = []
    character = response2.json()
    ch = character["characters"]
    for i in range(len(ch) - 1):
         board.append(ch[i]["name"])
    name_of_character = ', '.join(board)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список персонажей на момент {v}: {name_of_character}')


async def maps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sp = []
    mapa = response2.json()
    map_pool = mapa["maps"]
    for i in range(1, len(map_pool)):
        sp.append(map_pool[i]["name"])
    name_of_maps = ', '.join(sp)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список карт на момент {v}: {name_of_maps}')


def reply(update, context):
    try:
        text = update.message.text
        context.bot.send_message(chat_id=update.message.chat_id, text=text)
    except Exception as e:
        context.bot.send_message(chat_id=update.message.chat_id, text='Ошибка: ' + str(e))


addon.add_handler(CommandHandler('start', start))


@app.route('/', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), addon.bot)
    addon.process_update(update)
    return 'ok'


if __name__ == '__main__':
    addon = Application.builder().token("6084013080:AAGX8y5i-XAv514ZvUU5PzC45A8iZorLVW0").build()
    addon.add_handler(CommandHandler('reply', reply))
    addon.add_handler(CommandHandler('start', start))
    addon.add_handler(CommandHandler('totalplayers', totalplayers))
    addon.add_handler(CommandHandler('leaderboard', leaderboard))
    addon.add_handler(CommandHandler('name_of_characters', characters))
    addon.add_handler(CommandHandler('map_pool', maps))
    addon.run_polling()
