# Prints an inverted right-angled triangle, with the first row having the most stars.

def inverted_right_angle_triangle(n):
    for i in range(n):
        print((n-i)* "*")

n = 5
inverted_right_angle_triangle(n)