'''
script to Generate ngrams

Authors: Aditya, Abhinav
'''
import collections, nltk
from nltk import word_tokenize 
from nltk.util import ngrams
import json

with open("equations.json") as f:
	x = json.load(f)

qnList = []

for i in x:
	qnList.append(i['sQuestion'])

for k in range(0,len(qnList)):
	qnList[k] = qnList[k].replace('.',"")
	qnList[k]=qnList[k].strip()
	qnList[k] = qnList[k].replace("?","")
	qnList[k] = qnList[k].replace("-"," ")
	qnList[k] = qnList[k].replace("'","")

bigram=[]

for qn in qnList[:6]:
    token =nltk.word_tokenize(qn)
    bigram.append(list(ngrams(token,2))) 

print(bigram)