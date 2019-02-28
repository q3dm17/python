# utf-8
# coding=utf-8

import requests
import re

finder = re.compile("\d+!")


def step(left):
    response = requests.get("http://long.training.hackerdom.ru/", headers={"Range": "bytes={}-{}".format(left, left+150)})
    text = response.text
    found = finder.findall(text)
    if len(found) != 1:
        print text
    else:
        next_left = int(found[0][:-1])
        step(next_left)

step(8840)
