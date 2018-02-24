import numpy as np

dates = ['2016-02-23 09:36:26', '2016-02-23 09:36:26', '2016-02-23 09:36:26']

# assuming dates are passed as [yyyy-mm-dd hh:mm:ss]
def isOutdated(otherDates, currentDate):
	outdatedFrom = np.timedelta64(5, 'Y')
	thisDate = np.datetime64(currentDate, 'Y')

	print(thisDate)
	mean = (np.array(otherDates, dtype='datetime64[Y]')
        .view('i8')
        .mean()
        .astype('datetime64[Y]'))
	thisDate = np.datetime64(currentDate)

	if(thisDate > mean):
		print('Date ok')
		return 1

	mini, maxi = np.sort([thisDate, mean])
	if(maxi - mini > outdatedFrom):
		print('might be outdated')
		return 0

	else:
		print((mini-maxi).year)
		print(type(mini))
		print((1/5) * (1/(mini-maxi).year) + 1)
		return (1/5) * (1/(mini-maxi).year) + 1

isOutdated(dates, '2012-02-23 09:36:26')