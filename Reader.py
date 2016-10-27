import Config
import time

input_file = Config.input_path
prev_txt = "\n"
while True:
    time.sleep(2)
    prev = prev_txt.split("\n")
    prev.pop()
    now_txt = open(input_file,'r').read()
    now = now_txt.split("\n")
    if len(prev) <= 1 :
        print now_txt
    now.pop()
    new = []
    gate = False
    for idx, row in enumerate(now):
        if gate :
            new.append(row)
        if row == prev[-1]:
            gate = True
    for row in new:
        print row
        
    prev_txt = now_txt
        
