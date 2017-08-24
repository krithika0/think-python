def puzzle():
	diff=0
	while diff<100:
		i=0
		count=0
		while i<100:
			if(str(i).zfill(2)[::-1]==str(i+diff)):
				count+=1
				print(i,i+diff)
			i+=1
		if count>0:
			print("for difference in age of",diff,"ages are reversed",count,"times")
		diff+=1
puzzle()
