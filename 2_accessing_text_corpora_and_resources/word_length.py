from nltk.corpus import words
from nltk import ConditionalFreqDist as CFreqDist , FreqDist

cfd = CFreqDist([(w[0] , len(w)) for w in words.words()])
cfd.plot()
fd = FreqDist([w[0] for w in words.words()])
fd.plot()
