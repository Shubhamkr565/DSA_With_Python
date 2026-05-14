arr = [
    [11,2,4],
    [4,5,6],
    [10,8,-12]
]

def diagonalDifference(arr):
    sum1 = arr[0][0] + arr[1][1] + arr[2][2]
    sum2 = arr[2][0] + arr[1][1] + arr[0][2]

    print(sum1)
    print(sum2)
    dif = abs(sum1 - sum2)
    return dif

print(diagonalDifference(arr))
