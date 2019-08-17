#from itertools import permutations
from math import factorial,ceil
from operator import truediv

ans=''
t=int(input())
while t>0:
	f=12
	s=['a','b','c','d','e','f','g','h','i','j','k','l','m']
	#s=['a','b','c','d']
	n=int(input())
	ans=''
	while n>1:
		i=int(ceil(truediv(n,factorial(f))))
		#print(i)
		ans+=s[i-1]
		#print(ans)
		n=n-factorial(f)*(i-1)
		f-=1
		s.pop(i-1)
		#print(s)
	ans+=''.join(s)
	print(ans)
	t-=1
