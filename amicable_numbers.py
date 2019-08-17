#from operator import itemgetter
a=[(284,220),(1210,1184),(2924,2620),(5564,5020),(6368,6232),(10856,10744),(14595,12285),(18416,17296),(76084,63020),(66992,66928),(71145,67095),(87633,69615),(88730,79750)]
#a.sort(key=itemgetter(0))
#print(a)
t=int(input())
while t>0:
	n=int(input())
	sum=0
	for v in a:
		x=v[0]
		y=v[1]
		if x<n:
			sum+=x
		if y<n:
			sum+=y
	print(sum)
	t-=1
'''
from math import sqrt
from collections import defaultdict
def prime_decomposition(n):
	d=defaultdict(int)
	while n%2==0:
		d[2]+=1
		n=n//2
	for i in range(3,int(sqrt(n))+1,2):
		while n%i==0:
			d[i]+=1
			n=n//i
	if n>2:
		d[n]+=1
	t=1
	for p in d:
		e=d[p]
		t*=(p**(e+1)-1)//(p-1)
	return t
x=10**6
s=defaultdict(int)
for i in range(2,x+1):
	s[i]=prime_decomposition(i)-i
arr=[]
for v in s:
	a=s[v]
	b=prime_decomposition(a)-a
	if v==b and a!=b:
		arr.append((a,b))
print(arr)
'''
