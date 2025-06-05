'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index
 where it would be if it were inserted in order.
 Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4'''
#brute force approach
nums=[1,3,5,6]
target=5
i=0
n=len(nums)
while i<n and nums[i]<target:
    i+=1
print(i)
#the time complexity of brute force is o(n)
#the space complexity of brute force is o(1)
#optimal approach
'''the lower bound is same as the search insert position we have to return the smallest index which is greater than or eqaul to the target
'''
ans=len(nums)
low,high=0,len(nums)-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]>=target:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)
