# Remove duplicate from sorted array

arr = [1,2,3,4,5,3,4,2,3,65,7,8,5,32]

arr.sort()

def remove_sorted_Array():
    arr2 = []

    for i in range(len(arr)):
        if i ==0 or arr[i] != arr[i-1]:
            arr2.append(arr[i])
    return arr2

arr2 = remove_sorted_Array()

print(arr2)
