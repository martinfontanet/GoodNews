import http.client
import json
import requests
import pickle
import urllib

#urlToAnalyse = "https://www.indiatoday.in/education-today/gk-current-affairs/story/picassos-masterpiece-sold-auction-new-york-977763-2017-05-18"



#articleText = data["objects"][0]["text"]


class Website:

	def __init__(self, url):
		self.url = url
		self.isArticle = False
		self.date = ""
		self.language = "en"
		self.image = []
		self.json = self.getJson()

	def getJson(self):

		token = "be8deae83c43d9f061a2726cc24a315c"
		apiUrl = "https://api.diffbot.com/v3/analyze?token=" + token + "&url=" + self.url
		req = urllib.request.Request(apiUrl)
		r = urllib.request.urlopen(req).read()

		return json.loads(r)

	def getText(self):
		return self.json["objects"][0]["text"]

	def isArticle(self):
		return self.json["objects"][0]["type"] == "article"

	def getDate(self):
		return self.json["objects"][0]["date"]

	def getLanguage(self):
		return self.json["humanLanguage"]

	def getImages(self):
		all_url = []
		for im in self.json["objects"][0]["images"]:
			all_url.append(im["url"])

		return all_url

#website = Website("https://www.indiatoday.in/education-today/gk-current-affairs/story/picassos-masterpiece-sold-auction-new-york-977763-2017-05-18")
#print(website.getText())
#print(website.getLanguage())
#print(website.getDate())
#print(website.getImages())
