from math import sqrt
def fun(n):

	for c in range(1,n):
		if 2*c**2-(n-c)**2>0:
			x=abs(int(sqrt(2*(c**2)-(n-c)**2)))
			a=(n-c+x)//2
			b=(n-c-x)//2
			if a>0 and b>0 and c>0 and a**2+b**2==c**2 and a+b+c==n:
				return a*b*c
	return -1
t=int(input())
while t>0:
	n=int(input())
	print(fun(n))
	t-=1
