'''Script to generate word synonyms using word2vec 
Authors: Abhinav,Aditya
'''

import json
import ast
import gensim
#Load the Google pretrained Word2Vec Model.
#You can download it from http://mccormickml.com/2016/04/12/googles-pretrained-word2vec-model-in-python/
model  = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin',limit=1000000, binary=True)

#Open the file which has the list of all the word problems
with open("Resources/equations.json") as f:
	x = json.load(f)


qnList = []
#File which contains the contents words filtered by using spacy pos tag (Output of file words_for_synonyms)
pp = open("Resources/file").read()
loadedlist = ast.literal_eval(pp)

#Appending all questions from the json file to a list
for i in x:
	qnList.append(i['sQuestion'])


#List having 
synonyms=[]

qsynonyms=[[] for _ in range(len(qnList))]

i=0
for qn in range(len(qnList)):
	noun_verbs = loadedlist[qn]
	#if list is empty i.e has no words to be replaced by their synonyms then append an empty list
	if(not noun_verbs):
		synonyms.append([])
		continue
	for word in noun_verbs:
		words=[]
		try:
			xx=model.most_similar(positive = word,topn=2)
		except:
			continue
		for syn in xx:	
			words.append(word+"_"+syn[0])
		qsynonyms[i].append(tuple(words))
	synonyms.append(qsynonyms[i])
	i=i+1
print(synonyms)	
