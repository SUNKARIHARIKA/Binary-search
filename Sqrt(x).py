'''The key insight when applying binary search on answers (also called binary search on the result or binary search on the solution space) is:
You're searching for the smallest or largest value that satisfies a given condition, rather than searching through a sorted array.'''
#problem statement -we have to find the square root of x
#in other words we have to find the maximum value the squaring value is lesser than equal to x
#brute force approach
n=28
ans=1
for i in range(1,n+1):
    if i*i<=n:
        ans=i
    else:
        break
print(ans)
#the time complexity is o(n)
#the space complexity is o(1)
#optimal approach
low,high=1,n
def Sqrt(n,low,high):
    answer=1
    while low<=high:
        mid=(low+high)//2
        if (mid*mid)<=n:
            answer=mid
            low=mid+1
        else:
            high=mid-1
    return answer
print(Sqrt(n,low,high))
'''Tracing 
low=1 high=28 firstly initialize the range of which the answer lies
answer=1 1<=28----->enters loop
mid=(29)/2 mid=14
we have check the condition with the mid the square of mid should be lesser than equal to n then that might be my possible anser
14*14>28 then mid and after mid will not produce the square root so i have to remove the right search space high=mid-1 high=13
1<=13---->enters loop
mid=(14)/2 mid=7
7*7>28 means mid and after mid search space should be removed high=mid-1 high=7-1 high=6
1<=6----->enters loop
mid=7//2 mid=3
3*3=9 which may be my answer why because the square value is lesser than n so i have to find maximum integer answer=3 low=mid+1
low=4 high=6
4<=6----->enters loop
mid=5 5*5=25<=28 this might be my answer better than 3 so store it answer=5 low=mid+1 low=6 high=6
6<=6---->enters loop
mid=6 6*6=36>28 this will not be the valid condition high=mid-1 high=5
high>low breaks the loop returns answer as 5 '''

