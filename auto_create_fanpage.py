from ToolAutoFB import AutoCreateFanpage
import random
import json
import os
import time

# Get account clone
f = open("./acc_clone/acc_clone.json", encoding="utf8")
profile = json.load(f)

for key in profile[0].keys():
    start_time = time.time()
    username , password = key, profile[0].get(key)
    auto = AutoCreateFanpage(username = username,
                password = password)
    driver = auto.open_profile()
    try:
        auto.login_fb()
    except:
        pass
    time.sleep(4)
    auto.create_fanpage()
    time.sleep(random.choice(range(200,300)))
    driver.close()
