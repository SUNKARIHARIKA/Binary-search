'''Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, 
and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
The test cases are generated so that there will be an answer.'''
nums = [1,2,5,9]
threshold = 6
#brute foce approach
import math
ans=float('inf')
for i in range(1,max(nums)+1):
    s1=0
    for j in range(len(nums)):
        s1+=math.ceil(nums[j]/i)
    if s1<=threshold:
        ans=min(ans,i)
print(ans)
#the time complexity is o(m*n) where m is the max element and n is the size of array
#the space complexity is o(1)
#optimal approach
import math
ans=-1
low,high=1,max(nums)
while low<=high:
    mid=(low+high)//2
    s2=0
    for i in range(len(nums)):
        s2+=math.ceil(nums[i]/mid)
    if s2<=threshold:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)
