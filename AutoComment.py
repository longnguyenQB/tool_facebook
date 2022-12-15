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
import os


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
        try:
            element_click_and_hold = self.driver.find_element(
                By.XPATH, '//div[@aria-label="Bày tỏ cảm xúc"]')
            action = ActionChains(driver)
            action.click_and_hold(element_click_and_hold)
            action.perform()
            time.sleep(1)
            reaction = choice_reaction()
            self.driver.find_element(
                                By.XPATH,
                                '//div[@aria-label="' + reaction +'"]').click()
            print('Đã reaction')
        except:
            try:
                element_click_and_hold = self.driver.find_element(
                By.XPATH, '//div[@aria-label="Thích"]')
                action = ActionChains(driver)
                action.click_and_hold(element_click_and_hold)
                action.perform()
                time.sleep(1)
                reaction = choice_reaction()
                self.driver.find_element(
                                    By.XPATH,
                                    '//div[@aria-label="' + reaction + '"]').click()
                print('Đã reaction')
            except:
                pass

        sleep_long()
        check_dialog(self.driver)
        # comment_box = self.driver.find_element(
        #     By.XPATH, '//div[@aria-label="Viết bình luận"]')
        try:
            comment_box = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Viết bình luận"]')))
            sleep_short()
        except:
            comment_box = self.driver.find_element(
                By.XPATH, '//div[@aria-label="Viết bình luận"]')
        comment = random.choice(comments)
        comments.remove(comment)
        comment = re.sub(
            '[^a-zA-Z0-9áàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđ,.:)=]',
            ' ', comment)
        print(comment)
        comment_box.click()
        sleep_very_short()
        comment_box.send_keys(" " + comment + Keys.ENTER)
        check_dialog(self.driver)

        comments.remove(comment)
        return comments

# link_source = input('Enter link source: ')
link_seeding = 'https://www.facebook.com/groups/genzlethuy/posts/1092292301440556/'
# input('Enter link seeding: ')
cookies_profiles = []
for root, dirs, files in os.walk("./Cookies"):
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(root, file), 'r') as f:
                cookies_profiles.append(json.load(f.read))
# profile_name = [
#     'Profile 3', 'Profile 5', 'Profile 6', 'Profile 7', 'Profile 8',
#     'Profile 10', 'Profile 11', 'Profile 12', 'Default'
# ]
profile_name = [
    'Profile 3', 'Profile 5', 'Profile 6',  'Profile 8'
]
# random.shuffle(profile_name)
# comments = get_comment_from_post(post_url=link_source,
#                                  cookies_profile=cookies_profile)
comments = ['Vãi ma =))', 'Hôm nay t cũng bị ma nhập tiếp']
for profile in profile_name:
    print('*************************' * 20 + "\n" + str(profile))
    print('test', profile[0])
    auto = AutoSeedingPostDetail(profile)
    driver = auto.open_profile()
    time.sleep(4)
    comments = auto.comment_post(comments, link_seeding)
    time.sleep(random.choice(range(200,300)))
    driver.close()
