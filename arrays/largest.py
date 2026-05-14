# Find the second largest element


def largest_ele(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        if arr[i] > temp:
            temp = arr[i]
    return temp

arr = [10,40,20,65,4,22]
print(largest_ele(arr))