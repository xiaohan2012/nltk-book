from nltk.corpus import brown
from nltk import ConditionalFreqDist as CondFreqDist
cfd = CondFreqDist([(genre , word.lower())\
		for genre in brown.categories() \
			for target in ["romance" , "news"] if genre.lower().startswith(target)\
				for word in brown.words(categories = target)])
days = ["monday" , "tuesday" , "wednesday" , "thursday" , "friday" , "saturday" , "sunday" , "love" , "political"]
cfd.tabulate(samples = days)
