from nltk import book
from nltk import  FreqDist

def filter_words_by_len(text,length = 15):
    return set([w for w in text if len(w) >= length])

def filter_words_by_len_fq(text,length = 7 , freq = 7):
    fq = FreqDist(text)
    return set([w for w in text if len(w) >= length and fq[w] >= freq])
   
if __name__ == "__main__":
    for i in xrange(1,10):
        text = getattr(book,"text%d" %i)
        print text.name , len(filter_words_by_len_fq(text))
        print "#" *20
