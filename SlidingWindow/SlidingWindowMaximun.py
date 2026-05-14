# find the maximum element in each window
 # using Brute Force

# array = [5,3,6,2,8,0,4,1]

# k = 3

# for i in range(len(array) - k+1):
#     max_num = array[i]

#     for j in range(i, i+k):
#         if array[j] > max_num:
#             max_num = array[j]
#     window_number = array[j-k+1 : j+1]
#     print(f"{window_number} -> {max_num}")

 
# Optimized approach

array = [5,3,6,2,8,0,4,1]
k = 3

for i in range(len(array)-k+1):
    window = array[i: i+k]

    max_num = window[0]

    for j in window:
        if j > max_num:
            max_num = j

    print(f"{window} -> {max_num}")