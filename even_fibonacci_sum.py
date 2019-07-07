def fun(n):
	sum=0
	previous=0
	start=2
	while start<n:
		next_even=4*start+previous
		previous=start
		sum+=start
		start=next_even
	return sum


t=int(input())
while t>0:
	n=int(input())
	print(fun(n))
	t-=1
		
