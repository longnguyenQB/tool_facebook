from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from facebook_scraper import get_posts
import time
import random
import numpy
import re


def launchBrowser():
    chrome_options = Options()
    chrome_options.add_argument(
        "user-data-dir=C:/Users/GroooDev/AppData/Local/Google/Chrome/User Data"
    )
    # chrome_options.add_argument(
    #     "user-data-dir=C:/Users/ADMIN/AppData/Local/Google/Chrome/User Data")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--profile-directory=" + profile_name )
    chrome_options.add_argument("--window-size=700,700")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://touch.facebook.com/")
    return driver


def login(driver, username, password):
    driver.find_element(By.XPATH,
                        '//input[@id="m_login_email"]').send_keys(username)
    sleep_short()
    driver.find_element(By.XPATH,
                        '//input[@id="m_login_password"]').send_keys(password)
    sleep_short()
    driver.find_element(By.XPATH, '//button[@value="Log In"]').click()
    sleep_long()
    driver.get("https://touch.facebook.com/")


def logout(driver):
    driver.get("https://touch.facebook.com/")
    time.sleep(5)
    driver.find_element(
        By.XPATH, '//div[@class="_59te jewel _hzb noCount _4wrj"]').click()
    sleep_long()
    driver.find_element(
        By.XPATH,
        '/html/body/div[1]/div/div[4]/div/div/div/div[5]/a/div').click()
    try:
        driver.find_element(
            By.XPATH,
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/a[1]/div/div[2]'
        ).click()
        print("Đã log out!")
        sleep_long()
    except:
        pass


def choice_reaction():
    list_reaction = ['Thích', 'Yêu thích', 'Thương thương']
    return random.choice(list_reaction)


def sleep_very_short():
    return time.sleep(random.choice(numpy.arange(0.1, 1, 0.2)))


def sleep_short():
    return time.sleep(random.choice(range(2, 5)))


def sleep_long():
    return time.sleep(random.choice(range(4, 7)))


def sleep_very_long():
    return time.sleep(random.choice(range(8, 20)))


def sleep_very_very_long():
    return time.sleep(random.choice(range(20, 60)))


def get_comment_from_post(post_url, cookies_profile):
    post_list = []
    for post in get_posts(post_urls=[post_url],
                          options={
                              "comments": True,
                              "reactions": True
                          },
                          cookies=cookies_profile):
        post_list.append(post)
    list_comment = [
        post_list[0]['comments_full'][i]['comment_text']
        for i in range(len(post_list[0]['comments_full']))
    ]
    with open('./name_vn.txt', 'r', encoding="utf8") as f:
        names = [word[:-1] for word in f]
    pattern1 = '|'.join([r"\b" + name + r"\b" for name in names])
    list_comment = [
        comment for comment in pattern1
        if not re.search(pattern1, comment.lower())
    ]
    return list_comment


def check_dialog(driver):
    try:
        driver.switch_to.active_element
        element = driver.find_element(By.XPATH, '//div[@role="dialog"]')
        time.sleep(2)
        element.send_keys(Keys.ESCAPE)
        time.sleep(2)
        print('Bỏ qua dialog')
    except:
        pass