import mysql.connector
from mysql.connector import errorcode

try:
    dbConnection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Brasil101@',
        database='DB_EMPRESA'
    )
    print("Database connection made!")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is wrong")
    else:
        print(error)
else:
    dbConnection.close()
