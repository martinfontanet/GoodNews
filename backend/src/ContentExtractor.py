import json
import requests
import pickle
import urllib
import collections
import time
import datetime
class Website:

	#GLOBAL INSTANCES! only access them via the class Website
	availableCodes = ["be8deae83c43d9f061a2726cc24a315c", "df03773acaeb9ab91648941e184265c8", "bc73a3e866282150ff6be89c877cf270", "cade4b1ad0ddeed605a77ab391632193", "36b6760b666ad6644f2488d3a6b1b1a4", "7604e9c54883b168c3a524b0fa0698f5"] #Don't do this at home kids
	queue = collections.deque([(c, 0) for c in availableCodes])
	
	def __init__(self, url):
		self.url = url

	def fetch(self):
		code = self.getCode()
		apiUrl = "https://api.diffbot.com/v3/analyze?token=" + code + "&url=" + self.url
		req = urllib.request.Request(apiUrl)
		r = urllib.request.urlopen(req).read()
		self.json = json.loads(r.decode('utf-8'))
		Website.queue.appendleft((code, time.time())) #put the used code at the end of the queue
		print(type(self.json))
		print(self.json)
		return self

	def getText(self):
		return self.json["objects"][0]["text"]

	def isArticle(self):
		if "objects" not in self.json:
			return False
		if len(self.json["objects"]) == 0:
			return False
		if "type" not in self.json["objects"][0]:
			return False
		else:
			return self.json["objects"][0]["type"] == "article"

	def getYear(self):
		if "date" not in self.json["objects"][0]:
			return 999999
		rawDate = self.json["objects"][0]["date"]
		if len(rawDate) >= 17:
			return int(rawDate[12:16])
		else:
			return 9999999 #Don't do this at home kids

	def getLanguage(self):
		if "humanLanguage" not in self.json:
			return "---"
		return self.json["humanLanguage"]

	def getImages(self):
		return [im["url"] for im in self.json["objects"][0]["images"]]

	def getCode(self):
		(code, lastTimeUsed) = Website.queue.pop()
		if time.time() - lastTimeUsed <= 1.1: #the diffbot accepts only one request every 1 secs
			time.sleep(1) #1 sec
		return code

##########################
# After here, we unit test
##########################

if __name__ == "__main__":
	website = Website("https://www.christies.com/lotfinder/Lot/pablo-picasso-1881-1973-femme-assise-robe-bleue-6073940-details.aspx")
	website.fetch()
	#print(website.isArticle())
	print(website.getText())
	print(website.getLanguage())
	print(website.getDate())
	print(website.getImages())
