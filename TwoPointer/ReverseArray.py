# Reverse Array 

array = [1,2,3,4,5,6]

left = 0
right = len(array)-1
# array2 = []
while left <= right:
    array[left], array[right]  = array[right], array[left]

    left += 1
    right -= 1

print(array)