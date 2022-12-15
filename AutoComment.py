from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from ultils import *
import time
import random
import json
import re


class AutoSeedingPostDetail:
    def __init__(self, profile_name):
        super().__init__()
        self.profile_name = profile_name

    def open_profile(self):
        profile = launchBrowser(self.profile_name)
        self.driver = profile
        return self.driver

    def comment_post(self, comments, link_seeding):
        self.driver.get(link_seeding)
        time.sleep(2)
        comment_box = self.driver.find_element(
            By.XPATH, '//div[@aria-label="Viết bình luận"]')
        comment = random.choice(comments)
        comment_box.send_keys(" " + comment + Keys.ENTER)
        comments.remove(comment)
        return comments

link_source = input('Enter link source: ')
link_seeding = input('Enter link seeding: ')
with open('./Crawl/cookies_profile.txt', 'r') as f:
    cookies_profile = [line[:-1] for line in f]
profile_name = [
    'Profile 3', 'Profile 5', 'Profile 6', 'Profile 7', 'Profile 8',
    'Profile 10', 'Profile 11', 'Profile 12', 'Default'
]
random.shuffle(profile_name)
comments = get_comment_from_post(post_url=link_source,
                                 cookies_profile=cookies_profile)

for profile in profile_name:
    print('*************************' * 20 + "\n" + str(profile))
    auto = AutoSeedingPostDetail(profile)
    driver = auto.open_profile()
    time.sleep(4)
    comments = auto.comment_post(comments, link_seeding)
    time.sleep(random.choice(range(200,300)))
    driver.close()
