import mysql.connector
from mysql.connector import Error


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
            