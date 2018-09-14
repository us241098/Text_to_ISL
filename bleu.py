import pandas as pd
import numpy as np

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.translate.bleu_score import sentence_bleu

cor=pd.read_csv('bleu_correct.csv')
i= pd.read_csv('sl.csv')
print i.test

rea = cor["real"].values
tes = i["test"].values

 
ref=[]
cand=[]
num=[]

for x in range(234):
	reaa = rea[x].lower()
	tess = tes[x].lower()
	reaa = word_tokenize(reaa)
	tess = word_tokenize(tess)

	if len(tess) >= 4:
		num.append(x)

#print len(cand)
#print num

for i in num:
	reaa = rea[i].lower()
	tess = tes[i].lower()
	reaa = word_tokenize(reaa)
	tess = word_tokenize(tess)
	ref.append(reaa)
	cand.append(tess)
final=0
for i in range(113):
	reference = [ref[i],ref[i]]
	candidate = cand[i]
	score = sentence_bleu(reference, candidate)
	final=final+score
	print score

print final
	


