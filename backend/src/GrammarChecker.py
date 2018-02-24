import requests

def isSpellingOk(text):
	r = requests.get(prepareRequest(text))
	response = r.json()
	return len(response["matches"]) == 0

def prepareRequest(text):
	return "http://localhost:8082/v2/check?language=en-US&text=" + text
