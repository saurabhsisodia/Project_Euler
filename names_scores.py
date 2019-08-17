from collections import defaultdict
d=defaultdict(int)
t=int(input())
n=t
a=[]
while t>0:
	a.append(input())
	t-=1

a.sort()
for i in range(n):
	d[a[i]]=i+1
q=int(input())
while q>0:
	s=input()
	ans=0
	for v in s:
		ans+=ord(v)-ord('A')+1
	print(ans*d[s])
	q-=1

