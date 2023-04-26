from flask import Flask, request
import os
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Application, ContextTypes
import logging
import telegram
from telegram import Update
import requests


response2 = requests.get('https://eu.api.riotgames.com/val/content/v1/contents?locale=ru-RU&api_key=RGAPI-7e56727b-9d24-4f9a-8911-bd56ab4a742e')
response = requests.get('https://eu.api.riotgames.com/val/ranked/v1/leaderboards/by-act/34093c29-4306-43de-452f-3f944bde22be?size=21&startIndex=0&api_key=RGAPI-7e56727b-9d24-4f9a-8911-bd56ab4a742e')

version = response2.json()
v = version["version"]
lol = response.json()
val = []
load_dotenv()
app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

addon = Application.builder().token('6084013080:AAGX8y5i-XAv514ZvUU5PzC45A8iZorLVW0').build()

astra = 'Астра (кодовое имя Звезда) — ганский агент-специалист из игры VALORANT.' \
        ' Astra является одной из лучших специалистов' \
        ' и подойдет любителям тактической игры. Несмотря на свою нестандартность,' \
        ' данный агент пригодится любой хорошо сплоченной команде. '
breach = 'Использующий бионические усиления швед Breach полагается на мощные направленные взрывы,' \
         ' чтобы расчистить путь от агентов противника.' \
         ' Разрушительная сила его умений позволяет получить решающее преимущество в любом бою.'
brimstone = 'Brimstone (кодовое имя Сержант) — американский агент-специалист из игры VALORANT,' \
            ' специализирующийся на поддержке союзников и нанесении урона врагам по всей карте. Brimstone уникален тем,' \
            ' что использует мини-карту для развертывания некоторых своих способностей, делая его опасным,' \
            ' даже если он не присутствует непосредственно в бою.'
chamber = 'Одет с иголочки и вооружен до зубов. Chamber, французский конструктор оружия,' \
          ' уничтожает врагов с поразительной точностью. ' \
          'Уникальные умения этого нового стража позволяют эффективно защищаться,' \
          ' нейтрализовать врагов издалека и продумывать любой план до мельчайших подробностей.'
cypher = 'Торговец информацией из Марокко Cypher может самостоятельно создать целую информационную ' \
         'сеть для отслеживания действий противника. Под неусыпным взором Cypher все тайное становится явным.'
fade = 'Турчанка Fade, охотница за головами, связала свою жизнь с Кошмаром' \
       ' и научилась читать врагов как открытые книги с помощью силы этого существа.' \
       ' Впустив в свое сердце кромешную тьму, она получила способность раскрывать чужие страхи и сводить жертву с ума.'
gekko = 'Gekko из Лос-Анджелеса заправляет дружной командой безбашенных существ. Его верные зверята смело бросаются' \
        ' в драку, разнося врагов в пух и прах. А когда Gekko подбирает питомцев с поля боя,' \
        ' можно перевести дух и повторить!'
harbor = 'Агент Harbor с индийского побережья обрушивает бурю на поле боя, используя древнюю ' \
         'технологию управления водой. Он повелевает бурлящими потоками и сокрушительными волнами,' \
         ' чтобы защитить союзников и разгромить противников.'
jett = 'Представляющая Южную Корею Jett быстра и неуловима и может позволить себе рисковать чаще других.' \
       ' В любой стычке она заходит с флангов и быстро уничтожает растерявшегося противника.'
kayo = 'KAY/O — боевая машина, созданная лишь для одной цели: истребить радиантов.' \
       ' Его способность подавлять умения врага существенно ослабляет команду противника ' \
       'и обеспечивает надежную защиту союзникам.'
kj = 'Гений из Германии. Killjoy легко защищает территорию на поле боя с помощью своего арсенала изобретений.' \
     ' Если противника не остановит урон от ее устройств,' \
     ' то наносимые ими эффекты ослабления помогут Killjoy легко с ним справиться.'
neon = 'Агент из Манилы с кодовым номером 19 может стать огромным помощником команде, чтобы та добилась успеха.' \
       ' Способности Neon позволяют ей расчищать любые позиции и открывать выход на точку быстрее,' \
       ' чем это сделает кто-либо другой. Благодаря эффекту неожиданности, ' \
       'эта филиппинка принесет огромный вклад в победу. '
omen = 'Призрак из прошлого Omen наносит удары из тени.' \
       ' Он способен ослеплять врагов и незаметно перемещаться по полю боя,' \
       ' вселяя страх в сердца противников, тщетно пытающихся предугадать, откуда он нападет вновь'
phoenix = 'Phoenix — дуэлянт с мощной огненной атакой. Поэтому он часто выступает агентом,' \
          ' который возглавляет главную атаку своей команды. Как и любой дуэлянт, Phoenix — боец,' \
          ' который наносит прямой урон в разгар схватки.'
raze = 'Raze — мастер взрывного дела из Бразилии, обладательница сильного характера и еще более мощных пушек.' \
       ' Она способна легко справиться с засевшими в обороне противниками или зачистить небольшое помещение.' \
       ' Громко и без лишних церемоний.'
