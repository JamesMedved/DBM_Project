from multiprocessing.dummy import Pool as Threadpool
from requests_html import HTMLSession
from DBSM import DBSM

def get_images(response):
    for item in response:
        if item[2] == 'Movie':
            url = f"{root}m/{item[1].replace(' ', '_').replace('&', 'and').replace(':','').replace(',','').replace('!','').replace('+','')}"
            url = url.replace('\'','')
        else:
            url = f"{root}tv/{item[1].replace(' ', '_').replace('&', 'and').replace(':','').replace(',','').replace('!','').replace('+','')}"
            url = url.replace('\'','')
        print(f'\n\n{url}')
        r = s.get(url)
        r.html.render(sleep=1)
        image = r.html.find('img.posterImage', first=True)
        try:
            q = f"update titles set image = '{image.attrs['src']}' where title_id = {item[0]}"
            response = db.send_query(q)
            db.connection.commit()
        except Exception as e:
            print(e)
            url = url + f"_{item[3]}"
            print(f'\n\n{url}')
            r = s.get(url)
            r.html.render(sleep=1)
            image = r.html.find('img.posterImage', first=True)
            try:
                q = f"update titles set image = '{image.attrs['src']}' where title_id = {item[0]}"
                response = db.send_query(q)
                db.connection.commit()
            except Exception as e:
                print(e)

s = HTMLSession()
db = DBSM()
root = "https://www.rottentomatoes.com/"
response = db.send_query("select title_id, name, type, release_year from titles where image is null and title_id > 1000")
get_images(response)