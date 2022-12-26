from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from ultils import *
import time
import random
import json


class AutoFB:
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def open_profile(self):
        profile = launchBrowser()
        self.driver = profile
        return self.driver

    def login_fb(self):
        login(self.driver, self.username, self.password)

    def watch_story(self):
        self.driver.get("https://facebook.com/")
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
        self.driver.get("https://facebook.com/")
        return num_watch_story

    def watch_post(self):
        self.driver.get("https://facebook.com/")
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
        while (num_add <= 50):
            url = urls[s]
            s += 1
            print('Đã vào link: ', url)
            self.driver.get(url)
            sleep_very_long()
            self.driver.find_element(By.TAG_NAME, "body")
            sleep_short()
            elements_post = self.driver.find_elements(By.XPATH,
                                                      '//div[@class="_1g06"]')
            elements_post[0].click()
            sleep_short()
            self.driver.find_element(By.XPATH, '//div[@class="_1g06"]').click()
            sleep_short()
            for _ in range(10):
                try:
                    self.driver.find_element(
                        By.XPATH, '//div[@class="title mfsm fcl"]').click()
                except:
                    pass
            self.driver.execute_script(
                "document.getElementsByClassName('_54k8 _52jg _56bs _26vk _8yzt _56bu')[0];"
            )
            elements_addfriend = self.driver.find_elements(
                By.XPATH,
                '//button[@class="_54k8 _52jg _56bs _26vk _8yzt _56bu"]')
            sleep_short()
            print(len(elements_addfriend))
            for element_addfriend in elements_addfriend:
                try:
                    element_addfriend.click()
                    sleep_short()
                    num_add += 1
                    print(f"Đã kết bạn với {num_add} người")
                except:
                    pass
            urls.remove(url)
        return urls, num_add, it

    def logout_fb(self):
        logout(self.driver)


class AutoSeedingPostDetail:
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def open_profile(self):
        profile = launchBrowser()
        self.driver = profile
        return self.driver

    def login_fb(self):
        login(self.driver, self.username, self.password)

    def comment_post(self, link_seeding, comments, image_url):
        self.driver.get(link_seeding)
        time.sleep(2)
        # Like:
        self.driver.find_element(
            By.XPATH, '//a[@class="_15ko _77li touchable"]').click()
        sleep_long()
        # Move to comment:
        self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div/div/footer/div/div/div[2]/a').click()
        sleep_long()
        # Image
        if len(image_url) != 0:
            try:
                self.driver.find_element(
                    By.XPATH, '//a[@class="_5ecn"]').send_keys(image_url)
                sleep_very_long()
            except:
                self.driver.find_element(
                    By.XPATH, '//a[@class="_5s61 _2pii"]').send_keys(image_url)
                sleep_very_long()
        try:
            comment_box = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//textarea[@class="_uwx mentions-input"]')))
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

    def logout_fb(self):
        logout(self.driver)