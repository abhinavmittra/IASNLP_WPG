'''Script for evaluatiing Questions (sentence-wise) 
Authors: Aditya,Abhinav'''


import kenlm
model=kenlm.Model("Resources/final_1lineeach.binary") 
with open("Resources/word2vecsen", mode='r', encoding='utf-8', errors='ignore') as f:
	ques = f.read()
	quesList=ques.split("\n\n")
perp500 = []
perp750 = []
perp300 = []
perp1000 = []
perp1500 = []
above1500=[]
quesList.pop()
j = 0
s=0
senper=0
names=["Noah", "Eugenie", "Trent", "Teodora", "Georgie", "Toni", "Tory", "Carrol", "Wayne", "Shelli", "Leta", "Helena", "Katrice", "Lavon", "Charis", "Tamatha", "Bernardina", "Maynard", "Adelaida", "Nicolas"]

for k in range(0,len(quesList)):
	quesList[k] = quesList[k].replace('?',"")

for qn in quesList:
	k = qn.split(".")
	strlist=[]
	string=""
	for i in k:
		senper+=model.perplexity(i)
	qnper = senper/len(k)
	senper=0
	if(qnper<=300):
		perp300.append(qn)
	elif(qnper>300 and qnper <=500):
		perp500.append(qn)
	elif(qnper>500 and qnper<=750):
		perp750.append(qn)
	elif(qnper>750 and qnper<=1000):
		perp1000.append(qn)
	elif(qnper>1000 and qnper<=1500):
		perp1500.append(qn)
	else:
		above1500.append(qn)
	s+=qnper
	j=j+1
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