import requests
from collections import Counter
from ContentExtractor import Website

# 1 is excellent quality and 0 is horrible quality
def spellingQuality(text):
	text.replace("“", "") #remove quotation marks, Language Tool doesn't like the 

	#compute the number of sentences = roughly the number of occurence of one of the following: . ! ? ;
	count = Counter(text)
	numberOfSentences = max(1, count['.'] + count['?'] + count['!'] + count[';'])

	#compute the number of bad sentences
	r = requests.get(prepareRequest(text))
	response = r.json()

	numberOfBadSentences = 0
	for l in response["matches"]:
		if len(l["replacements"]) > 0 and "value" in l["replacements"][0] and len(l["replacements"][0]["value"]) > 0 and l["replacements"][0]["value"][0].islower():
			numberOfBadSentences += 1
	numberOfBadSentences = min(numberOfBadSentences, numberOfSentences)

	return 1 - numberOfBadSentences / numberOfSentences

def prepareRequest(text):
	return "http://localhost:8082/v2/check?language=en-US&text=" + text

if __name__ == "__main__":
	article = "Some dogs are happy. What about happy dogidoggos? I duno about them. What a waste of my time."
	print("that should be .6", spellingQuality(article))
	
	url = "http://www.bbc.com/news/uk-politics-43136076"
	article = Website(url)
	text = article.fetch().getText()
	print("that should be something close to 1 ", spellingQuality(text))