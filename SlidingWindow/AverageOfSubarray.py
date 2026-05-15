# Average of Subarray of size k

# array = [1,4,5,7]

# k = 2
# avg_max_sum = 0

# for i in range(len(array)-k+1):
#     window_sum = 0
#     for j in range(i, i+k):
#         window_sum += array[j]
        
#         avg = window_sum/k
#         avg_max_sum = max(avg_max_sum, avg)
# print(avg_max_sum)





array = [6,4,7,8,3,1]
k = 3
left = 0
avg = 0

max_avg = 0

for i in range(len(array) - k+1):
    window_sum = 0
    
    for j in range(i, i+k):
        window_sum += array[j]

    avg = window_sum/k
    print(f"{array[i: i+k]}", " => ", round(avg, 2))
    max_avg = max(max_avg, avg)

print(max_avg)







