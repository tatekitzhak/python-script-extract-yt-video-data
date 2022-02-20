import datetime


def make_bucket():

	time_now = datetime.datetime.now()
	year = '{:02d}'.format(time_now.year)
	month = '{:02d}'.format(time_now.month)
	day = '{:02d}'.format(time_now.day)
	hour = '{:02d}'.format(time_now.hour)
	minute = '{:02d}'.format(time_now.minute)

	current_time = '{}-{}-{}T{}'.format(year, month, day, hour)
	print('day_month_year: ' + current_time)


make_bucket()