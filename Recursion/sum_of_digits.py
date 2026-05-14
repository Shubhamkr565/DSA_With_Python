# How to find the sum of digits of a positive integer number using recursion ?

number = 1123

def sum_of_digits(n):
    assert n>=0 and int(n) == n, "The number has to be positive intergers"
    if n == 0 :
        return 0
    else:
        return int(n%10) + sum_of_digits(int(n/10))

print(sum_of_digits(number))