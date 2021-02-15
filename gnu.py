import re

import requests
import colorama
from termcolor import cprint


colorama.init()


URL = "https://kinggnu.jp/news"
PATTERN_STRING = '<a class="news-archive-preview__StyledLink-sc-19ik15e-1 cwSwjn".+?</a>'


def colored_print(pattern, color, text, default="white", background="grey"):
    match_objects = list(re.finditer(pattern, text))
    now_color = default

    for idx, char in enumerate(text):
        for match_object in match_objects:
            if idx == match_object.start():
                now_color = color
            elif idx == match_object.end():
                now_color = default
        
        cprint(char, now_color, "on_" + background, end="")
    
    print()


def GetNews():
    page = requests.get(URL).content.decode()
    found_list = re.findall(PATTERN_STRING, page)
    news_list = map(lambda x: re.sub("<.+?>", "", x), found_list)  # "<h1>Hello</h1>" -> "Hello"
    return list(news_list)




if __name__ == "__main__":
    news_list = GetNews()

    for i in news_list:
        colored_print("「.+」", "cyan", "◦ "+i)
