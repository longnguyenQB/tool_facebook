from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        #like:
        element_click_and_hold = self.driver.find_element(
            By.XPATH, '//div[@aria-label="Bày tỏ cảm xúc"]')
        action = ActionChains(driver)
        action.click_and_hold(element_click_and_hold)
        action.perform()
        time.sleep(1)
        reaction = choice_reaction()
        self.driver.find_element(
                            By.XPATH,
                            '//div[@aria-label="' + reaction + '"]').click()
        sleep_short()
        comment_box = self.driver.find_element(
            By.XPATH, '//div[@aria-label="Viết bình luận"]')
        sleep_short()
        comment = random.choice(comments)
        comments.remove(comment)
        comment = re.sub(
            '[^a-zA-Z0-9áàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđ,.]',
            ' ', comment)
        print(comment)
        comment_box.send_keys(" " + comment + Keys.ENTER)
        return comments


link_seeding = 'https://www.facebook.com/groups/odaychungtoiquantamdenlamdep/posts/1434645447061615/'
# link_source = input('Enter link source: ')
# with open('./Crawl/cookies_profile.txt', 'r') as f:
#     cookies_profile = [line[:-1] for line in f]
# profile_name = [
#     'Profile 3', 'Profile 5', 'Profile 6', 'Profile 7', 'Profile 8',
#     'Profile 10', 'Profile 11', 'Profile 12', 'Default'
# ]
# random.shuffle(profile_name)
# comments = get_comment_from_post(post_url=link_source,
#                                  cookies_profile=cookies_profile)
comments = [
'rỗ quá đừng nặn mụn nữa b ơi, mình nghĩ bạn nên ăn uống hợp lý, đừng ăn cay quá nó dễ nổi mụn, mà đã nổi mụn thì đừng nặn, cứ để nó lên, hết mụn rồi thì dùng chanh hoặc nghệ với mật ong rồi xát lên'
]
profile_name = ['Profile 4']
for profile in profile_name:
    print('*************************' * 20 + "\n" + str(profile))
    auto = AutoSeedingPostDetail(profile)
    driver = auto.open_profile()
    time.sleep(4)
    comments = auto.comment_post(comments, link_seeding)
    sleep_very_long()
    driver.close()