'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].'''
nums = [5,7,7,8,8,10]
target = 8
#brute force approach
first=-1
last=-1
n=len(nums)
for i in range(len(nums)):
    if nums[i]==target:
        if first==-1:
            first=i
        last=i
print('first occurence',first)
print('last ocurence',last)
#the time complexity is o(n)
#the space complexity is o(1)
#optimal approach
#the lower bound is the first occurence and the upper bound-1 is the last occurence in the array
low,high=0,len(nums)-1
def LowerBound(nums,low,high,target):
    ans=len(nums)  #store the hypothetical value
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
def UpperBound(nums,low,high,target):
    ans=len(nums)
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
lb=LowerBound(nums,low,high,target)
if lb==len(nums) or nums[lb]!=target:
    print([-1,-1])
else:
    print([lb,UpperBound(nums,low,high,target)-1])
#the time complexity for the lower bound is o(log n)(base 2)
#the space complexity for the upper bound id o(log n)(base 2)
#the total time complexity is 2*o(log n)--->o(logn)
#<----First and last occurence using Binary search----->
arr=[2,8,8,8,8,8,11,13]
target=8
low,high=0,len(arr)-1
def FirstOccurence(arr,low,high,target):
    first=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            first=mid
            high=mid-1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return first
def LastOcuurence(arr,low,high,target):
    last=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            last=mid
            low=mid+1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return last
fo=FirstOccurence(arr,low,high,target)
if fo==-1:
    print([-1,-1])
else:
    print([fo,LastOcuurence(arr,low,high,target)])
