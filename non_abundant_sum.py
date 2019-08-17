from math import sqrt
def factors(n):
	sum=1
	for i in range(2,int(sqrt(n))+1):
		if n%i==0:
			if n//i==i:
				sum+=i
			else:
				sum+=i+n//i
	return sum

def find(abundant,n,l):
	start,end=0,l-1
	while start<=end:
		if abundant[start]+abundant[end]==n:
			return True
		elif abundant[start]+abundant[end]<n:
			start+=1
		else:
			end-=1
	return False

abundant=[]
l=0
for i in range(12,10**5+1):
	check=factors(i)
	if check>i:
		l+=1
		abundant.append(i)

'''ans=[]
for i in range(24,10**5+1):
	if find(abundant,i,l):
		ans.append(i)
print(ans)'''
t=int(input())
while t>0:
	n=int(input())
	if find(abundant,n,l):
		print("YES")
	else:
		print("NO")
	t-=1


