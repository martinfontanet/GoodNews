from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

#returns some confidence level between 0 and 1. 0 is fake news and 1 is good news
def computeSimiliarity(bases, new):
	bases.append(new)
	vect = TfidfVectorizer(min_df=1)
	tfidf = vect.fit_transform(bases)
	cosines = (tfidf * tfidf.T).A[len(bases)-1][:len(bases)-1]
	print(cosines)
	agreeing = np.sum(cosines >= 0.5)
	return agreeing / (len(bases) - 1)

############################
# After here: "unit testing"
############################
def getTextForFile(name):
	with open("/Users/gilbert/Programming/hackatons/starthack2018/texts/" + name) as f:
		content = f.readlines()
		toReturn = ""
		for c in content:
			toReturn += c.strip()
		return toReturn

if __name__ == "__main__":
	train = [getTextForFile(x) for x in ["soccer2.txt", "soccer1.txt", "soccer3.txt", "soccer4.txt", "soccer5.txt"]] #, "soccer2.txt", "soccer3.txt", "soccer4.txt"	
	agreeing = computeSimiliarity(train, getTextForFile("guns2.txt"))
	print("Agreeing: ", agreeing, " -> ", "fake news" if agreeing < 0.5 else "good news")


#### GILBERT 24/02/18 : deprecated
#def getMatchingTopicsEstimates(train, test):
#	gen_docs = [[w.lower() for w in word_tokenize(text)] for text in train]
#	dictionary = gensim.corpora.Dictionary(gen_docs)
#	corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
#	tf_idf = gensim.models.TfidfModel(corpus)
#	sims = gensim.similarities.Similarity("/Users/gilbert/Desktop", tf_idf[corpus], num_features=len(dictionary))
#	query_doc = [w.lower() for w in word_tokenize(test)]
#	query_doc_bow = dictionary.doc2bow(query_doc)
#	query_doc_tf_idf = tf_idf[query_doc_bow]
#	print(sims[query_doc_tf_idf])