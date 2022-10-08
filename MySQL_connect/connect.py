import mysql.connector
from mysql.connector import Error

# Have to install MySQL connector in order to run. Line to execute in command line:
# pip install mysql-connector-python

try:
    connection = mysql.connector.connect(host = 'localhost',
                                        database = 'dbsmproject',
                                        user = 'root',
                                        password = 'JimmyLikesBoys123!')
    if connection.is_connected():   # Connection successful
        # Grabbing server info. Verifies we are connected to the right database
        db_Info = connection.get_server_info()
        print ("Connected to MySQL Server version ", db_Info)

        # Basic query build up
        MySQL_Query = ("SELECT * FROM disney")

        cursor = connection.cursor()

        cursor.execute(MySQL_Query)
        result = cursor.fetchall()
        print("Results from query", result)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")