# -*- coding: utf-8 -*-
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel access token (long-lived)
line_bot_api = LineBotApi('IggejjtYm0rLnHJ7aLVk2w1S9mqm8roItmjWuZ2NP0pvLefHbu1lkcnHLDkJYaXnlDn+CKdddMM4rhCn8lTtW1I5qCQakKN2Jym/dzzWojM/KhPicMAxsaBcK/4NHDlgq4677UQUfYza0ZaI1Pnr8wdB04t89/1O/w1cDnyilFU=')

# Channel secret 
handler = WebhookHandler('7b7ac971727df0611a71e5ad86b63272')

# User ID
userID = 'Ue7ec45513a34d6c0353321d0166b7877'


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def get_time():
	from datetime import datetime 
	now_time = datetime.now().strftime('%Y-%m-%d %H:%M')
	return now_time
	
message = TextSendMessage( get_time())
line_bot_api.push_message(userID, message)


	
if __name__ == '__main__':
    app.run(debug=True)