from flask import Flask, request
import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
import logging
import telegram

load_dotenv()
app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

updater = Updater(token = os.getenv('TOKEN'), use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Я бот. Как дела?")


def reply(update, context):
    try:
        text = update.message.text
        context.bot.send_message(chat_id=update.message.chat_id, text=text)
    except Exception as e:
        context.bot.send_message(chat_id=update.message.chat_id, text='Ошибка: ' + str(e))

start_handler = CommandHandler('start', start)
reply_handler = MessageHandler(Filters.text & (~Filters.command), reply)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(reply_handler)


@app.route('/', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), updater.bot)
    dispatcher.process_update(update)
    return 'ok'


if __name__ == '__main__':
    updater.start_webhook(listen="0.0.0.0",
                          port=8443,
                          url_path='6084013080:AAGX8y5i-XAv514ZvUU5PzC45A8iZorLVW0')
    updater.bot.setWebhook(url='https://your-bot-url.com/' + '6084013080:AAGX8y5i-XAv514ZvUU5PzC45A8iZorLVW0')
    app.run()
