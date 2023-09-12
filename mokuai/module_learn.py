import math
import random
import _json
import sys, os
import requests


def hello(name):
    print("hello ", name)


username = "阿三"

# print(math.pow(2, 3))

# print(random.randint(0, 100))

print(requests.get("http://www.baidu.com").status_code)
