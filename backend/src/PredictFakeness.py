import random
# returns a prediction dictionary with keys:
#    isFake in [0, 1]
def predictFakeness(imagePath, url):
	return str(random.randint(1,255))
	#return "Defo not a fake dayum for (" + str(imagePath) + ", " + str(url) + ")"
