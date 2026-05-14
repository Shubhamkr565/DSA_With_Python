# Maximum sum subarray of size K. 
# using Brute Force

# array = [2,1,5,1,3,2]
# k = 3
# max_sum = 0
# for i in range(len(array)-k+1):
#     window_sum = 0

#     for j in range(i, i+k):
#         window_sum += array[j]

#     max_sum = max(max_sum ,window_sum)
# print(max_sum)

# Optimized Sliding Window

array = [2,1,5,1,3,2]
k = 3

window_size = 0
max_size = 0
left = 0

for right in range(len(array)):
    window_size += array[right]

    if right - left+1 == k:
        max_size = max(max_size, window_size)

        window_size -= array[left]
        left += 1

print(max_size)
