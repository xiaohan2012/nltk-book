import nltk

def non_phrase_chunking_single_rule():
	sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
	grammar = "NP: {<DT>?<JJ>*<NN>}"
	cp = nltk.RegexpParser(grammar)
	result = cp.parse(sentence)
	print result
	result.draw()
def non_phrase_chunking_multiple_rules():
	grammar = r"""
	NP: {<DT|PP\$>?<JJ>*<NN>}
# chunk determiner/possessive, adjectives and nouns
{<NNP>+}
# chunk sequences of proper nouns
"""
	cp = nltk.RegexpParser(grammar)
	sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"),
	("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]
	print cp.parse(sentence)

def find_chunks(pattern , corpus):
	cp = nltk.RegexpParser(pattern)
	if callable(getattr(corpus,"tagged_sents",None)):
		for sent in corpus.tagged_sents()[:100]:
			tree = cp.parse(sent)
			for subtree in tree.subtrees():
				if subtree.node == "CHUNK":print subtree

def chinking_example():
	grammar = r"""
	NP: {<PP\$>? <JJ>* <NN.*>}
	}<VBD|RP>+{
	"""
	cp = nltk.RegexpParser(grammar)
	sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"),
	("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]
	print cp.parse(sentence)




if __name__ == "__main__":
#non_phrase_chunking_single_rule()
#non_phrase_chunking_multiple_rules()
#find_chunks("CHUNK: {<V.*> <TO> <V.*>}",nltk.corpus.brown)
	chinking_example()
