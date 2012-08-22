from nltk.corpus import cmudict
interested_words = ["what" , "fuck" , "shit"]
interested_prouns = [cmudict.dict()[word][0][-2:] for word in interested_words ]
print [word for word , proun in cmudict.entries() if proun[-2:] in interested_prouns] 
