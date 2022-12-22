from facebook_scraper import get_posts
import pickle
def get_post(post_urls, cookies_profile):
    post_list = []
    for post in get_posts(
                            post_urls=[post_urls],
                            options={
                                "comments": True,
                                "reactions": True
                            },
                            cookies=cookies_profile
                            ):
        post_list.append(post)
    list_comment = [post_list[0]['comments_full'][i]['comment_text'] for i in range(len(post_list[0]['comments_full']))]
    list_commenter_url = [post_list[0]['comments_full'][i]['commenter_url'] for i in range(len(post_list[0]['comments_full']))]
    with open("post_in4", "wb") as fp:   #Pickling
        pickle.dump(post_list, fp)
    return post_list, list_comment, list_commenter_url
post_urls = "https://www.facebook.com/UTE.Confession/posts/524410909725732"
cookies_profile = "./Cookies/facebook.com_cookies.txt"
get_post(post_urls, cookies_profile)