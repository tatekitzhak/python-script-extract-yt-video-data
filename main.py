import convert_tuple_into_json
import mysql_connection

def main():
	print('Response processing module:', convert_tuple_into_json.main(mysql_connection.main()))


main()