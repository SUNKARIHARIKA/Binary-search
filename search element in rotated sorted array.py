#the problem statement is we have to search for an element in the rotated array if it was present we have to return the index of that
#element
arr=[7,8,9,1,2,3,4,5,6]
target=1
#brute foce approach
for i in range(len(arr)):
    if arr[i]==target:
        print(i)
        break
#the time complexity is o(n)
#the space complexity is o(1)
#we can reduce the time complexity to o(n) to o(logn)
#optimal approach
low,high=0,len(arr)-1
def search(arr,low,high,target):
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        #if left part is sorted
        if arr[low]<=arr[mid]:
            if arr[low]<=target and target<=arr[mid]:
                #element exsist
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<=target and target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1
print(search(arr,low,high,target))