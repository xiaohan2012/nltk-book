from nltk.corpus import webtext
for file_id in webtext.fileids():
	print file_id
	print webtext.raw(file_id)[:100]
	print
