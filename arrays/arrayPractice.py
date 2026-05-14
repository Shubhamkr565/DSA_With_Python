# 1. Create an array and traverse.

from array import *
# my_arr = array('i',[1,2,3,4,5])

# for i in my_arr:
#     print(i)


# 2. Access individual elements through indexs.

# my_arr1 = array('i',[10,20,30,40,50])

# for i in range(0, len(my_arr1)):
#     print(f"index no = {i} and value is {my_arr1[i]}")
# # another 

# print(my_arr1[0])
# print(my_arr1[3])


# 3. Append any value to the array using append() method


my_arr = array('i',[10,20,30,40,50])
my_arr.append(100)
print(my_arr)

# 4. Insert value in an array using insert() method

print("step 4")
my_arr.insert(0,200)    # 0 is the index number and 200 is the value at position 0
print(my_arr)

# 5. Extend python array using extend() method

print("step 5")
my_arr1 = array('i',[100,200,300,400])
my_arr.extend(my_arr1)
print(my_arr)
# 6. Add items from list into array using fromList() method
print("Step 6")
tempList = [25,50,75]
my_arr.fromlist(tempList)
print(my_arr)

# 7. Remove any array element using remove() method
print("Step 7")
my_arr.remove(25)
print(my_arr)

# 8. Remove list array element using pop() method

print("setp 8")
my_arr.pop()
print(my_arr)

# 9. Fetch any element through its index using index() method
print("Step 9")
print(my_arr.index(20))

#10. Reverse a python array using reverse() method
print("step 10")
my_arr.reverse()
print(my_arr)

#11. Get array buffer information through buffer_info() method
print("step 11")
print(my_arr.buffer_info())

#12. Check for number of occurrences of an element  using count() method
print("Step 12")
print(my_arr.count(100))


#13. Convert array to a python list with same elements using tostring() method
print("Step 13")

#14. Convert array to a python list with same elements using tolist() method
print("Step 14")
print(my_arr.tolist())

#15. Append a string to char array using fromstring() method
#16. Slice Elements from an array

print("Step 16")
print(my_arr[1:4])