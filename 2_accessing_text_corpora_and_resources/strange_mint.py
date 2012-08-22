from nltk.corpus import wordnet as wn
for ss in wn.synsets("mint" , wn.NOUN):
	print ss.definition
