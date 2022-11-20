import mysql.connector
from mysql.connector import Error
import requests
from bs4 import BeautifulSoup
import re


class DBSM:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host = 'localhost',
                                                database = 'dbm_prj',
                                                user = 'root',
                                                password = 'RooT1234@@')
            if self.connection.is_connected():   # Connection successful
                self.cursor = self.connection.cursor()
                # Grabbing server info. Verifies we are connected to the right database
                db_Info = self.connection.get_server_info()
                print ("Connected to MySQL Server version ", db_Info)
        except Error as e:
            print("Error while connecting to MySQL", e)

    def end_connection(self):
        if self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("MySQL connection is closed")

    def send_query(self, query):
        # Basic query build up
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_img_link(self):
        titles = self.send_query("select * from titles")
        for title in titles:
            type = 'Movie'
            name = title[1]
            name = re.sub('\s+', '_', name)
            name = re.sub(':', '', name)
            name = re.sub('&', 'and', name)
            name = name.lower()
            print(title[1])
            print(name)

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

