import random
from ContentExtractor import Website
from GrammarChecker import spellingQuality
from MatchingTopicsChecker import computeSimilarity
from ListChecker import isWhiteListed
from ListChecker import isBlackListed
from OutdatedArticle import isOutdated
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
	#if isWhiteListed(articleURL):
	#	return {"isFake": 0.95, "message": "This website is generally trusted", "isArticle": 1}

	#if isBlackListed(articleURL):
	#	return {"isFake": 0.05, "message": "This website is generally not trusted", "isArticle": 1}

	#Grammar score computation
	if article.getLanguage() == "en" and spellingQuality(article.getText()) < 0.2: #the text has a very poor english... bad smell!
		return {"isFake": 0.1, "message": "The article has very bad spelling, it doesn't look serious", "isArticle": 1}

	articlesWithSameImages = [Website(url).fetch() for url in articlesWithSameImagesURLs]
	articlesWithSameImages = [x for x in articlesWithSameImages if x.isArticle()] # keep only articles

	#Article date score computation
	if isOutdated([website.getYear() for website in articlesWithSameImages], article.getYear()) <= 0.9: #picture appeared a long time ago... bad smell!
		return {"isFake": 0.3, "message": "Some picture were also found in old articles, bad smell!", "isArticle": 1}

	#Agreement score computation
	articlesWithSameImages = [x for x in articlesWithSameImages if x.getLanguage() == article.getLanguage()] # filter to only keep articles that match the original language
	if len(articlesWithSameImages) > 0:
		agreementScore = computeSimilarity([x.getText() for x in articlesWithSameImages], article.getText())
		return {"isFake": agreementScore, "message": "This estimate was found by looking at other articles using the same images", "isArticle": 1}

	return {"isFake": 0.5, "message": "Can't tell sorry", "isArticle": 1}

if __name__ == "__main__":
	# THIS SHOULD OUTPUT GOOD
	#toVerify = "http://www.bbc.com/news/world-europe-43169054"
	#withSameImage = ["http://www.bbc.com/news/uk-politics-32810887", "http://www.bbc.com/news/uk-politics-43136076", "https://edition.cnn.com/2018/02/23/opinions/brexit-could-change-the-united-kingdom-as-we-know-it-robertson-opinion/index.html"]

	# THIS SHOULD FAKE
	#toVerify = "https://www.gadgetsnow.com/tech-news/tech-mahindra-to-set-up-ai-excellence-unit-in-canada/articleshow/63058877.cms"
	#withSameImage = ["https://timesofindia.indiatimes.com/sports/football/epl/top-stories/fa-charges-guardiola-for-political-catalonia-ribbon/articleshow/63049174.cms", "https://timesofindia.indiatimes.com/sports/football/top-stories/zidane-proud-of-reals-emphatic-response-after-poor-start/articleshow/63048614.cms"]
	#print(predictFakeness(toVerify, withSameImage))
