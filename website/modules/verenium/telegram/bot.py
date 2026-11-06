"""Verenium private-chat navigator. Python 3.9+, standard library only."""
import getpass
import json
import os
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = 'https://ezargaruna.github.io/suticore/'
FORM = 'https://docs.google.com/forms/d/e/1FAIpQLScXLTMQ3UUywSRd73n-817sHVL3bfWpas5jlu9KWCAdSDXlyg/viewform'
ROUTES = {
 'care': ('забота', ['что нужно прямо сейчас?', 'какая поддержка тебе подходит?', 'чем хочется поделиться или обменяться?']),
 'order': ('порядок', ['что занимает внимание?', 'что можно отложить?', 'какой один шаг по силам сегодня?']),
 'council': ('нейровече', ['какой вопрос общий?', 'что известно и на чём это основано?', 'кого услышали, что решили и когда проверим?']),
 'setup': ('установка', ['скачай архив и распакуй в новую папку.', 'открой verenium.html в браузере.', 'для SUTI.os распакуй вложенный архив и открой папку vault в Obsidian.'])
}
DEPTHS = ('касание', 'различение', 'сборка')
def button(title, value, link=False):
    return {'text': title, 'url' if link else 'callback_data': value}

def screen(key):
    if key == 'stop':
        return 'останавливаемся здесь. маршрут бот не хранит. вернуться можно через /start.', []
    if key == 'privacy':
        return 'это чат Telegram. бот не записывает ответы и не передаёт их участникам. история чата остаётся в Telegram. для личных заметок открой карту; Google-анкета отправляет ответы отдельно, по нажатию «отправить».', [[button('личная карта', BASE+'care-map.html', True)], [button('в меню','home')]]
    parts = key.split(':')
    if parts[0] in ROUTES and len(parts)==2 and parts[1] in ('0','1','2'):
        route, level = parts[0], int(parts[1])
        title, cues = ROUTES[route]
        rows = [[button(d, route+':'+str(i)) for i,d in enumerate(DEPTHS)]]
        if route=='care':
            rows += [[button('карта для себя', BASE+'care-map.html',True),button('анкета заботы',FORM,True)],[button('атлас взаимной заботы', BASE+'care-atlas.html',True)]]
        else:
            rows += [[button('открыть мастерскую',BASE+'verenium.html#'+route,True)]]
        if route=='setup':
            rows += [[button('скачать Verenium с SUTI.os',BASE+'downloads/Verenium.zip',True)]]
        rows += [[button('в меню','home'),button('закончить','stop')]]
        return title+' · '+DEPTHS[level]+'\n\n'+'\n'.join(cues[:level+1]), rows
    return '∴ Verenium · друг заботы\nчто тебе сейчас нужно? можно выбрать один шаг или просто посмотреть.', [[button(ROUTES[k][0],k+':0') for k in pair] for pair in [('care','order'),('council','setup')]]+[[button('о данных','privacy'),button('закончить','stop')]]

class Failure(Exception):
    def __init__(self, code, retry=1):
        self.code, self.retry = code, retry

def run(token):
    def api(method, **data):
        req=Request('https://api.telegram.org/bot'+token+'/'+method,data=urlencode({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in data.items()}).encode())
        try:
            with urlopen(req,timeout=45) as r:return json.load(r)['result']
        except HTTPError as e:
            try:retry=json.load(e).get('parameters',{}).get('retry_after',1)
            except ValueError:retry=1
            raise Failure(e.code,retry) from None
    me=api('getMe')
    if me['username'].lower()!='verenium_bot':sys.exit('токен другого бота; настройки не менялись.')
    if api('getWebhookInfo')['url']:sys.exit('у бота уже есть webhook. действующий обработчик не изменён.')
    api('setMyCommands',commands=[{'command':k,'description':v} for k,v in [('start','выбрать маршрут'),('privacy','как устроены данные'),('stop','закончить')]])
    print('Verenium: личные чаты, long polling.',flush=True)
    offset=0
    while True:
        try:
            for u in api('getUpdates',offset=offset,timeout=25,allowed_updates=['message','callback_query']):
                q=u.get('callback_query',{}); m=q.get('message') or u.get('message',{}); chat=m.get('chat',{})
                if chat.get('type')=='private':
                    key=q.get('data') or {'/privacy':'privacy','/stop':'stop'}.get(m.get('text','').split('@')[0],'home')
                    txt,rows=screen(key)
                    try:
                        if q:api('answerCallbackQuery',callback_query_id=q['id'])
                        api('sendMessage',chat_id=chat['id'],text=txt,reply_markup={'inline_keyboard':rows})
                    except Failure as e:
                        if e.code not in (400,403):raise
                offset=u['update_id']+1
        except Failure as e:
            if e.code in (401,409):sys.exit('токен недействителен или уже работает другой обработчик.')
            time.sleep(max(2,e.retry))
        except (URLError,TimeoutError):time.sleep(3)

if __name__=='__main__':
    token=os.getenv('TELEGRAM_BOT_TOKEN') or getpass.getpass('токен @verenium_bot (ввод скрыт): ')
    if not token:sys.exit('токен не задан')
    try:run(token)
    except Failure as e:sys.exit('Telegram API: '+str(e.code))
