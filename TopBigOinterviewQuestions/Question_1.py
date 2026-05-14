# What is the runtime of the below code?
# Question 1
# def foo(array):
#     sum = 0
#     product = 1

#     # First loop to calculate the sum of all elements
#     for i in array:
#         sum += i
    
#     # Second loop to calculate the product of all elements
#     for i in array:
#         product *= i

#     # Print the results
#     print(f"Sum = {sum}, Product = {product}")

# # Example usage:
# arr = [1, 2, 3, 4, 5]
# foo(arr)

# Time Complexity : O(N)


# Questio 2

# def printPairs(array):
#     for i in array:
#         for j in array:
#             print(f"{i} , {j}")

# arr = [1,2,3,4,5]
# printPairs(arr)

# Time Complexity : O(N2) N square


# Qestion 3

# def printUnorderPairs(array):
#     for i in range(0, len(array)):
#         for j in range(i+1, len(array)):
#             print(str(array[i])+ "," +str(array[j]))

# arr = [1,2,3,4,5]

# printUnorderPairs(arr)

# Time Complexity : O(N2) 




# Question 4




# def printUnorderPairs(arrayA, arrayB):
#     for i in range(len(arrayA)):
#         for j in range(len(arrayB)):
#             if arrayA[i]< arrayB[j]:
#                 print(str(arrayA[i])+ "," + str(arrayB[j]))


# arrayA = [1,2,3,4,5]
# arrayB = [6,7,8,9,10]

# a = len(arrayA)
# b = len(arrayB)

# printUnorderPairs(arrayA , arrayB)

# Time Complexity : O(ab)



# Question 5


# def reverse(array):
#     for i in range(0, int(len(array)/2)):
#         other = len(array)-i -1
#         temp = array[i]
#         array[i] = array(other)
#         array(other) = temp
#     print(array)


# arr = [1,2,3,4,5]
# reverse(arr)

# Time Complexity : O(N)



