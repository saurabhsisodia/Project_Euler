from collections import defaultdict
d=defaultdict(bool)
p=[]
l=0
for i in range(999,100,-1):
	for j in range(i,100,-1):
		mul=i*j
		if str(mul)==str(mul)[::-1] and d[mul]==False:
			p.append(mul)
			l+=1
p.sort()
t=int(input())
for _ in range(t):
	n=int(input())
	for i in range(l-1,-1,-1):
		if p[i]<n:
			print(p[i])
			break
