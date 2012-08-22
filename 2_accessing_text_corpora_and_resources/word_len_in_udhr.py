from nltk.corpus import udhr
languages = ['Korean_Hankuko' , 'Japanese_Nihongo' , 'Vietnamese-ALRN' ]
cfd = nltk.ConditionalFreqDist(
			  (lang, len(word)) \
			  for lang in languages \
			  for word in udhr.words(lang + '-UTF8'))
cfd.plot(cumulative=True)

