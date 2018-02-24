from urllib.parse import urlsplit

with open('whitelist.txt') as f:
	whiteList = [l.replace("\n", "") for l in f.readlines()]
with open('blacklist.txt') as f:
	blackList = [l.replace("\n", "") for l in f.readlines()]
def isWhiteListed(url):
	return getDomainName(url) in whiteList

def isBlackListed(url):
	return getDomainName(url) in blackList

def getDomainName(url):
	return "{0.scheme}://{0.netloc}".format(urlsplit(url))

if __name__ == "__main__":
	print("Wikipedia is wl?", isWhiteListed("http://eurosport.com/yolo"))
	print("Creationists is bl?", isBlackListed("http://mercola.com"))




