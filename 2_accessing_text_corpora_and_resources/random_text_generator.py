from nltk.corpus import brown
from nltk import ConditionalFreqDist as CondFreqDist , bigrams
def gen_rand_text(cfd  , start_word , num = 15):
	word = start_word
	for i in xrange(num):
		print word,
		word = cfd[word].max()
		if not word:
			print "seems not in this genre"
			break

for genre in brown.categories():
	cfd = CondFreqDist(\
			bigrams( brown.words(categories = genre)))
	print genre
	gen_rand_text(cfd, 'love' )
	print 
