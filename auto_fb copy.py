from ToolAutoFB import AutoFB
import random
import json
import time
from ultils import *
from threading import Thread, Barrier

def autofb4multile(username, password):
    print(username , password)
    # Get url add friends
    f = open("./url_fb/url_LT.json", encoding="utf8")
    urls = json.load(f)
    urls = list(urls.values())
    #_______________________________
    start_time = time.time()
    print(frame("Login vào "+ username, 1, 3))
    auto = AutoFB(username = username,
                password = password)
    driver = auto.open_profile()
    time.sleep(10)
    try:
        auto.login_fb()
    except:
        pass
    time.sleep(10)
    actions = [
        'story', 'post', 'addfriend', 'post', 'story', 'story', 'post',
        'addfriend'
    ]
    random.shuffle(actions)
    actions = ['post'] + actions
    num_addfriends = 0
    num_watch_posts = 0
    num_watch_storys = 0
    num_get_urls = 0
    for action in actions:
        # action = random.choice(actions)
        print('############### Action: ', action)
        # action = 'story'
        if action == 'story':
            num_watch_story = auto.watch_story()
            num_watch_storys += num_watch_story
        elif action == 'post':
            num_watch_post = auto.watch_post()
            num_watch_posts += num_watch_post
        elif action == 'addfriend':
            urls, num_add, num_get_url = auto.add_friends(urls)
            num_addfriends += num_add
            num_get_urls += num_get_url
        sleep_very_very_long()
    auto.logout_fb()
    print(f'Đã kết bạn với {num_addfriends} người')
    print(f'Đã vào {num_get_urls} link')
    print(f'Đã xem {num_watch_posts} post')
    print(f'Đã xem {num_watch_storys} stories')
    print('Thời gian chạy: ', (time.time() - start_time) / 60)
    driver.close()

# Get account clone
f = open("./acc_clone/acc_clone.json", encoding="utf8")
profile = json.load(f)

number_of_threads = 8

barrier = Barrier(number_of_threads)

threads = []

for i in range(number_of_threads):
    username = list(profile[0].keys())[i]
    password = profile[0].get(list(profile[0].keys())[i])
    t = Thread(target=autofb4multile, args={username,password}) 
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()

