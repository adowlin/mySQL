import os
import pymysql

# Get username from workspace
username = os.getenv('C9_USER')

# Connect to database
connection = pymysql.connect(host='localhost',
                            user=username, password='', db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", "Bob")
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
