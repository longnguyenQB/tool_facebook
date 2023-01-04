from ToolAutoFB import AutoFB
import random
import json
import time
from ultils import *

# Get url add friends
f = open("./url_fb/url_LT.json", encoding="utf8")
url_LT = json.load(f)
urls = list(url_LT.values())
# Get account clone
f = open("./acc_clone/acc_clone.json", encoding="utf8")
profile = json.load(f)
for key in profile[0].keys():
    start_time = time.time()
    print(frame("Login vào "+ key, 1, 3))
    username , password = key, profile[0].get(key)
    auto = AutoFB(username = username,
                password = password)
    driver = auto.open_profile()
    try:
        auto.login_fb()
    except:
        pass
    time.sleep(5)
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
