# Assuming only the year are passed as argument (as int)
# assuming dates are passed as int representing year
def isOutdated(otherDates, thisDate):
	if len(otherDates) == 0:
		return 0

	mean = sum(otherDates) / len(otherDates)
	toReturn = (thisDate - mean) / 5
	toReturn = max(0, toReturn)
	toReturn = min(1, toReturn)
	return toReturn

if __name__ == "__main__":
	otherDates = [2000, 2000, 2000, 2000]
	thisDate = 2100
	print(isOutdated(otherDates, thisDate))