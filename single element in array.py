'''You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which 
appears exactly once.Return the single element that appears only once.
Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10'''
#extreme brute force approach
nums=[1,1,2,3,3,4,4,8,8]
def SingleElement(nums):
    if len(nums)==0:   #if there is only one number that number is single number
        return nums[0]
    for i in range(len(nums)):
        if i==0:  #for the first element compare with the second element if both are different then firt number is single number
            if nums[i]!=nums[i+1]:
                return nums[0]
        elif i==len(nums)-1:  #for the last element compare with last second if both are different last number is a single number
            if nums[i]!=nums[i-1]:
                return nums[len(nums)-1]
        else:    #comparing middle elements
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]
print(SingleElement(nums))
#the time complexity is o(n)
#the space complexity is o(1)
#solution using hashing technique
d={}
for i in nums:
    d[i]=d.get(i,0)+1
for i in d:
    if d[i]==1:
        print(i)
#the time complexity is o(n)
#the space complexity is o(n)
#solution using Bitmanuplation
xor=0
for i in nums:
    xor=xor^i
print(xor)
#the time complexity is o(n)
#the space complexity is o(1)
#solution using Binary search(we are searching single element in sorted array)
def Single(arr,n):
    if (n==1):   #if there is only single elemnt in the array
        return arr[0]
    if (arr[0]!=arr[1]):  #compare first and second
        return arr[0]
    if (arr[n-1]!=arr[n-2]):
        return arr[n-1]
    low,high=1,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid]+1:
            return arr[mid]
        '''eleminate the part where your element is not there
           (even,odd) element is on the right half
           (odd,even) elemnt is on the left half'''
        #we are in left
        if((mid%2!=0 and arr[mid]==arr[mid-1]) or (mid%2==0 and arr[mid]==arr[mid+1])):
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,1,2,2,3,4,4,5,5]
print(Single(arr,len(arr)))
'''Before single element (even,odd)
   After single element (odd,even)'''

