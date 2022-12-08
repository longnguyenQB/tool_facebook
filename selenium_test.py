from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

def launchBrowser(profile_name):
   chrome_options = Options()
   chrome_options.add_argument("user-data-dir=C:/Users/GroooDev/AppData/Local/Google/Chrome/User Data")
   chrome_options.add_argument("disable-infobars");
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
        self.device = profile
    def watch_story(self):
        #Click vào story đầu tiên:
        self.device.find_element(By.XPATH, '//div[@class="x1g0ag68 xx6bhzk x11xpdln xcj1dhv x1ey2m1c x9f619 xds687c x10l6tqk x17qophe x13vifvy"]').click()
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
                        self.device.find_element(By.XPATH, '//div[@aria-label="' + reaction + '"]').click()
                    except:
                        pass
            sleep_short()
            try:
                self.device.find_element(By.XPATH, '//div[@aria-label="Nhóm tiếp theo"]').click()
                sleep_short()
            except:
                self.device.find_element(By.XPATH, '//div[@aria-label="Thẻ tiếp theo"]').click()
                sleep_short()
        self.device.get("http://www.facebook.com/")
tmp = AutoFB('Profile 3')
tmp.open_profile()  
time.sleep(2)
tmp.watch_story()   

