from nltk import book
from nltk import FreqDist

def get_word_len_freq(text):
    fd = FreqDist([len(w) for w in text])
    return fd

if __name__ == "__main__":
    for i in xrange(1,10):
        text = getattr(book,"text%d" %i)
        fd = get_word_len_freq(text)
        selected_len = fd.keys()[:10]
        print text.name 
        print "".join( ("%d" %k).ljust(10) for k in selected_len )
        print "".join(( "%.3f" %fd.freq(k) ).ljust(10) for k in selected_len )
    
    
