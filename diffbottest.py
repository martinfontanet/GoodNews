import http.client
import json
import requests
import urllib
token = "be8deae83c43d9f061a2726cc24a315c"
urlToAnalyse = "https://www.indiatoday.in/education-today/gk-current-affairs/story/picassos-masterpiece-sold-auction-new-york-977763-2017-05-18"
apiUrl = "https://api.diffbot.com/v3/analyze?token=" + token + "&url=" + urlToAnalyse
req = urllib.request.Request(apiUrl)
r = urllib.request.urlopen(req).read()
print(r)
