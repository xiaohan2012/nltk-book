from nltk.corpus import reuters
from nltk import FreqDist

fq1 = dict([(cat , len(reuters.fileids(cat)) ) for cat in reuters.categories() ])
fq2 = FreqDist([cat for file_id in reuters.fileids() for cat in reuters.categories(file_id)])
print fq1["ship"],fq1["silver"],fq1["rye"]
print fq2["ship"],fq2["silver"],fq2["rye"]
