import numpy as np

# assuming dates are passed as int representing year
def isOutdated(otherDates, thisDate):


	print(thisDate)
	mean = np.array(otherDates).mean()

	if(thisDate >= mean):
		print('Date ok')
		return 1

	if(mean - thisDate > 5):
		return 0

	else:
		return (1/5) * (mean-thisDate) + 1
