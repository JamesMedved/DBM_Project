from DBSM import DBSM


def search_by_title(db, title_string):
    response = db.send_query(f'select * from disney where title like "%{title_string}%"')
    if not response:
        print("No results found.")
    return response

def get_hulu_links(db):
    response = db.send_query("select * from hulu")
    for item in response:
        if item[1] == "TV Show":
            link = "https://www.hulu.com/series/"
        if item[1] == "Movie":
            link = "https://www.hulu.com/movie/"
        print(f"{link}{item[2].replace(' ', '-')}")

def get_netflix_links(db):
    response = db.send_query("select * from netflix")
    for item in response:
        print(f"https://www.netflix.com/search?q={item[2].replace(' ', '%20')}")

def get_prime_links(db):
    response = db.send_query("select * from prime")
    for item in response:
        print(f"https://www.amazon.com/s?k={item[2].replace(' ', '+')}&i=instant-video")

def get_disney_links(db):
    response = db.send_query("select * from disney")
    for item in response:
        if item[1] == "TV Show":
            link = "https://www.disneyplus.com/series/"
        if item[1] == "Movie":
            link = "https://www.disneyplus.com/movies/"
        print(f"{link}{item[2].replace(' ', '-')}")

db = DBSM()
get_disney_links(db)
db.end_connection()

