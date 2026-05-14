# Prints an inverted right-angled triangle aligned to the left.

def inverted_left_angled_triangle(n):
    for i in range(n):
        print((" "* i)+ ("*" * (n-i)))

n = 5
inverted_left_angled_triangle(n)