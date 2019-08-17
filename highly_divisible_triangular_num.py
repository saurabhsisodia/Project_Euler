'''from collections import defaultdict
from math import sqrt
from operator import itemgetter
def p_decomposition(n):
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
	count=1
	for e in d.values():
		count=count*(e+1)
	return count
i=1
check=True
find=set()
tr=defaultdict(int)
while check:
	t=i*(i+1)//2
	d=p_decomposition(t)
	if d not in find:
		find.add(d)
		tr[d]=t
	if d>1000:
		check=False
	i+=1
a=[]
for k in tr:
	a.append((k,tr[k]))
a.sort(key=itemgetter(1,0))
print(a)
'''
def triangular_number(n):
	return n*(n+1)//2
a=[(1,1),(2,2), (3,4), (7,6), (8,9), (15,16), (24,18), (32,20), (35,24), (63,36), (80,40), (104,48), (224,90), (384,112), (560,128), (935,144), (1224,162), (1664,168), (1728,192), (2015,240), (2079,320), (5984,480), (12375,576), (14399,648), (21735,768), (41040,1024)]
t=int(input())
while t>0:
	n=int(input())
	for number,div in a:
		if div>n:
			print(triangular_number(number))
			break
	t-=1
