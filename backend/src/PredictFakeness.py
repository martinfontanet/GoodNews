import random
from ContentExtractor import Website
from GrammarChecker import spellingQuality
from MatchingTopicsChecker import computeSimilarity
from ListChecker import isWhiteListed
from ListChecker import isBlackListed
import time

# returns a prediction dictionary with keys:
#    isFake: in [0, 1] (0 = fake, 1 = good)
#    message: a message that explain the decision
#    isArticle: True if the link is an article else False
def predictFakeness(articleURL, articlesWithSameImagesURLs):
	article = Website(articleURL)
	article.fetch()

	if not article.isArticle():
		return {"isFake": 0, "message": "This is not an article!", "isArticle": 0}

	#Check for whitelist / blacklist
	if isWhiteListed(articleURL):
		return {"isFake": 0.95, "message": "This website is generally trusted", "isArticle": 1}

	if isBlackListed(articleURL):
		return {"isFake": 0.05, "message": "This website is generally not trusted", "isArticle": 1}

	#Grammar score computation
	grammarScore =  spellingQuality(article.getText()) if article.getLanguage() == "en" else -1

	#Agreement score computation
	agreementScore = -1
	articlesWithSameImages = [Website(url).fetch() for url in articlesWithSameImagesURLs]
	articlesWithSameImages = [x for x in articlesWithSameImages if x.getLanguage() == article.getLanguage() and x.isArticle()] # filter to only keep articles and only that match the original language
	if len(articlesWithSameImages) > 0:
		agreementScore = computeSimilarity([x.getText() for x in articlesWithSameImages], article.getText())

	#Article date score computation
	dateScore = 0.9 #todo...
	totScore = computeFakeProba(grammarScore, agreementScore, dateScore)
	return {"isFake": totScore, "message": "Some message...", "isArticle": 1}

def computeFakeProba(grammarScore, agreementScore, dateScore): # don't do this at home kids
	if grammarScore >= 0 and agreementScore >= 0:
		return (1 * dateScore + 6 * agreementScore + 1 * grammarScore) / float(8)
	elif grammarScore >= 0:
		return (1 * dateScore + 1 * grammarScore) / float(2)
	else:
		return (2 * dateScore + 4 * agreementScore) / float(6) 

if __name__ == "__main__":
	# THIS SHOULD OUTPUT GOOD
	#toVerify = "http://www.bbc.com/news/world-europe-43169054"
	#withSameImage = ["http://www.bbc.com/news/uk-politics-32810887", "http://www.bbc.com/news/uk-politics-43136076", "https://edition.cnn.com/2018/02/23/opinions/brexit-could-change-the-united-kingdom-as-we-know-it-robertson-opinion/index.html"]

	# THIS SHOULD FAKE
	toVerify = "https://www.gadgetsnow.com/tech-news/tech-mahindra-to-set-up-ai-excellence-unit-in-canada/articleshow/63058877.cms"
	withSameImage = ["https://timesofindia.indiatimes.com/sports/football/epl/top-stories/fa-charges-guardiola-for-political-catalonia-ribbon/articleshow/63049174.cms", "https://timesofindia.indiatimes.com/sports/football/top-stories/zidane-proud-of-reals-emphatic-response-after-poor-start/articleshow/63048614.cms"]
	print(predictFakeness(toVerify, withSameImage))
