# Write a program to find the biggest number in this array

arr = [23,45,89,56,34,75,83,22]



def biggest_number():
    biggest = 0
    for i in range(len(arr)):
        if biggest < arr[i]:
            biggest = arr[i]
    return biggest

biggest = biggest_number()

print(biggest)