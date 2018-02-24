import json
import requests
import pickle
import urllib

class Website:

	def __init__(self, url):
		self.url = url

	def fetch(self):
		token = "be8deae83c43d9f061a2726cc24a315c"
		apiUrl = "https://api.diffbot.com/v3/analyze?token=" + token + "&url=" + self.url
		req = urllib.request.Request(apiUrl)
		r = urllib.request.urlopen(req).read()
		self.json = json.loads(r.decode('utf-8'))

	def getText(self):
		return self.json["objects"][0]["text"]

	def isArticle(self):
		return self.json["objects"][0]["type"] == "article"

	def getDate(self):
		return self.json["objects"][0]["date"]

	def getLanguage(self):
		return self.json["humanLanguage"]

	def getImages(self):
		return [im["url"] for im in self.json["objects"][0]["images"]]


##########################
# After here, we unit test
##########################

if __name__ == "__main__":
	website = Website("https://www.indiatoday.in/education-today/gk-current-affairs/story/picassos-masterpiece-sold-auction-new-york-977763-2017-05-18")
	website.fetch()
	print(website.isArticle())
	print(website.getText())
	print(website.getLanguage())
	print(website.getDate())
	print(website.getImages())
