#-*- coding: utf-8 -*-

class Bot:

    def process(self, text_list):
        resp = ""
        for line in text_list:
            std = line.split(" ")
            time = std[0]
            name = std[1]
            resp += name + " 님은 바보\n"
        return resp.strip()
