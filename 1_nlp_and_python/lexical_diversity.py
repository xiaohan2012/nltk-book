from nltk import book
from nltk.corpus import brown
def lexical_diversity(text):
    return float(len(text)) / len(set(text))

def text1_9_diversity():
    for i in xrange(1,10):
        text = getattr(book,"text%d" %i)
        print "%s:%f" %(text.name , lexical_diversity(text) )  

def category_diversity():
    for category in brown.categories():
        words = brown.words(categories = category)    
        print "%s: %f" %(category , lexical_diversity(words))

if __name__ == "__main__":
    category_diversity()
   
