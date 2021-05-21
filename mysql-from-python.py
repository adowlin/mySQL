import os
import datetime
import pymysql

# Get username from workspace
username = os.getenv('C9_USER')

# Connect to database
connection = pymysql.connect(host='localhost',
                            user=username, password='', db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'),
                (24, 'Jim'),
                (25, 'Fred')]
        cursor.executemany("UPDATE Friends SET age = %s where name = %s;",
                        rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
