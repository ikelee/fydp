import pymysql
import pymysql.cursors

try:
    connection = pymysql.connect(user="root", password="password",
                            host="127.0.0.1",
                            database="IMPACT")
    cursor = connection.cursor()
except pymysql.InternalError as error:
    print("Connection Failed")
    print(error)