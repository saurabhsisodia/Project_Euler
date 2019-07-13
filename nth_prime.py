from math import sqrt
x=1000000
prime_array=[True]*(x+1)
for i in range(2,int(sqrt(x))+1):
	if prime_array[i]:
		p=i*i
		k=0
		while p+i*k<=x:
			prime_array[p+i*k]=False
			k+=1
prime=[]
for i in range(2,x+1):
	if prime_array[i]:
		prime.append(i)
t=int(input())
while t>0:
	n=int(input())
	print(prime[n-1])
	t-=1
