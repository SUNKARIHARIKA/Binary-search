'''A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt 
(in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
 '''
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
#<---------------brute force approach
#to answer any binary serach related problems first we have to decide the range here we have to decide the range of capacity that is 
#the minimum capacity and the maximum capacity 
'''as it was mentioned in th eproblem for each day the weight of the package should not exceed the capacity so the minimum capacity 
is max(weights) because for example in the above array if we take minimum as 8 we cant ship 9 and 10 because it will exceed the capactity
and the maximum capacity that can be possible is sum(arr) because we can ship all items in one day only thet will nead to minimum days
to ship all packagaes in d days'''
def leastcapacity(weights,days):
    for cap in range(max(weights),sum(weights)+1):
        daysreq=func(weights,cap)
        if daysreq<=days:
            return cap
def func(weight,cap):
    load=0
    day=1
    for i in range(len(weight)):
        if load+weight[i]>cap:
            day+=1
            load=weight[i]
        else:
            load+=weight[i]
    return day
print(leastcapacity(weights,days))
#the time complexity is o(sum-max)+1*o(n)
#<---------Optimal solution
def least(weights,days):
    low,high=max(weights),sum(weights)
    ans=-1
    while low<=high:
        mid=(low+high)//2
        daysreq=func(weights,mid)
        if daysreq<=days:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
print(least(weights,days))
            

