#floor-larget number in the array that is lesser or eqaul to the given number
#ceil-smallest number in the array that is greater or equal to the given number
arr=[10,20,30,40,50]
#if target=25 the floor is 20
#the ciel is 30
#if arr=[10,20,25,30,40] and target=25 then ceil and floor values are equal to 25
#<------Floor------>
target=25
low,high=0,len(arr)-1
def Floor(arr,low,high,target):
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=target:
            ans=arr[mid]
            low=mid+1
        else:
            high=mid-1
    return ans
print(Floor(arr,low,high,target))
low1,high1=0,len(arr)-1
def Ceil(arr,low1,high1,target):
    ans1=-1
    while low1<=high1:
        mid=(low1+high1)//2
        if arr[mid]>=target:
            ans1=arr[mid]
            high1=mid-1
        else:
            low1=mid+1
    return ans1
print(Ceil(arr,low1,high1,target))
        


    
