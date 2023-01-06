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
        sleep_long()
        #FB hiện thông báo Bạn đang xem tin, nhấn enter để bỏ thông báo đó đi
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        sleep_short()
        try:
            #Click vào story đầu tiên:
            self.driver.find_element(
                By.XPATH,
                '//div[@class="x1g0ag68 xx6bhzk x11xpdln xcj1dhv x1ey2m1c x9f619 xds687c x10l6tqk x17qophe x13vifvy"]'
            ).click()
            sleep_long()
        except:
            # print("Không vào được xem story")
            pass
            
        tmp = 0
        #Chọn xem bao nhiêu story:
        num_watch_story = random.choice(range(4, 10))
        for _ in range(num_watch_story):
            tmp += 1
            print(self.username,'_____________', tmp)
            if random.choice(['reaction', 'no']) == 'reaction':
                reaction = choice_reaction()
                sleep_long()  #Xem story
                #Chọn reaction bao nhiêu lần
                for _ in range(random.choice(range(1, 7))):
                    print(self.username,'_________________________________ ', reaction)
                    try:
                        self.driver.find_element(
                            By.XPATH,
                            '//div[@aria-label="' + reaction + '"]').click()
                    except:
                        # print("Không tìm được element thả reaction")
                        pass
            sleep_short()
            try:
                self.driver.find_element(
                    By.XPATH, '//div[@aria-label="Nhóm tiếp theo"]').click()
                sleep_short()
            except:
                try:
                    self.driver.find_element(
                        By.XPATH, '//div[@aria-label="Thẻ tiếp theo"]').click()
                    sleep_short()
                except:
                    pass
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
            print(self.username,'__________________Lần xem post thứ: ', i)
            if (reaction == 'reaction') & (comment == 'comment') & (open_post
                                                                    == 'open'):
                # element1 = driver.switch_to.active_element
                # Func = open("tmp.html", "w", encoding="utf-8")
                # Func.write(element1.get_attribute('innerHTML'))
                # Func.close()
                # print('reaction + comment + open post')
                element.send_keys(Keys.ESCAPE + "j" + 'l' + Keys.ARROW_RIGHT *
                                  random.choice(range(1, 3)) + Keys.ENTER +
                                  'o')
            if (reaction == 'reaction') & (comment == 'comment') & (open_post
                                                                    != 'open'):
                # print('reaction + comment')
                element.send_keys(Keys.ESCAPE + "j" + 'l' + Keys.ARROW_RIGHT *
                                  random.choice(range(1, 3)))
            elif (reaction == 'reaction') & (comment != 'comment'):
                # print('reaction')
                element.send_keys(Keys.ESCAPE + "j" + 'l' + Keys.ARROW_RIGHT *
                                  random.choice(range(1, 3)) + Keys.ENTER)
                element = self.driver.find_element(By.TAG_NAME, "body")
            elif (reaction !=
                  'reaction') & (comment != 'comment') & (open_post == 'open'):
                # print('just open post')
                element.send_keys(Keys.ESCAPE +
                                  "j" * random.choice(range(1, 4)) + "o")
            elif (reaction !=
                  'reaction') & (comment != 'comment') & (open_post != 'open'):
                # print('no action')
                element.send_keys(Keys.ESCAPE +
                                  "j" * random.choice(range(1, 4)))
        return num_watch_post

    def add_friends(self, urls):
        s = 0
        it = random.choice(range(3, 5))
        random.shuffle(urls)
        num_add = 0
        while s<it:
            if (s>=len(urls)):
                break
            url = urls[s]
            s += 1
            print(self.username, 'Đã vào link: ', url)
            self.driver.get(url)
            sleep_very_long()
            self.driver.find_element(By.TAG_NAME, "body")
            sleep_short()
            elements_post = self.driver.find_elements(By.XPATH,
                                                      '//div[@class="_1g06"]')
            try:
                elements_post[0].click()
                sleep_short()
            except:
                pass
            try:
                self.driver.find_element(By.XPATH, '//div[@class="_1g06"]').click()
                sleep_short()
            except:
                pass
            for _ in range(10):
                try:
                    self.driver.find_element(
                        By.XPATH, '//a[@class="touchable primary"]').click()
                    sleep_long()
                except:
                    # print("Không nhấn vào được Xem thêm")
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
                    if (num_add >50):
                        break
                    element_addfriend.click()
                    sleep_short()
                    num_add += 1
                    print(self.username, f"Đã kết bạn với {num_add} người")
                except:
                    # print("Không click được vào element kết bạn")
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
        try:
            self.driver.find_element(
                By.XPATH, '//a[@class="_15ko _77li touchable"]').click()
            # print("Đã like post")
        except:
            pass
        sleep_long()
        # # Move to comment:
        # self.driver.find_element(
        #     By.XPATH, '/html/body/div[1]/div/div[4]/div/div[1]/div/div/footer/div/div/div[2]/a').click()
        # sleep_long()
        # Image
        if len(image_url) != 0:
            try:
                self.driver.find_element(
                    By.XPATH, '//input[@type="file"]').send_keys(image_url)
                sleep_very_long()
            except:
                self.driver.find_element(
                    By.XPATH, '//div[@class="_5s61 _2pii"]').send_keys(image_url)
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
        comment_box.send_keys(comment)
        sleep_short()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[@type="submit"]'))).click()
        sleep_short()
            
        check_dialog(self.driver)
        return comments

    def logout_fb(self):
        logout(self.driver)
        
class AutoCreateFanpage:
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

    def create_fanpage(self):
        self.driver.get("https://facebook.com/pages/?category=top&ref=bookmarks")
        time.sleep(2)
        # Nhấn tạo trang:
        self.driver.find_element(
            By.XPATH, '//div[@class="x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou x1hr4nm9 x1r1pt67"]').click()
        sleep_short()
        # Nhập tên trang
        element = self.driver.switch_to.active_element
        element.send_keys("Đây là tên page")
        sleep_short()
        element = self.driver.switch_to.active_element
        # Nhập hạng mục
        element.send_keys(Keys.TAB + Keys.TAB + "a")
        sleep_short()
        self.driver.find_element(
            By.XPATH, '//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x78zum5 x1a2a7pz xh8yej3"]').click()
        sleep_long()
        element = self.driver.switch_to.active_element
        
        # Nhấn tạo:
        WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//a[@aria-label="Tạo Trang"]'))).click()

    def logout_fb(self):
        logout(self.driver)