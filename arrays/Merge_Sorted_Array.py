# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored 
# inside the array nums1. To accommodate this, nums1 has a length of m + n, 
# where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


num1 = [10,20,30,40]
num2 = [100,200,300,400]
num3 = []
m = len(num1)
n = len(num2)

def merge(num1, num2):
    for i in range(m):
        for j in range(n):
            num3 = num1[i] + num2[j]
    return num3


merge(num1,num2)

print(num3)