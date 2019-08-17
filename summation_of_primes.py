from collections import defaultdict
from math import sqrt
x=2*10**6
a=[True]*(x+1)
for i in range(2,int(sqrt(x))+1):
	p=i*i
	k=0
	while p+i*k<=x:
		a[p+i*k]=False
		k+=1
d=defaultdict(int)
d[1]=0
sum=0
d[2]=2
sum=2
for i in range(3,x+1):
	if a[i]:
		sum+=i

	d[i]=sum
print(d[2*10**6])
t=int(input())
while t>0:
	n=int(input())
	print(d[n])
	t-=1

