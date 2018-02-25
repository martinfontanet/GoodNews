# Assuming only the year are passed as argument (as int)

#returns 1 if the article is outdated 0 if it is current
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