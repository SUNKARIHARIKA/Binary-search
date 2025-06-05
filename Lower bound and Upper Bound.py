#Lower Bound
#the array should be sorted to apply lower bound
#lower bound is the smallest index where the element at that index is greater than or equal the give value arr[index]>=x
arr=[3,5,8,15,19]
#x=8   then the lower bound is 2
#x=9   then the lower bound will be 3
#x=20  then lower bound=5(hypothetical)
#brute force
i=0
x=20
n=len(arr)
while i<n and arr[i]<x:
    i+=1
print(i)
#the time complexity is o(n)
#optimal approach for finding the lower bound
'''arr1=[1,2,3,3,5,8,8,10,10,11]
target=9
low,high=0,len(arr1)-1
def LowerBound(arr1,low,high,target):
    ans=len(arr1)  #store the hypothetical value
    while low<=high:
        mid=(low+high)//2
        if arr1[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
print(LowerBound(arr1,low,high,target))
#the time complexity is o(log n)(base 2)'''
'''Tracing
low=0 high=9 target=9
ans=10
low(0)<=high(9) enters loop
iteration 1: mid=(0+9)//2
             mid=4
             arr[mid]=5 arr[mid]>=target
             5>=9(FALSE)
             low=6
iteration 2: low=6 high=9 (6<=9) enters loop
             mid=(6+9)//2 mid=6
             arr[mid]=8
             arr[mid]>=target
             8>=9(False)
             low=7
iteration 3: low=7 high=9 (7<=9) enters loop
             mid=(7+9)//2 mid=8
             arr[mid]=10
             arr[mid]>=target
             10>=9
             ans=8
             high=7
iteration 4: low=7 high=7 (7<=7) enters loop
             mid=(7+7)//7 mid=7
             arr[mid]=10
             arr[mid]>=target
             10>=9
             ans=7
             high=6
iteration 5:low=7 high=6 
            high>low loop breakss-------'''
#<----Upper Bound
#upper bound is also implemented when the array is sorted
#the smallest index such that it is strictly greater than given element arr[index]>x
arr2=[2,3,6,7,8,8,11,11,12]
#if x=6 smallest index is 3
#if x=11 smallest index is 8
#if x=12 smallest index is 9
target=11
low,high=0,len(arr2)-1
def UpperBound(arr2,low,high,target):
    ans1=len(arr2)
    while low<=high:
        mid=(low+high)//2
        if arr2[mid]>target:
            ans1=mid
            high=mid-1
        else:
            low=mid+1
    return ans1
print(UpperBound(arr2,low,high,target))
#the time complexity is o(log n)(base 2)
