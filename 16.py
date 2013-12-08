x=31.14159
s=str(x)
b=0
while s[b+1]!='.':
	otvet=s[b]
	b+=1
while s[b+1]=='.':
	if int(s[b+2])<5:
		print otvet+s[b]
	else:
		print otvet+str(int(s[b])+1)
	break
