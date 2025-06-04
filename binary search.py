#binary search is an efficient algorithm for finding the eleemnt in the sorted list
#instead  of checking every item like linear search the search space is reduced to half 
#we can use binary search when the array is sorted or roatted sort array
arr=[1,2,3,4,5,6]
# array is in sorted order we can apply binary serach to search an eleemnt in the array
ele=5
left,right=0,len(arr)-1
found=False
#assign two pointers one is at the start of array and the other is at the end of the array
while left<=right:
    mid=(left+right)//2
    if arr[mid]==ele:
        print(mid)
        found=True
        break
    elif ele<arr[mid]:
        right=mid-1
    else:
        left=mid+1
if not found:
    print('-1')
'''tracing
arr=[1,2,3,4,5,6] ele=5 left=0 right=len(arr)-1   right=5
 iteration 1: 0<5(True) enters loop
              mid=(0+5)//2
              mid=2
              arr[mid]=arr[2]=3
              we have to compare the mid value with the element we have to search to decide the search space
              arr[mid]=3!=ele
              ele<arr[mid](3)  5<3(False)
              ele>arr[mid](3)  5>3(True)   means the element is present on the right side of the array so there is no need to search 
              on the left side we have remove that search space so we assign left=mid+1 the reason is the element is not equal to mid and
              it is greater than mid so the search space is from mid+1 to lenght of the array
iteration 2: left=mid+1 left=3 right=5
             arr[left](4)<arr[right](6)  enters loop
             now we have to find the mid value on the right subarray
             mid=3+5//2=4
             arr[mid]=arr[4]=5
             5==ele(5)
             print(mid) 4 break the loop
'''

