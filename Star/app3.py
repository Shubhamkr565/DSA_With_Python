# Prints a right-angled triangle aligned to the left, with spaces before stars to create a right-aligned effect.

def left_triangle(n):
    for i in range(n):
        print(" "* (n-i-1) + (i+1)*( "*"))
        # print("*")


n = 5
left_triangle(n)