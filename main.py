from ToolAutoFB import AutoFB
from ultils import *
import json
import time

f = open("./url_fb/url_LT.json", encoding="utf8")
url_LT = json.load(f)
start_time = time.time()
urls = list(url_LT.values())

auto = AutoFB(username = "nguyenlonglttt@gmail.com",
              password = "longqblt123")
driver = auto.open_profile()
try:
    auto.login()
except:
    pass
time.sleep(4)
auto.logout()
actions = [
    'story', 'post', 'addfriend', 'post', 'story', 'story', 'post',
    'addfriend', 'addfriend'
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
    # action = 'addfriend'
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
print(f'Đã kết bạn với {num_addfriends} người')
print(f'Đã vào {num_get_urls} link')
print(f'Đã xem {num_watch_posts} post')
print(f'Đã xem {num_watch_storys} stories')
print('Thời gian chạy: ', (time.time() - start_time) / 60)
driver.close()