from nltk.corpus import words
from nltk import FreqDist

postfixes = ["tional","tion","sion"]
interested_words = [w for postfix in postfixes for w in words.words() if w.endswith(postfix)]
print len(interested_words) , len(set(interested_words))
fq = FreqDist(interested_words)	
print fq.keys()[:100]	

	
#print interested_words
