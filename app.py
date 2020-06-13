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

line_bot_api = LineBotApi('IggejjtYm0rLnHJ7aLVk2w1S9mqm8roItmjWuZ2NP0pvLefHbu1lkcnHLDkJYaXnlDn+CKdddMM4rhCn8lTtW1I5qCQakKN2Jym/dzzWojM/KhPicMAxsaBcK/4NHDlgq4677UQUfYza0ZaI1Pnr8wdB04t89/1O/w1cDnyilFU=')
# Channel access token (long-lived)
handler = WebhookHandler('7b7ac971727df0611a71e5ad86b63272')
# Channel secret 

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

    if event.message.text.startswith('貼圖'):
        text = event.message.text
        _, package_id, sticker_id = text.split('-')
        message = StickerSendMessage(
            package_id=int(package_id),
            sticker_id=int(sticker_id)
        )

def getNews():
    """
    建立一個抓最新消息的function
    """
    import requests
    import re
    from bs4 import BeautifulSoup

    url = 'https://www.ettoday.net/news/focus/3C%E5%AE%B6%E9%9B%BB/'
    r = requests.get(url)
    reponse = r.text

    url_list = re.findall(r'<h3><a href="/news/[\d]*/[\d]*.htm" .*>.*</a>',reponse)

    soup = BeautifulSoup(url_list[0])
    url = 'https://fashion.ettoday.net/' + soup.find('a')['href']
    title = soup.text


    tmp = title + ': ' +url
    return tmp

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 傳送文字
    if event.message.text == '傳送文字':
        message = TextSendMessage(getNews())
    else:
        message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == '__main__':
    app.run(debug=True)