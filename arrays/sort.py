# Check if the array is sorted


def sorted_arr(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

def sorted_arr2(arr2):
    for i in range(len(arr2)-1):
        if arr2[i]<arr2[i+1]:
            return False
    return True

arr = [10,20,30,40,50]

arr2 = [50,40,30,20,10]

print("According Order:",sorted_arr(arr))
print("Descending Order:",sorted_arr2(arr2))