reyna = 'Выросшая в самом сердце Мексики Reyna способна одолеть любого в бою один на один,' \
        ' и убийства придают ей сил. Ее мощь ограничена лишь мастерством и очень зависит от успехов в бою.'
sage = 'Защитница Китая Sage обеспечивает безопасность команды в бою.' \
       ' Благодаря возможности воскрешать союзников и сдерживать натиск ' \
       'врага она создает оазис покоя на жутком поле боя.'
skye = 'Австралийка Skye и ее звериная стая прокладывают путь по враждебной территории.' \
       ' Ее создания затрудняют продвижение врага, а сама Skye может лечить союзников.' \
       ' С ней команда будет в безопасности и станет сильнее, чем когда-либо.'
sova = 'Рожденный в вечной мерзлоте российского Заполярья,' \
       ' Sova выслеживает и уничтожает противников с холодной точностью и эффективностью.' \
       ' Этот первоклассный разведчик, экипированный особым луком, найдет вас, где бы вы ни прятались.'
viper = 'Химик из США Viper устанавливает контроль над полем боя с помощью источающих токсичный газ устройств' \
        ' и ограничивает обзор противникам. А тех, кого ей не удастся отравить, она непременно перехитрит.'
yoru = 'Уроженец Японии Yoru способен создавать разрывы в самой в реальности, чтобы незаметно пробираться на' \
       ' вражескую территорию. Сила и хитрость позволяют ему заставать врагов врасплох — они даже не успеют' \
       ' понять, откуда пришла смерть.'


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
                                                                          -/(название оружия): Отправляю все скины на оружие на момент {v}-\
                                                                          Вот Список: classic, shorty, ghost, frenzy, sheriff,\
                                                                          stinger, spectre, bucky, judge, bulldog, guardian, vandal,\
                                                                          phantom, marshal, operator, ares, odin
                                                                          -/(имя персонажа): Отправляю краткую биографию о персонаже\
                                                                          и фотографию самого персонажа(И конечно же лучшего игрока на нем)
                                                                          ''')

    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chamba.jpg')


async def totalplayers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    total = response.json()
    players = total["totalPlayers"]
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Привет, вот кол-во игроков с которыми ты сможешь слить рейтинг {players}')


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


async def astra1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{astra}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/astra.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/stas.jpg')


async def breach1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{breach}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/breach.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/ivan.jpg')


async def brimstone1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{brimstone}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/brimsone.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/serega.jpeg')


async def chamber1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{chamber}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/chamber.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/yura.jpg')


async def cypher1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{cypher}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/cypher.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/yura.jpg')


async def fade1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{fade}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/fade.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/ivan.jpg')


async def gekko1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{gekko}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/gekko.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/eminem.jpg')


async def harbor1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{harbor}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/harbor.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/platon.jpg')


async def jett1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{jett}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/jett.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/rlevenz.jpg')


async def kayo1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{kayo}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/kayo.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/buster.jpg')


async def kj1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{kj}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/kj.png')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/nottihon.jpg')


async def neon1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{neon}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/neon.png')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/platon.JPG')


async def omen1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{omen}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/omen.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/egor.jpg')


async def phoenix1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{phoenix}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/phoenix.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/andrey.jpg')


async def raze1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{raze}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/raze.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/andrey.png')


async def reyna1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{reyna}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/reyna.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/andrey.png')


async def sage1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{sage}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/sage.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/angela.jpg')


async def skye1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{skye}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/skye.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/angela.jpg')


async def sova1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{sova}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/sova.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/shaman.jpg')


async def viper1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{viper}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/viper.png')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/angela.jpg')


async def yoru1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{yoru}')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/yoru.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='chads/egor.jpg')


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
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/Ascent.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/Split.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/Fracture.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/Bind.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/Breeze.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/Lotus.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/Pearl.jpg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/Icebox.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/TheRange.jpeg')
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo='data/Haven.jpeg')


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
    addon.add_handler(CommandHandler('astra', astra1))
    addon.add_handler(CommandHandler('breach', breach1))
    addon.add_handler(CommandHandler('brimstone', brimstone1))
    addon.add_handler(CommandHandler('chamber', chamber1))
    addon.add_handler(CommandHandler('cypher', cypher1))
    addon.add_handler(CommandHandler('fade', fade1))
    addon.add_handler(CommandHandler('gekko', gekko1))
    addon.add_handler(CommandHandler('harbor', harbor1))
    addon.add_handler(CommandHandler('jett', jett1))
    addon.add_handler(CommandHandler('kayo', kayo1))
    addon.add_handler(CommandHandler('killjoy', kj1))
    addon.add_handler(CommandHandler('neon', neon1))
    addon.add_handler(CommandHandler('omen', omen1))
    addon.add_handler(CommandHandler('phoenix', phoenix1))
    addon.add_handler(CommandHandler('raze', raze1))
    addon.add_handler(CommandHandler('reyna', reyna1))
    addon.add_handler(CommandHandler('sage', sage1))
    addon.add_handler(CommandHandler('skye', skye1))
    addon.add_handler(CommandHandler('sova', sova1))
    addon.add_handler(CommandHandler('viper', viper1))
    addon.add_handler(CommandHandler('yoru', yoru1))
    addon.run_polling()
