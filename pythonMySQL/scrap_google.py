from multiprocessing.dummy import Pool as Threadpool
from requests_html import HTMLSession
from DBSM import DBSM

def get_images(response):
    for item in response:
        if item[2] == 'Movie':
            url = f"{root}{item[1].replace(' ', '%20').replace('&', 'and').replace(':','').replace(',','').replace('!','').replace('+','').replace('-','')}%20Movie"
        else:
            url = f"{root}{item[1].replace(' ', '%20').replace('&', 'and').replace(':','').replace(',','').replace('!','').replace('+','').replace('-','')}%20Tv%20Show"
        print(f'\n\n{url}')
        r = s.get(url)
        r.html.render(sleep=1)
        image = r.html.find('img.kAOS0', first=True)
        try:
            q = f"update titles set image = '{image.attrs['src']}' where title_id = {item[0]}"
            response = db.send_query(q)
            db.connection.commit()
        except Exception as e:
            print(e)
            url = f"{root}{item[1].replace(' ', '%20').replace('&', 'and')}"
            print(f'\n\n{url}')
            r = s.get(url)
            r.html.render(sleep=1)
            image = r.html.find('img.kAOS0', first=True)
            try:
                q = f"update titles set image = '{image.attrs['src']}' where title_id = {item[0]}"
                response = db.send_query(q)
                db.connection.commit()
            except Exception as e:
                print(e)
    

s = HTMLSession()
db = DBSM()
root = "https://www.google.com/search?q="
response = db.send_query("select title_id, name, type from titles where image is null")
get_images(response)