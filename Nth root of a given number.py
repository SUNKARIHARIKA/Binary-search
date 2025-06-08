m=27
n=3
''' check from 1 1*1*1=1<27 increment 2*2*2=8<27 increment 3*3*3=27 so the answer is 3 if there is no nth root present for that
particular number then return -1'''
#brute force approach
def Power(i,n):
    ans=1
    for _ in range(n):
        ans=ans*i
    return ans
def Nthroot(m,n):
    for i in range(1,m):
        p=Power(i,n)
        if p==m:
            return i
    return -1
print(Nthroot(m,n))
#the time complexity of brute foce approach is o(m*n)
#optimal solution
def Power1(mid,n,m):
    ans=1
    for i in range(n):
        ans=ans*mid
        if ans>m:
            return 2
    if ans==m:
        return 1
    return 0
low,high=1,m
while low<=high:
    mid=(low+high)//2
    if Power1(mid,n,m)==1:
        print(mid)
        break
    elif Power1(mid,n,m)==2:
        high=mid-1
    else:
        low=mid+1
else:
    print(-1)
