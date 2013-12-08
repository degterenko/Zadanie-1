text = "random text"
a=0
b=3
c=0
otvet=-1
while True:
	a+=1
	b+=1
	if text[a:b]=="zip":
		c+=1
	if text[a:b]=="zip":
		if c==2:
			otvet=a
	if text[-1]==text[b]:
		break
print otvet