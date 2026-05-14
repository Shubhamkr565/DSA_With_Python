from array import*

                                # Creating an array

# arr1 = array("i", [1,2,3,4,5])
# print(arr1)
# print(type(arr1))




                                    # Insertion

# arr1 = array("i",[1,2,3,4,5])
# arr1.insert(5,20)  # 5 is the last index of the array, 20 is the value at index no 5.
# print(arr1)
# arr1.insert(0,100)
# print(arr1)
# # Insertion , when an array is full.
# arr1.insert(8,900)
# print(arr1)
# arr1.insert(9,300)
# print(arr1)



                                # Array traversal


# def traverseArray(array):
#     for i in array:
#         print(i)

# def traverseArray(array):
#     for i in range(0,len(arr1)):
#         # print(i)            # printing the index no.
#         # print(arr1[i])      # print the value inside index no
#         print(i, arr1[i])

# arr1 = array("i",[10,20,30,40,50])
# traverseArray(arr1)

# Time Complexity : O(n)
# Space Complexity : O(1)

                                # Access an element of Array

# def accessArray(array, index):
#     if index >= len(array):
#         print("There is not any element in this array")
#     else:
#         print(array[index])

# arr1 = array("i",[10,20,30,40,50])
# accessArray(arr1,2)  
# Time Complexity : O(1)
# Space Complexity : O(1)


                                    # Finding an element

# def searchInArray(array, value):
#     for i in array:
#         if i == value:
#             return array.index(value)
#     return "The element does not exits in this array"

# arr1 = array("i",[10,20,30,40,50])
# result =  searchInArray(arr1, 40)
# print(f"Index number = {result}")
# Time Complexity : O(n)
# Space Complexity : O(1)



                                            # Deletion

# arr1 = array("i",[10,20,30,40,50])
# arr1.remove(40)
# print(arr1)
# Time Complexity : O(n)
# Space Complexity : O(1)

# In Python arrays, deletion of elements is allowed using the remove() method. When an element is removed, the subsequent elements are shifted to fill the gap, maintaining the array's structure without any empty spaces.

