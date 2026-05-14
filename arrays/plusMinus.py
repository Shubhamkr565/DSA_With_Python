# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with 6 places after the decimal.

arr = [-4, 3, -9, 0, 4, 1]
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0

    for num in arr:
        if num > 0:
            pos += 1
        elif num <0:
            neg += 1
        else:
            zero +=1
    # print("Total positive numbers:", pos)
    # print("Total negative numbers:", neg)
    # print("Total zeros:", zero)

    n = len(arr)
    # print("proportion of positive values: ",pos/n)
    # print("proportion of negative values: ",neg/n)
    # print("proportion of zeros: ",zero/n)

    print("{:.6f}".format(pos/n))
    print("{:.6f}".format(neg/n))
    print("{:.6f}".format(zero/n))

plusMinus(arr)
