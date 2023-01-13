from ToolAutoFB import AutoFB
import random
import json
import time
import os
from ultils import *
from threading import Thread


def autofb4multile(username, password):
    # Get url add friends
    f = open("./url_fb/url_LT.json", encoding="utf8")
    urls = json.load(f)
    urls = list(urls.values())
    #_______________________________
    start_time = time.time()
    print(frame("Login vào " + username, 1, 3))
    auto = AutoFB(username=username, password=password)
    driver = auto.open_profile()
    time.sleep(10)
    try:
        auto.login_fb()
    except:
        pass
    time.sleep(10)
    actions = [
        'post','story', 'post', 'addfriend', 'post', 'story', 'story', 'post',
        'addfriend'
    ]
    random.shuffle(actions)
    actions = ['story'] + actions
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
    print(f'{username} Đã kết bạn với {num_addfriends} người')
    print(f'{username} Đã vào {num_get_urls} link')
    print(f'{username} Đã xem {num_watch_posts} post')
    print(f'{username} Đã xem {num_watch_storys} stories')
    print(f'{username} Thời gian chạy: ', (time.time() - start_time) / 60)
    driver.close()

def main():
    cwd = os.getcwd()
    # Get acc clone
    path_acc_clone = os.path.join(cwd, './acc_clone/acc_clone.txt')
    with open(path_acc_clone, 'r', encoding="utf8") as f:
            acc_clone = [word[:-1] for word in f]
    acc_clone = [acc_clone[i].split("|") for i in range(len(acc_clone))]
    threads = []

    session = []
    leng_session = (len(acc_clone) // 4) + 1 if len(acc_clone)%4 !=0 else len(acc_clone)/4

    for _ in range(int(leng_session)):
        session.append(acc_clone[:4])
        acc_clone = acc_clone[4:]
        
    for list_acc_clone in session:
        for i in range(len(list_acc_clone)):
            username , password = list_acc_clone[i][0], list_acc_clone[i][1]
            threads.append(Thread(target=autofb4multile, args=(username,
                                                            password,)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
if __name__ == "__main__":
    main()