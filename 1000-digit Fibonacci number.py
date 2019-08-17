from math import log,floor
#digit=int(floor(log(n,10))+1)
#from collections import defaultdict
d=[]
d.append(1)
a,b=1,1
p=1
len=1
i=3
c=a+b
while len!=5000+1: 
	x=int(floor(log(c,10))+1)
	if x!=p:
		p=x
		d.append(i)
		len+=1
	i+=1
	a=b
	b=c
	c=a+b
t=int(input())
while t>0:
	n=int(input())
	print(d[n-1])
	t-=1
