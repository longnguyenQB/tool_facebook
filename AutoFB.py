from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ultils import *
import time
import random
import json


class AutoFB:
    def __init__(self, profile_name):
        super().__init__()
        self.profile_name = profile_name

    def open_profile(self):
        profile = launchBrowser(self.profile_name)
        self.driver = profile
        return self.driver

    def watch_story(self):
        self.driver.get("http://www.facebook.com/")
        sleep_long()
        #Click vào story đầu tiên:
        self.driver.find_element(
            By.XPATH,
            '//div[@class="x1g0ag68 xx6bhzk x11xpdln xcj1dhv x1ey2m1c x9f619 xds687c x10l6tqk x17qophe x13vifvy"]'
        ).click()
        tmp = 0
        #Chọn xem bao nhiêu story:
        num_watch_story = random.choice(range(3, 8))
        for _ in range(num_watch_story):
            tmp += 1
            print('_____________', tmp)
            if random.choice(['reaction', 'no']) == 'reaction':
                reaction = choice_reaction()
                sleep_long()  #Xem story
                #Chọn reaction bao nhiêu lần
                for _ in range(random.choice(range(1, 7))):
                    print('_________________________________ ', reaction)
                    try:
                        self.driver.find_element(
                            By.XPATH,
                            '//div[@aria-label="' + reaction + '"]').click()
                    except:
                        print("Không tìm được element thả reaction")
                        pass
            sleep_short()
            try:
                self.driver.find_element(
                    By.XPATH, '//div[@aria-label="Nhóm tiếp theo"]').click()
                sleep_short()
            except:
                self.driver.find_element(
                    By.XPATH, '//div[@aria-label="Thẻ tiếp theo"]').click()
                sleep_short()
        self.driver.get("http://www.facebook.com/")
        return num_watch_story

    def watch_post(self):
        self.driver.get("http://www.facebook.com/")
        sleep_long()
        element = self.driver.find_element(By.TAG_NAME, "body")
        # Chọn số lần xem post
        num_watch_post = random.choice(range(15, 20))
        for i in range(0, num_watch_post):
            reaction = random.choice(['reaction', 'no'])
            comment = random.choice(['comment', 'no', '1', '2', '3'])
            open_post = random.choice(['open', 'no'])
            sleep_very_long()
            print('__________________Lần xem post thứ: ', i)
            if (reaction == 'reaction') & (comment == 'comment') & (open_post
                                                                    == 'open'):
                # element1 = driver.switch_to.active_element
                # Func = open("tmp.html", "w", encoding="utf-8")
                # Func.write(element1.get_attribute('innerHTML'))
                # Func.close()
                print('reaction + comment + open post')
                element.send_keys(Keys.ESCAPE + "j" + 'l' + Keys.ARROW_RIGHT *
                                  random.choice(range(1, 3)) + Keys.ENTER +
                                  'o')
            if (reaction == 'reaction') & (comment == 'comment') & (open_post
                                                                    != 'open'):
                print('reaction + comment')
                element.send_keys(Keys.ESCAPE + "j" + 'l' + Keys.ARROW_RIGHT *
                                  random.choice(range(1, 3)))
            elif (reaction == 'reaction') & (comment != 'comment'):
                print('reaction')
                element.send_keys(Keys.ESCAPE + "j" + 'l' + Keys.ARROW_RIGHT *
                                  random.choice(range(1, 3)) + Keys.ENTER)
                element = self.driver.find_element(By.TAG_NAME, "body")
            elif (reaction !=
                  'reaction') & (comment != 'comment') & (open_post == 'open'):
                print('just open post')
                element.send_keys(Keys.ESCAPE +
                                  "j" * random.choice(range(1, 4)) + "o")
            elif (reaction !=
                  'reaction') & (comment != 'comment') & (open_post != 'open'):
                print('no action')
                element.send_keys(Keys.ESCAPE +
                                  "j" * random.choice(range(1, 4)))
        return num_watch_post

    def add_friends(self, urls):
        s = 0
        it = random.choice(range(3, 5))
        random.shuffle(urls)
        num_add = 0
        print(s, it, len(urls))
        while (s <= it):
            url = urls[s]
            s += 1
            print(s)
            print('Đã vào link: ', url)
            self.driver.get(url)
            sleep_very_long()
            element = self.driver.find_element(By.TAG_NAME, "body")
            sleep_short()
            element.send_keys("j")
            sleep_long()
            try:
                elements_list_reactions = self.driver.find_elements(
                    By.XPATH,
                    '//div[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1n2onr6 x87ps6o x1lku1pv x1a2a7pz x1heor9g xnl1qt8 x6ikm8r x10wlt62 x1vjfegm x1lliihq"]'
                )
            except:
                try:
                    elements_list_reactions = self.driver.find_elements(
                        By.XPATH,
                        '//div[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1n2onr6 x87ps6o x1lku1pv x1a2a7pz x1heor9g xnl1qt8 x6ikm8r x10wlt62 x1vjfegm x78zum5"]'
                    )
                except:
                    print(
                        "Không tìm được element hiển thị những người reaction")
                    pass
            print('Số lượng elements_list_reactions: ',
                  len(elements_list_reactions))
            for elements_list_reaction in elements_list_reactions:
                try:
                    elements_list_reaction.click()
                    sleep_short()
                    elements_add = self.driver.find_elements(
                        By.XPATH, '//*[@aria-label="Thêm bạn bè"]')
                    print("Số lượng elements thêm bạn bè tìm được: ",
                          len(elements_add))
                    for elem in elements_add:
                        try:
                            elem.click()
                            num_add += 1
                            print(f'Đã kết bạn với {num_add} người')
                        except:
                            element_notclick = driver.switch_to.active_element
                            element_notclick.send_keys(Keys.ESCAPE)
                            print("Không click vào được element Thêm bạn bè")
                            pass
                        sleep_short()
                    if len(elements_add) < 20:
                        print("Lướt thêm bài tiếp")
                        element_scroll = self.driver.switch_to.active_element
                        element_scroll.send_keys(Keys.ESCAPE)
                    else:
                        break
                    # action_scroll = self.driver.switch_to.active_element
                except:
                    print(
                        "Không click vào được element hiển thị những người reaction"
                    )
                    pass
            try:
                urls.remove(url)
            except:
                break
        return urls, num_add, it


f = open("./url_fb/url_LT.json", encoding="utf8")
data = json.load(f)
# profile_name = [
#     'Profile 3', 'Profile 5', 'Profile 6', 'Profile 7', 'Profile 8',
#     'Profile 10', 'Profile 11', 'Profile 12', 'Default'
# ]
profile_name = ['Profile 3', 'Profile 5', 'Profile 6', 'Profile 8']
random.shuffle(profile_name)
for profile in profile_name:
    start_time = time.time()
    urls = list(data.values())
    print('*************************' * 20 + "\n" + str(profile))
    auto = AutoFB(profile)
    driver = auto.open_profile()
    time.sleep(4)
    actions = [
        'story', 'post', 'addfriend', 'post', 'story', 'story', 'post',
        'addfriend', 'addfriend'
    ]
    # actions = ['addfriend', 'addfriend', 'addfriend']
    random.shuffle(actions)
    actions = ['post'] + actions
    num_addfriends = 0
    num_watch_posts = 0
    num_watch_storys = 0
    num_get_urls = 0
    for action in actions:
        # action = random.choice(actions)
        print('############### Action: ', action)
        action = 'addfriend'
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