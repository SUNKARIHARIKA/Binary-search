num = 30
low,high=0,num
def PerfectSquare(low,high,num):
    if num<1:
        return num
    while low<=high:
        mid=(low+high)//2
        square=mid*mid
        if square==num:
            return True
        elif square>num:
            high=mid-1
        else:
            low=mid+1
    return False
print(PerfectSquare(low,high,num))