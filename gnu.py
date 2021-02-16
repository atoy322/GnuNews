import re

import requests

from color import cprint


URL = "https://kinggnu.jp/news"
PATTERN_STRING = '<a class="news-archive-preview__StyledLink-sc-19ik15e-1 cwSwjn".+?</a>'




def GetNews():
    """
    サイトからニュースを取得してリストで返す。
    """
    page = requests.get(URL).content.decode()
    found_list = re.findall(PATTERN_STRING, page)
    news_list = map(lambda x: re.sub("<.+?>", "", x), found_list)  # "<h1>Hello</h1>" -> "Hello"
    return list(news_list)



if __name__ == "__main__":
    color_table = {
        "「.+」": "CYAN",
        "[0-9]+?月[0-9]+?日": "GREEN",
        "常田大希|井口理|新井和輝|勢喜遊": "YELLOW"
    }  # Pattern: Color
    LIGHTBLACK = "\x1b[100m"  # background color
    END = "\x1b[49m"

    news_list = GetNews()

    for idx, i in enumerate(news_list):
        if idx % 2: l = r = ""
        else: l, r = LIGHTBLACK, END
        cprint(l+"◦ "+i+r, color_table=color_table)
