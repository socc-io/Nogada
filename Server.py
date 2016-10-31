#!/usr/bin/python
from flask import Flask, request, send_from_directory
app = Flask(__name__, static_url_path='/static')


#### BOT ##################
import SimpleBot
bot_room = {
    'SOCC' : SimpleBot.Bot()
}
    
#### Filter ###############
t_cache = {'SOCC' : []}
def filter_text(chat_room, text):
    spd_cache = t_cache[chat_room]
    spd_text = text.split("\n")[:30]
    mrg_text = []
    last_line = ""
    for line in spd_text:
        if len(line) > 5 and str.isdigit(line[:2])\
          and line[2] == ":" and str.isdigit(line[3:5]):
            mrg_text.append(last_line.strip())
            last_line = line
        elif len(line) > 5 and line[4] != '년':
            last_line = last_line.strip() + " " + line
    mrg_text.append(last_line.strip())
    mrg_text.pop(0)
    start_idx = 0
    for idx, txt in enumerate(mrg_text[::-1]):
        isnew = True
        for cache in spd_cache[::-1]:
            if cache == txt:
                isnew = False
        if isnew:
            start_idx = idx + 1
    t_cache['SOCC'] = mrg_text
    return mrg_text[len(mrg_text) - start_idx:]

@app.route("/bot", methods=["POST"])
def bot_input():
    text = request.json['text'].encode('utf-8')
    chat_room =  request.json['chat_room'].encode('utf-8')
    resp = ""
    if bot_room[chat_room] != None:
        f_text = filter_text(chat_room, text)
        for t in f_text:
            print 'ROOM :', chat_room , ', TEXT :', t
        resp = bot_room[chat_room].process(f_text)
    return resp

@app.route("/static/<path:path>")
def send_html(path):
    return send_from_directory('static',path)

app.run(host="0.0.0.0",port=5999)
