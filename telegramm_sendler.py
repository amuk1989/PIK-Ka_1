import requests
import telebot

def send_telegram(text: str):
    chat_id = '-1001490792674'
    method = "sendMessage"
    token = "1846413915:AAETjV3q2tkVYulqA8WFnv17pCMBHbFsf94"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)