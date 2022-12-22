from ToolAutoFB import AutoSeedingPostDetail
import random
import json
import os
import time
link_seeding = 'https://www.facebook.com/groups/genzlethuy/posts/1092292301440556/'

cookies_profiles = []
for root, dirs, files in os.walk("./Cookies"):
    for file in files:
        if file.endswith(".txt"):
            with open(os.path.join(root, file), 'r') as f:
                cookies_profiles.append(json.load(f.read))

with open('./comment_sample.txt', 'r', encoding="utf8") as f:
        comments = [word[:-1] for word in f]
profile_name = []
for profile in profile_name:
    print('*************************' * 20 + "\n" + str(profile))
    auto = AutoSeedingPostDetail(profile)
    driver = auto.open_profile()
    time.sleep(4)
    comments = auto.comment_post(comments, link_seeding)
    time.sleep(random.choice(range(200,300)))
    driver.close()
