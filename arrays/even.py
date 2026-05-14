

def count_evens(nums):
    count = 0
    for i in range(len(arr)):
        if arr[i]%2==0:
            count += 1
    return count

arr = [1, 4, 6, 7, 9, 10]
print(count_evens(arr))