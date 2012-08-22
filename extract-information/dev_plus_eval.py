import nltk
def iob2tree():
	text = '''
he PRP B-NP
accepted VBD B-VP
the DT B-NP
position NN I-NP
of IN B-PP
vice NN B-NP
chairman NN I-NP
of IN B-PP
Carlyle NNP B-NP
Group NNP I-NP
, , O
a DT B-NP
merchant NN I-NP
banking NN I-NP
concern NN I-NP
. . O
	'''
	nltk.chunk.conllstr2tree(text, chunk_types=['PP']).draw()

def baseline_chunker():
	cp = nltk.RegexpParser("")
	test_sents = nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=['NP'])
	print cp.evaluate(test_sents)


def regex_chunker():
	cp = nltk.RegexpParser("NP: { <NN.*>+ }")
	test_sents = nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=['NP'])
	print cp.evaluate(test_sents)

class UnigramChunker(nltk.ChunkParserI):
	def __init__(self,train_sents):
		train_tags =  [[( p , c ) for w , p , c  in  nltk.chunk.tree2conlltags(sent)] for sent in train_sents ]#extract pos and chunk tag
		self.tagger = nltk.UnigramTagger(train_tags) #train the tagger

	def parse(self,sent):
		pos = [pos for (w,pos) in sent] #get pos
		chunk_tags = [ chunk_tag for p,chunk_tag in self.tagger.tag(pos) ]#tag pos
		oib = [(w,pos, chunk_tag) for (w , pos) , chunk_tag in zip(sent,chunk_tags)] #concatenate the two lists
		return nltk.chunk.conlltags2tree(oib)

def unigramchunker_test():
	train_sents = nltk.corpus.conll2000.chunked_sents('train.txt', chunk_types=['NP'])
	test_sents = nltk.corpus.conll2000.chunked_sents('test.txt', chunk_types=['NP'])
	chunker = UnigramChunker(train_sents)
	print chunker.evaluate(test_sents)

if __name__ == "__main__":
#iob2tree()
#baseline_chunker()
#regex_chunker()
	unigramchunker_test()
