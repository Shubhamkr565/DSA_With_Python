#  Prints a centered pyramid (triangle) of stars, with spaces used for alignment.

def pyramid(n):
    for i in range(n):
        print(" "* (n-i-1) + "*" * (2*i-1))

n = 5
pyramid(n)