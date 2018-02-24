import numpy as np

# assuming dates are passed as int representing year
def isOutdated(otherDates, thisDate):


	print(thisDate)
	mean = np.array(otherDates).mean()

	if(mean - thisDate >= 5):
		return 0
	elif(mean - thisDate <= -5):
		return 0

	elif(thisDate < mean):
		return (-1/5) * (mean-thisDate) + 1

	elif(thisDate > mean):
		return (1/5) * (mean-thisDate) + 1
	
	else:
		return 0

