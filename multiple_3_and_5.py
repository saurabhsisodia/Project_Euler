def fun(n):
	if n%3!=0:
		n3=n//3
	else:
		n3=n//3-1
	if n%5!=0:
		n5=n//5
	else:
		n5=n//5-1
	if n%15!=0:
		n35=n//15
	else:
		n35=n//15-1
	s3=n3*(3+n3*3)//2
	s5=n5*(5+n5*5)//2
	s35=n35*(15+n35*15)//2
	return s3+s5-s35

t=int(input())
while t>0:
	n=int(input())
	print(fun(n))
	t-=1
