'''

Script to generate words which are to be replaced by their synonyms while generating sentences

Authors: Aditya, Abhinav

'''

import spacy
import json

nlp = spacy.load('en')

with open("equations.json") as f:
	x = json.load(f)

qnList = []

for i in x:
	qnList.append(i['sQuestion'])

qnSynonyms = []
synList=[]

for i in qnList:
	qnSynonyms = []
	doc = nlp(i)
	for token in doc:
		if(token.dep_ in ['dobj','amod','iobj','pobj'] and token.pos_ not in ['PROPN']):
			a = token.text
			a=a.replace('.',"")
			if(a.isdigit() == False):
				qnSynonyms.append(token.text)
	qnSynonyms = list(set(qnSynonyms))
	synList.append(qnSynonyms[:5])

print(synList)	
			