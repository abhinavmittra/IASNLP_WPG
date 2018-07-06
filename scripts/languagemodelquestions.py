'''Evaluation of the generated questions with the kenlm model'''

import kenlm


model=kenlm.Model("Resources/questions.binary") 

#Open the file which contains the generated sentences by sentence_generate.py
with open("Resources/questions", mode='r', encoding='utf-8', errors='ignore') as f:
	ques = f.read()
	quesList=ques.split("\n\n")

perp500 = []
perp750 = []
perp300 = []
perp1000 = []
perp1500 = []
above1500=[]


quesList.pop()#to delete the last blank line from the list
i = 0
s=0
for qn in quesList:
	per=model.perplexity(qn)
	#print(i+1," : ",qn,"-> ",per)
	if(per<=100):
		perp300.append(qn)
	elif(per>300 and per <=500):
		perp500.append(qn)
	elif(per>500 and per<=750):
		perp750.append(qn)
	elif(per>750 and per<=1000):
		perp1000.append(qn)
	elif(per>1000 and per<=1500):
		perp1500.append(qn)
	else:
		above1500.append(qn)
	s+=per
	i=i+1

print("Average Perplexity: ",s/len(quesList))
print("------------------------------------------------------\n\n\n")
print("below 300 \n\n")
for qn in perp300:
	print(qn)
print("300 to 500 \n\n")
for qn in perp500:
	print(qn)
print("500 to 750 \n\n")
for qn in perp750:
	print(qn)
print("750 to 1000 \n\n")
for qn in perp1000:
	print(qn)
print("1000 to 1500 \n\n")
for qn in perp1500:
	print(qn)
print("Above 1500 \n\n")
for qn in above1500:
	print(qn)
