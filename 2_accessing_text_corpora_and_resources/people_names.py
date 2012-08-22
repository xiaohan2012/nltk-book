from nltk.corpus import names
from nltk import ConditionalFreqDist as CondFreqDist

g2n = CondFreqDist([(gender, name[0]) for gender in names.fileids() for name in names.words(gender)])
n2g = CondFreqDist([(name[0] , gender) for gender in names.fileids() for name in names.words(gender)])
g2n.plot()
n2g.plot()

