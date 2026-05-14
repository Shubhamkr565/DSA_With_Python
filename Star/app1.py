# Prints a right-angled triangle of stars, with each row having one more star than the previous.

def right_angle_triangle(n):
    for i in range(n):
        print("*" * (i+1))

n = 5
right_angle_triangle(n)


# Prints an inverted right-angled triangle, with the first row having the most stars.

def inverted_right_angle_triangle(n):
    for i in range(n):
        print((n-i)* "*")

n = 5
inverted_right_angle_triangle(n)

