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
        list_of_names = ['Fred', 'Bob']
        # Prepare the string with the same number of
        # placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
