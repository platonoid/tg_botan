from flask import Flask, request
import requests

app = Flask(__name__)


def brawlstars():
    return 'Привет'


def send_message(chat_id, text):
    method = "sendMessage"
    token = "6145174608:AAE_RKJRKNY_t82sPknD1mglkQu5qpXqVKw"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        print(request.json)
        chat_id = request.json["message"]["chat"]["id"]
        weather = brawlstars()
        send_message(chat_id, weather)
    return {"ok": True}
