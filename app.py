from flask import Flask, request
import os
from dotenv import load_dotenv
from telegram.ext import CommandHandler, MessageHandler, filters, Application
import logging
import telegram

load_dotenv()
app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

addon = Application.builder().token('6084013080:AAGX8y5i-XAv514ZvUU5PzC45A8iZorLVW0').build()


async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a Chamber, please talk to me!")


def reply(update, context):
    try:
        text = update.message.text
        context.bot.send_message(chat_id=update.message.chat_id, text=text)
    except Exception as e:
        context.bot.send_message(chat_id=update.message.chat_id, text='Ошибка: ' + str(e))


addon.add_handler(CommandHandler('start', start))
reply_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), reply)


@app.route('/', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), addon.bot)
    addon.process_update(update)
    return 'ok'


if __name__ == '__main__':
    addon = Application.builder().token("6084013080:AAGX8y5i-XAv514ZvUU5PzC45A8iZorLVW0").build()
    addon.add_handler(CommandHandler('start', start))
    addon.run_polling()
