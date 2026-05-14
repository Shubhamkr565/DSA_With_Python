# Write a program to find the sum of all elements in an array.

def sum_of_array(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum




arr = [1, 2, 3, 4, 5]
result = sum_of_array(arr)
print(result)