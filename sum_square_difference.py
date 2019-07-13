from collections import defaultdict
d=defaultdict(int)
for i in range(1,10000+1):
	result=i*(i*i-1)*(3*i+2)
	result=result//12
	d[i]=result
print(d[100])
t=int(input())
while t>0:
	n=int(input())
	print(d[n])
	t-=1

