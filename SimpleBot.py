#-*- coding: utf-8 -*-

class Bot:

    def __init__(self):
        self.init_moim()

    def init_moim(self):
        self.moim = ["", "", "", "알고리즘", "머신러닝", "정기모임"]
        self.person = [[],[],[],[],[],[]]
        
    def process(self, text_list):
        resp = ""
        for line in text_list:
            std = line.split(" ")
            time = std[0]
            name = std[1]
            text = " ".join(std[2:])
            line_result = ""
            if "@봇" in text :
                if "모임참여" in text and "교시" in text:
                   for c in text:
                       if str.isdigit(c):
                           c = int(c)
                           if c < len(self.moim) and len(self.moim[c]) > 0:
                               line_result += self.moim[c] + " 교시에 참여하였습니다. "
                               if name not in self.person[c]:
                                   self.person[c].append(name)
                           else:
                               line_result += str(c) + "는 존재하지 않는 교시입니다. "
                if "모임참여현황" in text:
                    for i in range(len(self.moim)):
                        if len(self.moim[i]) > 0:
                            line_result += self.moim[i] + " 참여자는 "\
                              + str(len(self.person[i])) + "명 입니다. "
                if "모임초기화" in text:
                    self.init_moim()
                    for i, mname in enumerate(self.moim):
                        if len(mname) > 0:
                            line_result += mname + " 참여자는 "\
                              + str(len(self.person[i])) + "명 입니다. "
                if "모임참여취소" in text and "교시" in text:
                    for c in text:
                       if str.isdigit(c):
                           c = int(c)
                           if c < len(self.moim) and len(self.moim[c]) > 0:
                               line_result += self.moim[c] + " 교시를 취소 하였습니다. "
                               if name in self.person[c]:
                                   self.person[c].remove(name)
                           else:
                               line_result += str(c) + "는 존재하지 않는 교시입니다. "
                if "저녁메뉴" in text :
                    line_result = " 강남불백 이 좋겠네요! "
                if len(line_result) == 0:
                    line_result = "다시 말씀해 주세요! "
                resp += "@" + name + " " + line_result + "\n"
        return resp.strip()
