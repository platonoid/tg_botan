from flask import Flask, request
import os
from dotenv import load_dotenv
from telegram.ext import CommandHandler, MessageHandler, filters, Application, CallbackContext, ContextTypes
import logging
import telegram
from telegram import Update
import requests


response = requests.get('')
response2 = requests.get('')

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
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'''Привет, меня зовут Chamber, если ты еще совсем\
                                                                          чайник в игре, то я тебе дам информацию\
                                                                          которая может быть поможете тебе в будущем
                                                                          Что я умею:
                                                                          -/totalplayers: Я пишу количество игроков, играющих в Valorant
                                                                          -/leaderboard: Я пишу тебе список игроков, их место, их рейтинг,\
                                                                          а также кол-во их побед
                                                                          -/name_of_characters: пишу список персонажей на текущей версии игры
                                                                          -/map_pool: Пишу названия карт на текущей версии игры
                                                                          -/(название оружия): Отправляю все скины на оружие на момент {v}-
                                                                          Вот Список: classic, shorty, ghost, frenzy, sheriff,
                                                                          stinger, spectre, bucky, judge, bulldog, guardian, vandal,
                                                                          phantom, marshal, operator, ares, odin
                                                                          ''')

    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chamba.jpg')


async def totalplayers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    total = response.json()
    players = total["totalPlayers"]
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Привет, вот список игроков, с которыми ты точно сольешь рейтинг{players}')


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
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Игрок который никогда не докасался до женщин:{i + 1} - номер в таблице лидеров, {board1[i]} - рейтинг {board2[i]} - победы')


async def characters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    board = []
    character = response2.json()
    ch = character["characters"]
    for i in range(len(ch) - 1):
         board.append(ch[i]["name"])
    name_of_character = ', '.join(board)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список персонажей на момент {v}: {name_of_character}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/breach.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/brimsone.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/chamber.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/cypher.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/fade.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/gekko.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/harbor.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/jett.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/kayo.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/kj.png')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/neon.png')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/omen.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/phoenix.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/raze.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/reyna.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/sage.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/skye.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/viper.png')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/yoru.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/sova.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/astra.jpg')


async def maps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sp = []
    mapa = response2.json()
    map_pool = mapa["maps"]
    for i in range(1, len(map_pool)):
        sp.append(map_pool[i]["name"])
    name_of_maps = ', '.join(sp)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список карт на момент {v}: {name_of_maps}')


async def odin(update: Update, context: ContextTypes.DEFAULT_TYPE):     #1
    pulemet = []
    city = response2.json()
    big = city["chromas"]
    for i in range(1, len(big)):
        b = ''
        if 'Odin ' in big[i]["name"]:
            b = big[i]["name"]
            pulemet.append(b)
    ok = ', '.join(pulemet)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Odin на момент {v}: {ok}')


async def vandal(update: Update, context: ContextTypes.DEFAULT_TYPE):   #2
    vanal = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Vandal ' in paf[i]["name"]:
            b = paf[i]["name"]
            vanal.append(b)
    ok = ', '.join(vanal)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Vandal на момент {v}: {ok}')


async def phantom(update: Update, context: ContextTypes.DEFAULT_TYPE):      #3
    phantm = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Phantom ' in paf[i]["name"]:
            b = paf[i]["name"]
            phantm.append(b)
    ok = ', '.join(phantm[:54])
    ok1 = ', '.join(phantm[55:])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Phantom на момент {v}: {ok}')
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f'Список скинов на Phantom на момент {v}: {ok1}')


async def classic(update: Update, context: ContextTypes.DEFAULT_TYPE):      #4
    classic = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Classic ' in paf[i]["name"]:
            b = paf[i]["name"]
            classic.append(b)
    ok = ', '.join(classic)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Classic на момент {v}: {ok}')


async def sheriff(update: Update, context: ContextTypes.DEFAULT_TYPE):      #5
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Sheriff ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Sheriff на момент {v}: {ok}')


async def ghost(update: Update, context: ContextTypes.DEFAULT_TYPE):        #6
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Ghost ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Ghost на момент {v}: {ok}')


async def ares(update: Update, context: ContextTypes.DEFAULT_TYPE):     #7
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Ares ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Ares на момент {v}: {ok}')


async def shorty(update: Update, context: ContextTypes.DEFAULT_TYPE):       #8
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Shorty ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Shorty на момент {v}: {ok}')


async def frenzy(update: Update, context: ContextTypes.DEFAULT_TYPE):       #9
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Frenzy ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Frenzy на момент {v}: {ok}')


async def bucky(update: Update, context: ContextTypes.DEFAULT_TYPE):        #10
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Bucky ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Bucky на момент {v}: {ok}')


async def judge(update: Update, context: ContextTypes.DEFAULT_TYPE):        #11
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Judge ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Judge на момент {v}: {ok}')


async def bulldog(update: Update, context: ContextTypes.DEFAULT_TYPE):      #12
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Bulldog ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Bulldog на момент {v}: {ok}')


async def operator(update: Update, context: ContextTypes.DEFAULT_TYPE):     #13
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Operator ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Ну все задолбали покупаю Operator в {v}: {ok}')


async def guardian(update: Update, context: ContextTypes.DEFAULT_TYPE):     #14
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Guardian ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Guardian на момент {v}: {ok}')


async def marshal(update: Update, context: ContextTypes.DEFAULT_TYPE):      #15
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Marshal ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Marshal на момент {v}: {ok}')


async def spectre(update: Update, context: ContextTypes.DEFAULT_TYPE):      #16
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Spectre ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Spectre на момент {v}: {ok}')


async def stinger(update: Update, context: ContextTypes.DEFAULT_TYPE):      #17
    count = []
    puh = response2.json()
    paf = puh["chromas"]
    for i in range(1, len(paf)):
        b = ''
        if 'Stinger ' in paf[i]["name"]:
            b = paf[i]["name"]
            count.append(b)
    ok = ', '.join(count)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Список скинов на Stinger на момент {v}: {ok}')


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
    addon.add_handler(CommandHandler('Odin', odin))
    addon.add_handler(CommandHandler('Operator', operator))
    addon.add_handler(CommandHandler('Spectre', spectre))
    addon.add_handler(CommandHandler('Stinger', stinger))
    addon.add_handler(CommandHandler('Frenzy', frenzy))
    addon.add_handler(CommandHandler('Bucky', bucky))
    addon.add_handler(CommandHandler('Judge', judge))
    addon.add_handler(CommandHandler('Marshal', marshal))
    addon.add_handler(CommandHandler('Ares', ares))
    addon.add_handler(CommandHandler('Vandal', vandal))
    addon.add_handler(CommandHandler('Ghost', ghost))
    addon.add_handler(CommandHandler('Guardian', guardian))
    addon.add_handler(CommandHandler('Bulldog', bulldog))
    addon.add_handler(CommandHandler('Classic', classic))
    addon.add_handler(CommandHandler('Shorty', shorty))
    addon.add_handler(CommandHandler('Phantom', phantom))
    addon.add_handler(CommandHandler('Sheriff', sheriff))
    addon.add_handler(CommandHandler('totalplayers', totalplayers))
    addon.add_handler(CommandHandler('leaderboard', leaderboard))
    addon.add_handler(CommandHandler('name_of_characters', characters))
    addon.add_handler(CommandHandler('map_pool', maps))
    addon.run_polling()
