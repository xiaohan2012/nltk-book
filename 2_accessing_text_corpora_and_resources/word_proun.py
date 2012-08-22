from nltk.corpus import cmudict
for w,proun in cmudict.entries():
	if len(proun) >= 10 and len(w) <= 10:
		print w , proun

