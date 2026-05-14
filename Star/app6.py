#  Prints an inverted pyramid, with the widest row at the top.

def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" "* (n-i) + "*" * (2*i-1))

n= 5
inverted_pyramid(n)