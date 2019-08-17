from collections import defaultdict
def fun(n):
    d=defaultdict(bool)
    ans=''
    r=1%n
    while r!=0 and d[r]==False:
        d[r]=True
        r=r*10
        ans+=str(r//n)
        r=r%n
    if r==0:
        return 0
    else:
        x=r
        res=''
        while True:
            r=r*10
            res+=str(r//n)
            r=r%n
            if r==x:
                break
        return len(res)

a=[]
l=0
for i in range(1,10**4+1):
    a.append(fun(i))
    l+=1
m=0
ans=[]
last=1
for i in range(l):
    t=a[i]
    if t>m:
        m=t
        last=i+1
    ans.append((m,last))
t=int(input())
while t>0:
    n=int(input())
    if n>=2:
        print(ans[n-2][1])
    else:
        print(0)
    t-=1
