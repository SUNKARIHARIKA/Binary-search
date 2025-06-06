#binary search is an efficient algorithm for finding the elemnt in the sorted list
#instead  of checking every item like linear search the search space is reduced to half 
#we can use binary search when the array is sorted or roatted sort array
#key concept:binary search is all about eliminating the half of the search space by comparing the target element with mid value
#if we want to search an element with linear search the time complexity is o(n) where as it is reduce to o(logn) by using the binary search
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
#recursive approach of binary search
arr1=[3,4,6,7,9,12,16,17] #the array is sorted we can apply binary search
target=13
left,right=0,len(arr1)-1
def BinarySearch(arr1,left,right,target):
    mid=(left+right)//2
    if left>right:
        return -1  #if element is not found
    elif arr1[mid]==target:  #if the middle element is target
        return mid
    elif target>arr1[mid]:   #if target is greater than mid left search space is removed
        return BinarySearch(arr1,mid+1,right,target)
    else:     #if target is less than mid right search space is removed
        return BinarySearch(arr1,left,mid-1,target)
print(BinarySearch(arr1,left,right,target))
#Understanding the time complexity of the binary search
'''For example if the size of the array is 32 initially then the next search space will be 32//2 near around 16
32 --> 16 --> 8 --> 4 --> 2 -->1 heare there are 6 steps or 6 iteration to complete a binary serach of 34 size array
which is equivalent to log32(base2)  log(2**5)(base2)  5log(2)(base2)  5
'''
#the time complexity is o(log n)(base2)
