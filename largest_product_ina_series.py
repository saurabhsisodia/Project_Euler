def if_zero(j,k,number):
	p=1
	for i in range(j,j+k):
		p=p*int(number[i])
	return p
def fun(number,n,k):
	max_p=1
	for i in range(k):
		max_p=max_p*int(number[i])
	previous=max_p
	for i in range(n-k):
		if number[i]!='0' and previous!=0:
			next_p=(previous*int(number[i+k]))//int(number[i])
			max_p=max(max_p,next_p)
			previous=next_p
		else:
			p=if_zero(i+1,k,number)
			previous=p
			max_p=max(max_p,p)
	return max_p
t=int(input())
while t>0:
	n,k=map(int,input().split( ))
	number=input()
	print(fun(number,n,k))
	t-=1
