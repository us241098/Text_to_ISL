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


nltk.download('wordnet')
	
df = pd.read_csv('text.csv')
txt = "What is his name?" 
txt=txt.replace('.',' ')
txt=txt.replace(',',' ')
tokenized = sent_tokenize(txt)
print tokenized