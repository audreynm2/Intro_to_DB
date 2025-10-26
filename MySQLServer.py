import mysql.connector

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""    
    )

    if connection.is_connected():
        cursor = connection.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")


except mysql.connector.Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    try:
        cursor.close()
        connection.close()
    except:
        pass
