from flask import Flask, request
import telegram
#from telegram import bot
from telebot.credentials import bot_token, bot_user_name,URL
from telebot.mastermind import get_response


#global botA
global TOKEN
TOKEN = bot_token
#botA = telegram.bot(token = TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), telegram.bot(token = TOKEN))

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text_to_be_analyzed = update.message.text.encode('utf-8').decode()

    response = get_response(text)
    telegram.bot(token = TOKEN).sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

    return 'ok'

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)
