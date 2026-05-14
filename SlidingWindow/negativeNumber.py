# First negative number in every window

# array = [1, -3, 5, -2, 4, -7]

# k = 3

# window_neg = []

# for i in range(len(array)-k+1):

#     for j in range(i, i+k):
#         if(array[j] < 0):
#             window_neg.append(array[j])

# for i in range(len(window_neg)-1):
#     print(window_neg[i])


array = [1, -3, 5, -2, 4, -7]

k = 3

for i in range(len(array)-k+1):
    found = False

    for j in range(i, i+k):
        if array[j] < 0:
            print(array[j])
            found = True
            break
    if not found:
        print(0)