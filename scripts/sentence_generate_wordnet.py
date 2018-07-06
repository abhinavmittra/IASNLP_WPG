'''
Generate sentences with wordnet synonyms

Authors: Aditya, Abhina
'''

import itertools
import inflect
import json
import ast
import random
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

inflect = inflect.engine()

### Temporary list of proper nouns ###
names=["Noah", "Eugenie", "Trent", "Teodora", "Georgie", "Toni", "Tory", "Carrol", "Wayne", "Shelli", "Leta", "Helena", "Katrice", "Lavon", "Charis", "Tamatha", "Bernardina", "Maynard", "Adelaida", "Nicolas"]

with open("equations.json") as f:
	x = json.load(f)

qnList = []

for i in x:
	qnList.append(i['sQuestion'])

### naive pre-processing ###
for k in range(0,len(qnList)):
	qnList[k] = qnList[k].replace('.',"")
	qnList[k]=qnList[k].strip()
	qnList[k] = qnList[k].replace("?","")
	qnList[k] = qnList[k].replace("-"," ")
	qnList[k] = qnList[k].replace("'","")


zz = open("synonyms_2each").read()
array = ast.literal_eval(zz)

qncount=1
for qn in range(len(array)):
	# print("Question Number: " + str(qncount) + " ->" + "\n\n")
	# qncount+=1
	perm = list(itertools.product(*array[qn]))      # Generate a permuted list of tuples holding synoinyms for each sentence
	text = qnList[qn]
	tokenize_text = word_tokenize(text)
	pos_tag_text = nltk.pos_tag(tokenize_text)
	propernouns = list(set([word for word,pos in pos_tag_text if pos == 'NNP']))
	while "How" in propernouns or "how" in propernouns: propernouns.remove("How")    #nltk tags How as propn, maybe for many other capitalized words too (we didn't encounter)
	# print(propernouns)
	ran_names = random.sample(names,len(propernouns))   #for each sentence for a given synonym list replace names with random names


	#stop_counter variable to restrict number of generated sentences. optional.
	stop_counter=0

	for i in perm:
		stop_counter+=1
		if(stop_counter==30):
			break
		else:
			ran_names = random.sample(names,len(propernouns))
				
			'''loop checks for each word in the sentence whether its singular or plural form has a synonym in the permuted list and generates sentences with
				random names'''	
			for word in text.split():

				if (inflect.singular_noun(word) is False):
					plu = inflect.plural(word)
					sing = word
				else:
					plu = word
					sing = inflect.singular_noun(word)	
				plu = plu+"_"
				sing = sing+"_"
				# print(x)
				temp_str = [ i[i.index(t)] for t in i if plu in t ]  
				x = plu
				if(not temp_str):
					temp_str = [ i[i.index(t)] for t in i if sing in t ]
					x=sing
				if(not temp_str):	
					if word in propernouns:
						print(ran_names[propernouns.index(word)], end=' ')
					else:	
						print (word, end=' ')
				else:
					temp_temp = temp_str[0]
					new_str = temp_temp[(len(x)):]
					print(new_str, end=' ')

			print("\n")				
