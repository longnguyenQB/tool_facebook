from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from ultils import *
import time
import random
import json


def launchBrowser_zalo():
    chrome_options = Options()
    # chrome_options.add_argument(
    #     "user-data-dir=C:/Users/GroooDev/AppData/Local/Google/Chrome/User Data"
    # )
    chrome_options.add_argument(
        "user-data-dir=C:/Users/ADMIN/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--profile-directory=" + "Profile 3")
    chrome_options.add_argument("--window-size=700,700")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://chat.zalo.me/")
    return driver


texts1 = ['ê mi hủy kb t à? răng t nt ko được hè?',
          'hủy kb t à m? răng tìm zalo m k thấy nửa?',
          'bạn iu ơi hủy kb t à?',
          'alo bạn iu răng hủy kb rứa?',
          'zalo bị răng mà tự nhiên ko thấy m nửa',
          'ê zalo bị răng à? tự nhiên hủy kb rứa?',
          'tự nhiên hủy kết bạn tau rứa mi?',
          'ủa răng hủy kb?',
          'vì răng hủy kb t à?',
          'hủy kb t à hay răng ko tìm được m?',
          'zalo bị ngáo à, răng hủy kb t rứa?',
          'ơ tự nhiên hủy kb t rứa?',
          'ủa tự nhiên hủy kb r?',
          'ê mày hủy kb t à? sao t nt ko được hè?',
          'hủy kb t à m? sao tìm zalo m k thấy nửa?',
          'bạn iu ơi hủy kb t à?',
          'alo bạn iu sao hủy kb thế?',
          'zalo bị sao mà tự nhiên ko thấy m nửa',
          'ê zalo bị sao à? tự nhiên hủy kb thế?',
          'tự nhiên hủy kết bạn tau thế mày?',
          'ủa sao hủy kb?',
          'vì sao hủy kb t à?',
          'hủy kb t à hay sao ko tìm được m?',
          'zalo bị ngáo à, sao hủy kb t thế?',
          'ơ tự nhiên hủy kb t thế?',
          'ủa tự nhiên hủy kb r?']
with open("spam_zalo.txt", 'r', encoding="utf8") as f:
    texts2 = [word[:-1] for word in f]
with open("phone_1tr.txt", 'r', encoding="utf8") as f:
    phones = [word[:-1] for word in f]
with open("aff_url.txt", 'r', encoding="utf8") as f:
    aff_url = [word[:-1] for word in f]
icon = [
    ":b ", "b-) ", ":') ", ":d ", ":-(( ", "/-heart ", "_()_ ", ":-bye ", ":v "]


class AutoZalo:
    def __init__(self, phones, texts1, texts2, aff_url):
        super().__init__()
        self.phones = phones
        self.texts1 = texts1
        self.texts2 = texts2
        self.aff_url = aff_url

    def open_profile(self):
        profile = launchBrowser_zalo()
        self.driver = profile
        return self.driver

    def spam(self):
        count = 0
        phone_nothave_zalo = []
        for phone in self.phones:
            self.driver.get("https://chat.zalo.me/")
            sleep_long()
            try:
                self.driver.find_element(
                    By.XPATH, '//input[@id="contact-search-input"]').send_keys(phone)
                sleep_short()
                self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                sleep_short()

                # Add friends
                self.driver.find_element(
                    By.XPATH, '//div[@data-id="btn_Chat_AddFrd"]').click()
                sleep_short()
                self.driver.switch_to.active_element.send_keys(Keys.ENTER)

                # Send text
                self.driver.find_element(
                    By.XPATH, '//div[@class="chat-input__content"]').click()
                sleep_short()
                modau = random.choice(self.texts1) + " " + \
                    random.choice(icon)
                self.driver.switch_to.active_element.send_keys(modau)
                sleep_short()
                self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                sleep_short()

                mua = random.choice(self.texts2) + " " + \
                    random.choice(icon)

                self.driver.switch_to.active_element.send_keys(mua)
                sleep_short()
                
                self.driver.switch_to.active_element.send_keys(Keys.ENTER)
                sleep_short()
                
                url = random.choice(self.aff_url)
                self.driver.switch_to.active_element.send_keys(
                    url)
                sleep_short()
                
                self.driver.switch_to.active_element.send_keys(Keys.ENTER)


                print("Nhắn phone: ", phone)
                print(modau)
                print(mua)
                print(url)
                sleep_very_very_long()
            except:
                print("Không nhắn được số ", phone)
                phone_nothave_zalo.append(phone)
                pass
            count += 1
            print(count)
        return phone_nothave_zalo


auto = AutoZalo(phones=phones[100:],
                texts1=texts1,
                texts2=texts2,
                aff_url=aff_url)
auto.open_profile()
sleep_long()
phone_nothave_zalo = auto.spam()
with open('phone_nothave_zalo.txt', 'w') as f:
    for line in phone_nothave_zalo:
        f.write(f"{line}\n")
