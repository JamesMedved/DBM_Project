# import requests
# from bs4 import BeautifulSoup

# root = "https://www.google.com/search?q="
# title = "star%20wars%20rougue%20one"

# url = root + title

# result = requests.get(url)
# doc = BeautifulSoup(result.text, "html.parser")

# img = doc.find_all(class_="kAOS0")
# print(img)

from requests_html import HTMLSession

s = HTMLSession()

root = "https://www.google.com/search?q="
title = "star%20wars%20rougue%20one"

url = root + title

r = s.get(url)

r.html.render(sleep=1)

image = r.html.find('img.kAOS0', first=True)
print(image)
