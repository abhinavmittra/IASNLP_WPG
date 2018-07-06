names=["Noah", "Eugenie", "Trent", "Teodora", "Georgie", "Toni", "Tory", "Carrol", "Wayne", "Shelli", "Leta", "Helena", "Katrice", "Lavon", "Charis", "Tamatha", "Bernardina", "Maynard", "Adelaida", "Nicolas"]
s = "Noah had 5 balls with him he gave 3 to Georgie how many balls is left with noah?"

k = s.split()
strlist=[]
string=""
for l,i in enumerate(k):
	# if(l==len(k)-1):
	# 	strlist.append(string)
	# 	strlist.append(i)
	# 	break
	if(i[0].isupper() and i not in names):
		strlist.append(string)
		string=i+" "
	else:
		string+=i+" "	
# if(string not in strlist):
print(string)
strlist[-1]=strlist[-1]+string
strlist = [i.strip() for i in strlist]
print(strlist)		