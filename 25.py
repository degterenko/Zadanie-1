# def 
a=3
b=1
def sp(a,b):
	c=1 
	while c<=a:
		print str(b)+'*'+str(c)+'='+str(c*b)
		c+=1
while b<=a:
	sp(a,b)
	b+=1