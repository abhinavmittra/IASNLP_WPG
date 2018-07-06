import nltk
from nltk.corpus import wordnet as wn
import json
from nltk.tokenize import sent_tokenize,word_tokenize


with open("Resources/equations.json") as f:
	x = json.load(f)

qnList = []

for i in x:
	qnList.append(i['sQuestion'])

for a in range(len(qnList)):
	qnList[a] = qnList[a].replace('.',"")
	qnList[a]=qnList[a].strip()
	qnList[a] = qnList[a].replace("?","")

synonyms=[]
qsynonyms=[[] for _ in range(len(qnList))]

for qn in range(len(qnList)):
	sentence = qnList[qn]
	tokenize_text = word_tokenize(sentence)
	pos_tag_text = nltk.pos_tag(tokenize_text)
	
	noun_verbs = list(set([word for word,pos in pos_tag_text if (pos == 'NN' or pos == 'NNS' or pos == 'VB' or pos == 'VBD'or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ')]))

	for word in noun_verbs:
		words=set()
		for syn in wn.synsets(word):	
			for lm in syn.lemmas():
				words.add(word+"_"+lm.name())
		qsynonyms[i].append(tuple(words))
	qsynonyms[i]=[t for t in qsynonyms[i] if t]
	synonyms.append(qsynonyms[i])
	i=i+1
print(synonyms)	
