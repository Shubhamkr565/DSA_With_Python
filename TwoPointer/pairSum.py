# Find two numbers whoses sum == target


# This is brute force approach  (O(n²))
# array = [1,2,3,4,6]
# target = 6

# for i in range(len(array)):
#     for j in range(i+1, len(array)):
#         if array[i] + array[j] == target:
#             print(f"{array[i]}", "+", array[j], " = ", target)




# Two Pointer Solution
array = [1,2,3,4,6]
target = 10 

left = 0
right = len(array)-1

while left < right:
    current_sum = array[left] + array[right]

    if current_sum == target:
        print(f"{array[left]} + {array[right]} = {current_sum}")
        break
    
    elif current_sum < target:
        left += 1
    else:
        right -= 1





"""
When Should You Think About Two Pointer?

Use Two Pointer when:

✅ Array is sorted
✅ Need pair/triplet
✅ Reverse operations
✅ Palindrome
✅ Sliding window
✅ Subarray problems
✅ Remove duplicates
"""