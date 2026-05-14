arr = [1,2,3,4,5]

def min_max(arr):
    min_num = arr[0]
    max_num = arr[0]

    for i in range(1, len(arr)):
        if min_num > arr[i]:
            min_num = arr[i]
        if max_num < arr[i]:
            max_num = arr[i]

    print("Min_Num : ", min_num)
    print("Max_Num : ", max_num)

    
    total_sum = 0
    min_sum = 0
    max_sum = 0
    for i in range(len(arr)):
        
        total_sum = total_sum+arr[i]
        min_sum = total_sum-max_num
        max_sum = total_sum-min_num
    print("Min_sum: ",min_sum)
    print("Max_sum: ", max_sum)

    
min_max(arr)