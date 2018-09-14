import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import OrderedDict
import numpy as np
import nltk
import pandas as pd
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import *
import csv
text_file = open("output.txt", "w")

nltk.download('wordnet')
df = pd.read_csv('text.csv')
inpp= pd.read_csv('sentences.csv')
inputt=inpp.sent

for i in inputt:
	df = pd.read_csv('text.csv')
	print i
	txt = str(i) 
	txt=txt.replace('.',' ')
	txt=txt.replace(',',' ')
	tokenized = sent_tokenize(txt)
#	print tokenized


	for i in tokenized:
		wordsList = nltk.word_tokenize(i)
		tagged = nltk.pos_tag(wordsList)
		array = np.array(tagged)
		list1, list2 = zip(*tagged)
#		print list1,list2


	list1=np.array(list1)
#	print list1
#	print list2
	list2 = " ".join(list2)
	df=df.loc[(df["sent"]== list2 )]
	x= (df.rules.values.tolist())
	x=x[0].split()
#	print x
	ans=""


	for i in x:
		ps = PorterStemmer()
		lm = WordNetLemmatizer()
#		print lm.lemmatize('made','v')

		if '#' in i:
		    i=list(i)
		    i=int(i[0])
		    ans=ans+" "+ps.stem(list1[i])

		elif '*' in i:
		    i=list(i)
		    i=int(i[0])
		    ans=ans+" "+lm.lemmatize(list1[i],'v')

		else:
		    i=int(i)
		    ans=ans+" "+list1[i]

	print ans
	text_file.write(ans+"\n")

text_file.close()


	#print df.rules.value.split(" ")
