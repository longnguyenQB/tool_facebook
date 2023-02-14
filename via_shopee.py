from ToolAutoFB import AutoFB
import random
import json
import time
import os
from ultils import *
from threading import Thread


def autofb4multile(username, password):
    # Get url add friends
    f = open("./url_fb/url_LT.json", encoding="utf8")
    urls = json.load(f)
    urls = list(urls.values())
    #_______________________________
    start_time = time.time()
    print(frame("Login vào " + username, 1, 3))
    auto = AutoFB(username=username, password=password)
    driver = auto.open_profile()
    time.sleep(5)
    try:
        auto.login_fb()
    except:
        pass
    time.sleep(5)
    driver.get("https://shopee.vn/buyer/login")
    sleep_short()
    driver.find_element(
                By.XPATH,
                '//button[@class="nGTAZw lyJbNT bQ2eCN"]'
            ).click()
    sleep_short()
    driver.switch_to.window(driver.window_handles)
    time.sleep(5)
    driver.find_element(
                By.XPATH,
                '//div[@class="x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1fq8qgq"]'
            ).click()
    time.sleep(20)
    driver.switch_to.window(driver.window_handles)
    time.sleep(20)
    driver.get("https://shopee.vn/D%C3%A9p-quai-ngang-n%E1%BB%AF-Cross-Classic-Sandal-Crush-nhi%E1%BB%81u-m%C3%A0u-%C4%91%E1%BA%BF-cao-5cm-2-quai-g%E1%BA%AFn-Jib-d%E1%BB%85-th%C6%B0%C6%A1ng-S%E1%BA%A5u-vui-v%E1%BA%BB-Official-CSH-i.611799372.17627542170?sp_atk=796a4aa3-1525-4f52-8012-b7cb5d59cced&xptdk=796a4aa3-1525-4f52-8012-b7cb5d59cced")
    time.sleep(10)
    driver.find_element(
                By.XPATH,
                '//button[@class="IYjGwk"]'
            ).click()
    # driver.close()

def main():
    cwd = os.getcwd()
    # Get acc clone
    path_acc_clone = os.path.join(cwd, './acc_clone/acc_clone.txt')
    with open(path_acc_clone, 'r', encoding="utf8") as f:
            acc_clone = [word[:-1] for word in f]
    acc_clone = [acc_clone[i].split("|") for i in range(len(acc_clone))]
    threads = []

    session = []
    leng_session = (len(acc_clone) // 4) + 1 if len(acc_clone)%4 !=0 else len(acc_clone)/4

    for _ in range(int(leng_session)):
        session.append(acc_clone[:2])
        acc_clone = acc_clone[2:]
        
    for list_acc_clone in session:
        for i in range(len(list_acc_clone)):
            username , password = list_acc_clone[i][0], list_acc_clone[i][1]
            threads.append(Thread(target=autofb4multile, args=(username,
                                                            password,)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
if __name__ == "__main__":
    main()