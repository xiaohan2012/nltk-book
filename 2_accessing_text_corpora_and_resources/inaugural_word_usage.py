from nltk.corpus import inaugural as inag
from nltk import ConditionalFreqDist as CondFreqDist
cfd = CondFreqDist([(target , fileid[:4])\
		for fileid in inag.fileids() \
			for word in inag.words(fileid) \
				for target in ["wealth" , "peace" , "harmony" , "prosperous"] if word.lower().startswith(target)
		])
cfd.plot()
