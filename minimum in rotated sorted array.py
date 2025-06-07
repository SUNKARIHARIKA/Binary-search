arr=[4,5,6,7,0,1,2]
#brute force approach
print(min(arr))
#the time complexity is o(n)
#the space complexity is o(1)
#optimal solution
low,high=0,len(arr)-1
def Minimum(arr,low,high):
    mini=float('inf')
    while low<=high:
        mid=(low+high)//2
        #check which part is sorted
        if arr[low]<=arr[mid]:
            #left part is sorted
            mini=min(mini,arr[low])
            low=mid+1
        else:
            #right part is sorted
            mini=min(mini,arr[mid])
            high=mid-1
    return mini
print(Minimum(arr,low,high))
#the time complexity is o(logn)
#the space complexity is o(1)
'''Tracing
arr=[4,5,6,7,0,1,2,3]
mini=INT_MAx
low=0 high=7
0<=7------>enters loop
itration 1: mid=(0+7)//2 mid=3 
            check which part is sorted here arr[low](4)<=arr[mid](7) so left part of the array is sorted
            the minimum is mini=min(INT_MAx,4) mini=4 now we have to remove the left search space because we have finded the minimum
            from left sorted array move to right by low=mid+1 low=4 high=7
4<=7-------->enters loop
iteration 2: mid=(4+7)//2 mid=5
             arr[low](0)<=arr[mid](1) left is sorted
             mini=min(4,0) mini=0 low=mid+1 low=6 high=7
6<=7-------->enters loop
iteration 3: mid=(6+7)//2 mid=6
             arr[low](2)<=arr[mid](2)
             mini=min(0,2) mini=0
             low=mid+1 low=7
7<=7-------->enters loop
iteration 4: mid=7 
             arr[low](3)<=arr[mid](3)
             mini=min(0,3) mini=3
             low=mid+1 low=8
low(8)>high(7)---->breaks the loop return mini(0)'''