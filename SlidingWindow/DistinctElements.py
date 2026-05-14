# find the How many distinct (unique) elements are present in every window of size k.


array = [1, 2, 1, 3, 4, 2, 3]
k = 4

for i in range(len(array) -k+1):
    s = set()

    for j in range(i, i+k):
        s.add(array[j])
    
    print(len(s))