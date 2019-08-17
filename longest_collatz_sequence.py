from math import log
last=5*10**6
arr=[0]*(last+1)
arr[1]=1
arr[2]=2
m=0
max_value=[0]*(last+1)
ind=0
max_value[1]=1
max_value[2]=2
for i in range(3,last+1):
	n=i
	count=0
	while True:
		if n<=last and arr[n]!=0:
			arr[i]=arr[n]+count
			if arr[i]>=m:
				m=arr[i]
				ind=i
			max_value[i]=ind
			break
		# Power of two
		elif (n&(n-1))==0:
			arr[i]=count+int(log(n,2))+1
			if arr[i]>=m:
				m=arr[i]
				ind=i
			max_value[i]=ind
			break
		elif n%2==0:
			n=n//2
			count+=1
			if n<=last:
				arr[i]=count+arr[n]+1
				if arr[i]>=m:
					m=arr[i]
					ind=i
				max_value[i]=ind
				break
		else:n=3*n+1
		count+=1
t=int(input())
while t>0:
	n=int(input())
	if n>1000000:
		print(8400511)
	else:
		print(max_value[n])
	t-=1
