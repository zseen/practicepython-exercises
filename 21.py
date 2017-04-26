import requests
from bs4 import BeautifulSoup

url = 'http://github.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")

open_file=open('url', 'w')
open_file.write(r.text)
open_file.close()


