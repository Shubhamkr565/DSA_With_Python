# Given an array of integers, where all elements but one occur twice, find the unique element.

def uniqueElement(arr):
        unique = 0
        for num in arr:
                unique ^= num #  XOR cancels out duplicates 
        return unique


arr = [1,2,3,4,3,2,1]


print(uniqueElement(arr))