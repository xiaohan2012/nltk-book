import nltk

def loop_contrast(sentence, loop_c):
	grammar = r"""
	NP: {<DT|JJ|NN.*>+}
# Chunk sequences of DT, JJ, NN
	PP: {<IN><NP>}
# Chunk prepositions followed by NP
	VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
	CLAUSE: {<NP><VP>}
# Chunk NP, VP
	"""
	cp = nltk.RegexpParser(grammar , loop = loop_c)
	print "\nwith loop parameter : %d" %(loop_c)
	print cp.parse(sentence)

if __name__ == "__main__":
	sentence = [("Mary", "NN"), ("saw", "VBD"), ("the", "DT"), ("cat", "NN"),
		("sit", "VB"), ("on", "IN"), ("the", "DT"), ("mat", "NN")]
	loop_contrast(sentence , 1)
	loop_contrast(sentence , 2)

	sentence1 = [("John", "NNP"), ("thinks", "VBZ"), ("Mary", "NN"),
	("saw", "VBD"), ("the", "DT"), ("cat", "NN"), ("sit", "VB"),
	("on", "IN"), ("the", "DT"), ("mat", "NN")]
	loop_contrast(sentence1 , 1)
	loop_contrast(sentence1 , 2)
	loop_contrast(sentence1 , 3)
	loop_contrast(sentence1 , 4)

