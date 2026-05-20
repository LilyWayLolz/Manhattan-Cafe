import json
import random
import lxml
from bs4 import BeautifulSoup

with open("config.json", "r") as f:
    config = json.load(f)

cafes = "https://safebooru.org/index.php?page=post&s=list&limit=1000&json=1&tags=manhattan_cafe_%28umamusume%29+"
cafes_str = json.dumps(cafes)
with open("cafes.json", "w") as f:
    f.write(cafes_str)
with open("cafes.json", "r") as f:
    replies = json.load(f)

for i in replies:
    i = 0
    if i < 10:
        random_index = random.randint(0, len(replies) - 1)
        print (replies[random_index])
        i += 1