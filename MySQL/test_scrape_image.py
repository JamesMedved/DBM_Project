import requests
from bs4 import BeautifulSoup
import re

type = 'Movie'
name = ''
name = re.sub('\s+', '_', name)
name = re.sub('[\W_]+', '', name)

if type == 'Movie':
    rt_link = f"https://www.rottentomatoes.com/m/{name}"
else:
    rt_link = f"https://www.rottentomatoes.com/tv/{name}"

try:
    page = requests.get(rt_link)
    soup = BeautifulSoup(page.text, 'lxml')
    img_link = soup.find_all('img', class_="posterImage")[0]['src']
    print(img_link)
except:
    pass