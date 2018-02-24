from urllib.parse import urlsplit

def isWhiteListed(url):
	whiteList = {"http://wikipedia.com/"}
	return getDomainName(url) in whiteList

def isBlackListed(url):
	blackList = {"http://creationists.com/"}
	return getDomainName(url) in blackList

def getDomainName(url):
	return "{0.scheme}://{0.netloc}/".format(urlsplit(url))

if __name__ == "__main__":
	print("Wikipedia is wl?", isWhiteListed("http://wikipedia.com/some/random/stuff"))
	print("Creationists is bl?", isBlackListed("http://creationists.com/yolo"))