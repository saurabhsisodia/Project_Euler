from math import sqrt
def fun(n):
	last=2
	while n%2==0:
		n=n//2
	for i in range(3,int(sqrt(n))+1,2):
		while n%i==0:
			if last<i:
				last=i
			n=n//i
	if n>2:
		if n>last:
			last=n
	return last
t=int(input())
while t>0:
	n=int(input())
	print(fun(n))
	t-=1
