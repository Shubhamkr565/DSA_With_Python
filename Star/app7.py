# Diamond Star Pattern

# **Description**: Combines a pyramid and an inverted pyramid to form a diamond shape.

def diamond_star(n):
    for i in range(n):
        print("   "* (n-i-1) + " * " *(2*i-1))
    for i in range(n-1,-1,-1):
        print("   "*(n-i-1) + " * " * (2*i-1))

n = 5
diamond_star(n)