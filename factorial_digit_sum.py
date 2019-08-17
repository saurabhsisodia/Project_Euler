a=[0]*(1000+1)
a[0]=1
a[1]=1
for i in range(2,1000+1):
    a[i]=i*a[i-1]
t=int(input())
while t>0:
	n=int(input())
	x=str(a[n])
	sum=0
	for v in x:
		sum+=int(v)
	print(sum)
	t-=1
	
