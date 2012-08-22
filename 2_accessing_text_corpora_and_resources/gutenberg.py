import nltk
from nltk.corpus import gutenberg as gb
print "word length \t sentence length\tlexical diversity"
for file_id in gb.fileids():
	raw_len = len(gb.raw(file_id))
	words_len = len(gb.words(file_id))
	sents_len = len(gb.sents(file_id))
	text = nltk.Text(gb.words(file_id))
	vocabs_len = len(set([w.lower() for w in gb.words(file_id)]))
	print "%.2f\t %.2f\t%.2f\t%s" %(raw_len / words_len , words_len / sents_len ,  words_len / vocabs_len , file_id )
