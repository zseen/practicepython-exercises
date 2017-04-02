import requests
from bs4 import BeautifulSoup
import re

url = 'http://github.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)


# for tag in soup.find_all(True):
#     print(tag.name)

for tag in soup.find_all(re.compile("t")):
    print(tag.name)