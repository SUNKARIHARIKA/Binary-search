'''You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.'''
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
#brute force approach
def Search(matrix,target):
    m=len(matrix) #number of rows
    n=len(matrix[0]) #number of columns
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==target:
                return True
    return False
print(Search(matrix,target))
#the time complexity is o(mn)
#the space complexity is o(1)
#better solution
#since each row in the matrix is sorted  and if we arrange in matrix format the whole matrix is sorted
def search(matrix,target):
    n=len(matrix[0])
    for i in range(len(matrix)):
        if target>=matrix[i][0] and target<=matrix[i][n-1]:
            return BinarySearch(matrix[i],target)
    return False
def BinarySearch(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return True
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return False
print(search(matrix,target))
#the time complexity is o(n)+o(log m)
#the space complexity is o(1)
#optimal solution
def Optimal(matrix,target):
    m=len(matrix)
    n=len(matrix[0])
    low,high=0,(m*n-1)
    while low<=high:
        mid=(low+high)//2
        row=mid//n
        col=mid%n
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]>target:
            high=mid-1
        else:
            low=mid+1
    return False
print(Optimal(matrix,target))
#the time complexity is o(log m)
#the space complexity is o(1)

            
