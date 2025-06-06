'''You are given a 0-indexed integer array nums and a target element target.
A target index is an index i such that nums[i] == target.
Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an 
empty list. The returned list must be sorted in increasing order.
Example 1:
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
Example 2:
Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.'''
# we can solve the above problem with the time complexities o(nlog n) binary serach and sorting and o(n)
#bruteforce 1
nums=[1,2,5,2,3]
target=2
nums.sort()
l=[]
for i in range(len(nums)):
    if nums[i]==target:
        l.append(i)
print(l)
#the time complexity is o(nlogn) for sorting and o(n) for iteration =>o(nlogn)
#optimal solution
l=[]
count=0
smaller=0
for i in range(len(nums)):
    if nums[i]==target:
        count+=1
    elif nums[i]<target:
        smaller+=1
for i in range(count):
    l.append(smaller)
    smaller=smaller+1
print(l)
#the time complexity is o(n)
#we can also apply binary search
nums=[1,2,5,2,3]
target=2
nums.sort()
low,high=0,len(nums)-1
l=[]
def FirstOccurence(nums,low,high,target):
    first=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            first=mid
            high=mid-1
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return first
def LastOccurence(nums,low,high,target):
    last=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            last=mid
            low=mid+1
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return last
fo=FirstOccurence(nums,low,high,target)
lo=LastOccurence(nums,low,high,target)
for i in range(fo,lo+1):
    l.append(i)
print(l)

        