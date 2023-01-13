from ToolAutoFB import AutoSeedingPostDetail
import os
from os import startfile, getcwd
import random
import json
import time

# cookies_profiles = []
# for root, dirs, files in os.walk("./Cookies"):
#     for file in files:
#         if file.endswith(".txt"):
#             with open(os.path.join(root, file), 'r') as f:
#                 cookies_profiles.append(json.load(f.read))

def main():
    cwd = os.getcwd()
    # Get acc clone
    path_acc_clone = os.path.join(cwd, './acc_clone/acc_clone.txt')
    with open(path_acc_clone, 'r', encoding="utf8") as f:
            acc_clone = [word[:-1] for word in f]
    acc_clone = [acc_clone[i].split("|") for i in range(len(acc_clone))]

    # Get list comment sample
    path_comment_sample = os.path.join(cwd, "./comment_sample.txt")
    with open(path_comment_sample, 'r', encoding="utf8") as f:
            comments = [word[:-1] for word in f]

    # Get url seeding
    path_url_seeding = os.path.join(cwd, "./url_seeding.txt")  
    with open(path_url_seeding, 'r', encoding="utf8") as f:
            link_seedings = [word[:-1] for word in f]


    image_url = ""


    for acc in acc_clone:
        start_time = time.time()
        username , password = acc[0], acc[1]
        auto = AutoSeedingPostDetail(username = username,
                    password = password)
        driver = auto.open_profile()
        try:
            auto.login_fb()
        except:
            pass
        time.sleep(4)
        for link_seeding in link_seedings:
            comments = auto.comment_post(link_seeding, comments, image_url)
        time.sleep(random.choice(range(100,200)))
        driver.close()
