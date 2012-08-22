from nltk.corpus import words
from nltk import FreqDist

puzzle = FreqDist( "qwekmnabc" )
must = "a"
matched = [w for w in words.words() if must in w \
	  and FreqDist(w) <= puzzle\
	  and len(w) >= 3]
print matched
