from nltk.corpus import nps_chat
from nltk import FreqDist

first_n = 100

a_fq = FreqDist(nps_chat.words('11-09-adults_706posts.xml'))
t_fq = FreqDist(nps_chat.words('11-09-teens_706posts.xml'))

a_words = set(a_fq.keys()[:first_n])
t_words = set(t_fq.keys()[:first_n])

print "common used words:"
print ','.join( a_words.intersection(t_words) )
print 
print "adult use while teens not use:"
print ','.join( a_words - t_words )
print
print "teen use while adult not use:"
print ','.join( t_words - a_words )
