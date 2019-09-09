# github test

import math
import os
import random


import requests

mylist = [2, 109, False, 10, "Lorem", 482, "Ipsum"]

rnd = random.choice(mylist)


r = requests.get("https://google.com")
print(r.status_code)

