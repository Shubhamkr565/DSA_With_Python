#  Maximum sum subarray of size K. 

# array = [4,2,6,7,5,7]
# k = 3
# max_sum = 0
# for i in range(len(array)-k+1):
#     window_sum = 0
#     for j in range(i, i+k):
#         window_sum += array[j]

#         max_sum = max(max_sum, window_sum)

# print(max_sum)


# Average of subarray of size k

# array = [4,2,6,7,5,7]
# k = 3
# ave_subArray = 0

# for i in range(len(array) -k+1):
#     window_sum = 0

#     for j in range(i, i+k):
#         window_sum += array[j]

#     ave_subArray = window_sum/k

#     print(ave_subArray)


# optimized approach
# array = [4,2,6,7,5,7]
# k = 3

# window_sum = 0
# for i in range(k):
#     window_sum += array[i]

# print(window_sum)

# for i in range(k, len(array)):
#     window_sum = window_sum -array[i-k] + array[i]

# print(window_sum/k)



#  Maximum sum subarray of size K. 

# Optimized approach

# array = [4,20,6,7,2,9,1]

# k = 3

# window_sum = 0
# max_sum = 0
# for i in range(k):
#     window_sum += array[i]

# # print(window_sum)

# for j in range(k, len(array)):
#     window_sum = window_sum - array[j-k] + array[j]

#     max_sum = max(max_sum , window_sum)

# print(max_sum)





# First negative number in every window

# array = [-2,-5, 6, 7,-9, 4]
# k = 3
# negative_no = []

# for i in range(len(array)- k+1):
#         for j in range(i, i+k):
#             if array[j] < 0:
#                 negative_no.append(array[j])

# for k in range(len(negative_no)):
#     print(negative_no[k])



# optimized approach

# array = [-2,-5, 6, 7,-9, 4]
# k = 3
# negative_no = []
# for i in range(k):
#     if(array[i]<0):
#         negative_no.append(array[i])
# print(negative_no)

# for j in range(k, len(array)):
#     if array[j-k] in negative_no:
#         negative_no.remove(array[j-k])

#     if array[j] < 0:
#         negative_no.append(array[j])

#     print(negative_no)
        




# Count vowels in every substring of size K

# s = "shubham"

# k = 3
# count = 0
# vowel = "aeiouAEIOU"
# for i in range(k):
#     if s[i] in vowel:
#         count += 1
# print(f'"{s[0:k]}" → {count} vowel')
# for j in range(k, len(s)):
#     # remove outgoing char
#     if s[j-k] in vowel:
#         count -= 1
    
#     # add incoming char

#     if s[j] in vowel:
#         count += 1

#     window = s[j-k+1 : j+1]
#     print(f'"{window}" → {count} vowel')






# Maximum sum subarray of size K. 

# array = [6,4,7,8,3,1]
# k = 3
# left = 0
# max_sum = 0

# for i in range(len(array)- k+1):
#     window_sum  = 0
#     for j in range(i, i+k):
#         window_sum += array[j]

#     max_sum = max(window_sum, max_sum)

# print(max_sum)

# array = [6,4,7,8,3,1]
# k = 3
# left = 0
# max_sum = 0
# window_sum = 0

# for right in range(len(array)):
#     window_sum += array[right]

#     if right - left+1 == k:
#         max_sum = max(max_sum,  window_sum)

#         window_sum -= array[left]

#         left += 1
    
# print(max_sum)





# Average of subarray of size k

# array = [6,4,7,8,3,1]
# k = 3
# left = 0
# avg = 0

# max_avg = 0

# for i in range(len(array) - k+1):
#     window_sum = 0
    
#     for j in range(i, i+k):
#         window_sum += array[j]

#     avg = window_sum/k
#     print(f"{array[i: i+k]}", " => ", round(avg, 2))
#     max_avg = max(max_avg, avg)

# print(max_avg)





#  Maximum sum subarray of size K. 

# array = [6,4,7,8,3,1]
# k = 3

# window_sum = 0
# max_sum = 0

# left = 0

# for right in range(len(array)):
#     window_sum += array[right]

#     if right - left+1 == k:
#         print(f"{array[left: right+1]}", " => ", window_sum)
#         max_sum = max(max_sum, window_sum)

#         window_sum -= array[left]

#         left += 1
    

# print(max_sum)




# Count vowels in every substring of size K


str = "Shubham"
k = 3
vowel = "aeiouAEIOU"
left = 0
window_vowerl = []
count = 0

for right in range(len(str)):
    if str[right] in vowel:
        window_vowerl.append(str[right])
        count += 1

    if right - left+1 == k:
        print(f"{str[left: right+1]}", " => ", window_vowerl,"=>", count)
        
        if str[left] in vowel:
            window_vowerl.remove(str[left])
            count -= 1

        left += 1








# str = "Shubham"
# k = 3
# vowel = "aeiouAEIOU"

# for i in range(len(str) - k+1):
#     count = 0
#     for j in range(i, i+k):
#         if str[j] in vowel:
#             count +=1
#     print(f"{str[i:i+k]}", " => ", count)