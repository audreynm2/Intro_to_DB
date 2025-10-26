import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # CREATE DATABASE (checker expects alxbookstore)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
        print("Database 'alxbookstore' created successfully!")

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
