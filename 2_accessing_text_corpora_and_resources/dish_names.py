from nltk.corpus import wordnet as wn
for synset in  wn.synsets("dish"):
	print synset
	print [lemma.name for hypo in synset.hyponyms() for lemma in hypo.lemmas]
