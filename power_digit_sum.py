x=10**4
a=[0]*(x+1)
a[1]=2
for i in range(2,x+1):
	if i%2==0:
		a[i]=a[i//2]*a[i//2]
	else:
		a[i]=a[i//2]*a[i//2+1]

t=int(input())
while t>0:
	n=int(input())
	s=str(a[n])
	sum=0
	for v in s:
		sum+=int(v)
	print(sum)
	t-=1
	
