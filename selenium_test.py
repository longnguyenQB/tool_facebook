from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json

def launchBrowser(profile_name):
    chrome_options = Options()
    #    chrome_options.add_argument("user-data-dir=C:/Users/GroooDev/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_argument("user-data-dir=C:/Users/ADMIN/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--profile-directory="+ profile_name)
    chrome_options.add_argument("--window-size=500,500")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://www.facebook.com/")
    return driver
def choice_reaction():
    list_reaction = ['Thích', 'Yêu thích', 'Thương thương']
    return random.choice(list_reaction)
def sleep_very_short():
    return time.sleep(random.choice(numpy.arange(0.1,1,0.2)))
def sleep_short():
    return time.sleep(random.choice(range(2,5)))
def sleep_long():
    return time.sleep(random.choice(range(4,7)))
def sleep_very_long():
    return time.sleep(random.choice(range(8,20)))
class AutoFB:
    def __init__(self, profile_name):
        super().__init__()
        self.profile_name = profile_name
    def open_profile(self):
        profile = launchBrowser(self.profile_name)
        self.driver = profile
    def watch_story(self):
        #Click vào story đầu tiên:
        self.driver.find_element(By.XPATH, '//div[@class="x1g0ag68 xx6bhzk x11xpdln xcj1dhv x1ey2m1c x9f619 xds687c x10l6tqk x17qophe x13vifvy"]').click()
        tmp = 0
        #Chọn xem bao nhiêu story:
        for _ in range(random.choice(range(3,8))): 
            tmp +=1
            print('_____________',tmp)
            if random.choice(['reaction', 'no']) == 'reaction':
                reaction = choice_reaction()
                sleep_long() #Xem story
                #Chọn reaction bao nhiêu lần
                for _ in range(random.choice(range(1,5))): 
                    print('_________________________________ ', reaction)
                    try:
                        self.driver.find_element(By.XPATH, '//div[@aria-label="' + reaction + '"]').click()
                    except:
                        pass
            sleep_short()
            try:
                self.driver.find_element(By.XPATH, '//div[@aria-label="Nhóm tiếp theo"]').click()
                sleep_short()
            except:
                self.driver.find_element(By.XPATH, '//div[@aria-label="Thẻ tiếp theo"]').click()
                sleep_short()
        self.driver.get("http://www.facebook.com/")
    def watch_post(self):
        element = self.driver.find_element(By.TAG_NAME,"body")
        # Chọn số lần xem post
        for i in range(0,random.choice(range(10,20))):
            reaction = random.choice(['reaction', 'no'])
            comment = random.choice(['comment', 'no', '1', '2', '3'])
            open_post = random.choice(['open', 'no'])
            sleep_very_long()
            print('__________________Lần xem post thứ: ',i)
            if (reaction == 'reaction') & (comment == 'comment') & (open_post == 'open'):
                # element1 = driver.switch_to.active_element
                print('reaction + comment + open post')
                element.send_keys(Keys.ESCAPE + "j" + 'l' + Keys.ARROW_RIGHT*random.choice(range(1,3)) + Keys.ENTER + 'o')
            if (reaction == 'reaction') & (comment == 'comment') & (open_post != 'open'):
                print('reaction + comment')
                element.send_keys(Keys.ESCAPE + "j" + 'l' + Keys.ARROW_RIGHT*random.choice(range(1,3)))
            elif (reaction == 'reaction') & (comment != 'comment'):
                print('reaction')
                element.send_keys(Keys.ESCAPE + "j" + 'l' + Keys.ARROW_RIGHT*random.choice(range(1,3)) + Keys.ENTER)
                element = self.driver.find_element(By.TAG_NAME,"body")
            elif (reaction != 'reaction') & (comment != 'comment') & (open_post == 'open'):
                print('just open post')
                element.send_keys(Keys.ESCAPE + "j"*random.choice(range(1,4)) + "o")
            elif (reaction != 'reaction') & (comment != 'comment') & (open_post != 'open'):
                print('no action')
                element.send_keys(Keys.ESCAPE + "j"*random.choice(range(1,4)))
    def add_friends(self):
        f = open("./url_fb/url.json", encoding="utf8")
        data = json.load(f)
        for url in data.values():       
            self.driver.get(url)
            element = self.driver.find_element(By.TAG_NAME,"body")
            element.send_keys("j")
            try:
                self.driver.find_element(By.XPATH, '//div[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1n2onr6 x87ps6o x1lku1pv x1a2a7pz x1heor9g xnl1qt8 x6ikm8r x10wlt62 x1vjfegm x1lliihq"]').click()
            except:
                self.driver.find_element(By.XPATH, '//div[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1n2onr6 x87ps6o x1lku1pv x1a2a7pz x1heor9g xnl1qt8 x6ikm8r x10wlt62 x1vjfegm x78zum5"]').click()
            sleep_short()
            elements = self.driver.find_elements(By.XPATH, '//*[@aria-label="Thêm bạn bè"]')
            for elem in elements:
                try:
                    elem.click()
                except:
                    pass
                sleep_short()
tmp = AutoFB('Profile 3')
tmp.open_profile()  
time.sleep(4)
# tmp.watch_story()  
# tmp.watch_post() 
tmp.add_friends()