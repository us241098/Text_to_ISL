import doctest
doctest.testmod()
def wer(r, h):
    """
    Calculation of WER with Levenshtein distance.

    Works only for iterables up to 254 elements (uint8).
    O(nm) time ans space complexity.

    Parameters
    ----------
    r : list
    h : list

    Returns
    -------
    int

    Examples
    --------
    >>> wer("who is there".split(), "is there".split())
    1
    >>> wer("who is there".split(), "".split())
    3
    >>> wer("".split(), "who is there".split())
    3
    """
    # initialisation
    import numpy
    d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8)
    d = d.reshape((len(r)+1, len(h)+1))
    for i in range(len(r)+1):
        for j in range(len(h)+1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i

    # computation
    for i in range(1, len(r)+1):
        for j in range(1, len(h)+1):
            if r[i-1] == h[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                substitution = d[i-1][j-1] + 1
                insertion    = d[i][j-1] + 1
                deletion     = d[i-1][j] + 1
                d[i][j] = min(substitution, insertion, deletion)
    k=len(r)

    return d[len(r)][len(h)],k



import pandas as pd
import numpy as np

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.translate.bleu_score import sentence_bleu

cor=pd.read_csv('bleu_correct.csv')
i= pd.read_csv('sl.csv')

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

sums=0
for i in range(113):
    ans=wer(ref[i], cand[i])
    new_ans = float(ans[0])/float(ans[1])
    print new_ans
    sums=sums+new_ans

print sums

