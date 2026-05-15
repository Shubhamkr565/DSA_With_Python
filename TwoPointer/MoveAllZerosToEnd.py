# Move all zeros to end

array = [0,1,0,3,12]

j = 0

for i in range(len(array)):
    if array[i] != 0:
        array[j], array[i] = array[i], array[j]

        j += 1
print(array)
