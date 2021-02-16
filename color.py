import re

from colorama import init, Fore, Back, Style

init()


def cprint(text, color_table, **kwargs):
    for pattern in color_table.keys():
        frcolor_name = color_table[pattern]
        frcolor_cmd = Fore.__getattribute__(frcolor_name)
        matched_list = re.findall(pattern, text, re.DOTALL)

        for i in matched_list:
            text = text.replace(i, frcolor_cmd+i+Fore.RESET)
        
    print(text, **kwargs)
