# Given five positive integers, find the minimum and maximum values that can be 
# calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line 
# of two space-separated long integers.

# arr = [1,2,3,4,5]

# def max_min(arr):
#     max_no = arr[0]
#     min_no = arr[0]

#     for i in arr:
#         if i > max_no:
#             max_no = i
#         if i < min_no:
#             min_no = i

#     print("Max Number: ",max_no)
#     print("Min Number: ",min_no)

#     sum = 0
#     min_sum = 0
#     max_sum = 0

#     for i in arr:
#         sum += i
        
#         max_sum = sum - min_no
#         min_sum = sum - max_no
        
#     print("Max Sum is: ",max_sum)
#     print("Min sun is: ",min_sum)
# max_min(arr)




arr = [1,2,3,4,5]

def miniMaxSum(arr):
    max_no = arr[0]
    min_no = arr[0]
    for i in arr:
        if i > max_no:
            max_no = i
        if i < min_no:
            min_no = i
    sum = 0
    max_sum = 0
    min_sum = 0

    for i in arr:
        sum +=i

        max_sum = sum - min_no
        min_sum = sum - max_no
    print(min_sum, max_sum)

miniMaxSum(arr)        


