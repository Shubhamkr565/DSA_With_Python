# Reverse the array

def reverse_arr(arr):
    start = 0
    end = len(arr)-1
    # while start < end:
    #     temp = arr[start]
    #     arr[start] = arr[end]
    #     arr[end] = temp
    #     start += 1
    #     end -= 1
    # return arr

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -= 1
    return arr



arr = [10,20,30,40,50]
print(reverse_arr(arr))