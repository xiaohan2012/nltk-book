from nltk.corpus import brown
from nltk import ConditionalFreqDist as CondFreqDist

categories = brown.categories()
words = ["likely" , "perhaps" , "probably" , "maybe" ]
words = ["female" , "male" , "gentleman" , "lady" , "boy" , "girl"]
cfd = CondFreqDist([(cat , word) for cat in categories\
					for word in brown.words(categories = cat)])
cfd.tabulate(conditions = categories , samples = words)

