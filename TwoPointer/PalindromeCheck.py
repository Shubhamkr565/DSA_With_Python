# Palindrome Check

array = [1,2,3,3,2,1]
left = 0
right = len(array)-1

while left < right:
    if array[left] != array[right]:
        print("Not Palindrome")
        break
    left += 1
    right -= 1
else:
    print("Palindrome ")