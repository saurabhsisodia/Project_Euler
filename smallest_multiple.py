from math import gcd
from collections import defaultdict
d=defaultdict(int)
def lcm(a,b):
	g=gcd(a,b)
	return (a*b)//g
l=lcm(1,2)
d[1]=1
d[2]=l
for _ in range(3,41):
	l=lcm(_,l)
	d[_]=l
#print(d[20])
t=int(input())
while t>0:
	n=int(input())
	print(d[n])
	t-=1
