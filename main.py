# coding: utf-8
import os
try:
    from urlparse import urlparse
except:
    from urllib.parse import urlparse
import requests
import datetime
import json
import smtplib
from email.mime.text import MIMEText
from settings import MAILL_SETTING

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}
SAVE_FILE = "save.json"

if not os.path.isfile(SAVE_FILE):
    print("create %s" % SAVE_FILE)
    SAVE_FILE = open(SAVE_FILE, "w")
    SAVE_FILE.write("{}")
    SAVE_FILE.close()


def send_mail(title, text):
    maill_boday = text
    print(maill_boday)
    msg = MIMEText(maill_boday, 'html', 'utf-8')
    msg['From'] = MAILL_SETTING['from']
    msg['To'] = MAILL_SETTING['to']
    msg['Subject'] = '[JRMonitor] ' + title

    server = smtplib.SMTP(MAILL_SETTING['smtp'])
    server.login(user=MAILL_SETTING["from"],
                 password=MAILL_SETTING['password'])
    server.send_message(msg=msg)
    server.close()


def load_cards():
    card_json=open(SAVE_FILE, "r")
    card_dict = json.load(card_json)
    card_json.close()
    if not card_dict:
        return {}
    return card_dict


def save_card(id, title, text):
    card_dict = (load_cards())
    if id not in card_dict:
        card_dict[id] = title
        save_file = open(SAVE_FILE, "w")
        save_file.write(json.dumps(
            card_dict, ensure_ascii=False, indent=2))
        save_file.close()
        send_mail(title, text)


def scan_cards_list(id=None):
    url = "https://m.weibo.cn/api/container/getIndex?type=uid&value=5886054987&containerid=1076035886054987&page="
    if id:
        url = url+str(id)
    response = requests.get(url, headers=header)
    res_json = response.content
    res_dict = json.loads(res_json)
    for i in res_dict['data']['cards']:
        if "mblog" in i:
            if '改造预告' in i['mblog']['text']:
                print('-----------------'+i['mblog']['text'])
                text = "<a href='"+i['scheme'] + \
                    "'>改造预告</a><br>" + i['mblog']['text']
                save_card(i['mblog']['id'], '改造预告', text)
            if '新船预告' in i['mblog']['text']:
                print('-----------------'+i['mblog']['text'])
                text = "<a href='"+i['scheme'] + \
                    "'>新船预告</a><br>" + i['mblog']['text']
                save_card(i['mblog']['id'], '新船预告', text)


if __name__ == '__main__':
    scan_cards_list()
