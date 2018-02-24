import json
import requests
import pickle
import urllib
import datetime
import numpy as np
class Website:

	def __init__(self, url):
		self.url = url

	def fetch(self):
		token = "be8deae83c43d9f061a2726cc24a315c"
		apiUrl = "https://api.diffbot.com/v3/analyze?token=" + token + "&url=" + self.url
		req = urllib.request.Request(apiUrl)
		r = urllib.request.urlopen(req).read()
		self.json = json.loads(r.decode('utf-8'))
		try:
			self.article = self.isArticle()
		except IndexError:
			self.article = False

	def getText(self):
		if(self.article):
			return self.json["objects"][0]["text"]
		else:
			return ""

	def isArticle(self):
		return self.json["objects"][0]["type"] == "article"

	def getDate(self):
		if(self.article):
			rawDate = self.json["objects"][0]["date"]
			#rawDate1 = rawDate.replace(" GMT", "")
			#rawDate2 = rawDate1.replace(",", "")
			#print(rawDate2)
			datetime_object = rawDate[12:16]
			#datetime_object = datetime.datetime.strptime(rawDate2, "%a %d %b %Y %I:%M:%S")
			return datetime_object
		else:
			return datetime.datetime(1000,1,1)

	def getLanguage(self):
		if(self.article):
			return self.json["humanLanguage"]
		else:
			return ""

	def getImages(self):
		if(self.article):
			return [im["url"] for im in self.json["objects"][0]["images"]]
		else:
			return []

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
