# Function to calculate the power of a number using recursion
def power_of_number(base, power):
    
    # Base case 1: If the power is 0, any number raised to the power of 0 is 1
    if power == 0:  
        return 1

    # Base case 2: If the power is 1, return the base itself
    if power == 1:
        return base

    # Recursive case: Multiply the base with the result of the function called with (power - 1)
    return base * power_of_number(base, power-1)

# Testing the function with base 2 and power 5
print(power_of_number(2, 5))  # Output: 32
