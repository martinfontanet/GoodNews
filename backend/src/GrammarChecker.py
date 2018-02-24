import requests
from collections import Counter

# 1 is excellent quality and 0 is horrible quality
def spellingQuality(text):
	#compute the number of sentences = roughly the number of occurence of one of the following: . ! ? ;
	count = Counter(text)
	numberOfSentences = max(1, count['.'] + count['?'] + count['!'] + count[';'])

	#compute the number of bad sentences
	r = requests.get(prepareRequest(text))
	response = r.json()
	numberOfBadSentences = min(numberOfSentences, len(response["matches"]))
	print(response["matches"][0])

	return 1 - numberOfBadSentences / numberOfSentences

def prepareRequest(text):
	return "http://localhost:8082/v2/check?language=en-US&text=" + text

if __name__ == "__main__":
	article = "Some dogs are happy. What about happy dogidoggos? I duno about them. What a waste of my time. Hey you;"
	print(spellingQuality(article))