# Remove Duplicates from sorted array

array = [1,1,2,2,3,4,4]
i = 0
for j in range(1, len(array)):
    if array[i] != array[j]:
        i += 1
        array[i] = array[j]

print(array[: i+1])
 