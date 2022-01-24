import mysql.connector
from mysql.connector import Error
import os, errno

def make_dir_folder(name):
	path= '/Users/eli/git_repos/python-script-extract-yt-video-data/'+name

	# Check whether the specified path exists or not
	path_isExist = os.path.exists(path)
	print('IsExis a tpath : ',path_isExist)

	if not path_isExist:
	  
	  # Create a new directory because it does not exist 
	    try:
	        os.makedirs(path)
	        print("The new directory is created =>", name)
	    except OSError as e:
	        if e.errno != errno.EEXIST:
	            raise

def create_foders():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='db_test1',
                                             user='ran',
                                             password='ran')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            
        sql_select_Query = "select * from topics"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\n Table data: ",records)
        for row in records:
            # print("Rows = ", row[1] )
            make_dir_folder(row[1])
            print('__________________')

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

create_foders()
