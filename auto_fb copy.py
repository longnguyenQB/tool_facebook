from ToolAutoFB import AutoFB
import random
import json
import time
from ultils import *
from threading import Thread, Barrier

# Get url add friends
f = open("./url_fb/url_LT.json", encoding="utf8")
url_LT = json.load(f)
urls = list(url_LT.values())
# Get account clone
f = open("./acc_clone/acc_clone.json", encoding="utf8")
profile = json.load(f)

number_of_threads = 5

barrier = Barrier(number_of_threads)

threads = []

for i in range(number_of_threads):
    username = list(profile[0].keys())[i]
    password = profile[0].get(list(profile[0].keys())[i])
    auto = AutoFB(username = username,
                password = password)
    t = Thread(target=auto.open_profile()) 
    t.start()
    threads.append(t)

for t in threads:
    t.join()

