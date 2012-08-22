from nltk.corpus import stopwords , brown

def not_common_words_fraction(words):
	not_common = set( [w.lower() for w in words if w not in stopwords.words("english") ])
	return len(not_common) / float( len(words) )

#print [(genre , not_common_words_fraction( brown.words(categories = genre))) for genre in brown.categories() ]	
for genre in brown.categories():
	print genre , not_common_words_fraction( brown.words(categories = genre))
