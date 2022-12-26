from ToolAutoFB import AutoSeedingPostDetail
import random
import json
import os
import time

# cookies_profiles = []
# for root, dirs, files in os.walk("./Cookies"):
#     for file in files:
#         if file.endswith(".txt"):
#             with open(os.path.join(root, file), 'r') as f:
#                 cookies_profiles.append(json.load(f.read))

# Get url seeding link
f = open("./url_fb/url_LT.json", encoding="utf8")
url_LT = json.load(f)
link_seedings = list(url_LT.values())
link_seedings = ['https://touch.facebook.com/groups/genzlethuy/posts/1099538864049233']

with open('./comment_sample.txt', 'r', encoding="utf8") as f:
        comments = [word[:-1] for word in f]
image_url = "C:/Users/GroooDev/Desktop/meme/2f1a895b81fafd8c9f6f1a5848f08a5310-diem-khanh-banh-khoe-10-ngon-tay.jpg"
# Get account clone
f = open("./acc_clone/acc_clone.json", encoding="utf8")
profile = json.load(f)

for key in profile.keys():
    start_time = time.time()
    username , password = key, profile.get(key)
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
        time.sleep(random.choice(range(200,300)))
        driver.close()
