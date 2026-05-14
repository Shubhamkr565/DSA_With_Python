# How to find the sum of digits of a positive integer number using recursion ?

# def sum_of_digits(x):
#     x = abs(x)
#     if x == 0:
#         return 0
#     else:
#         return int(x%10) + sum_of_digits(int(x/10))

# result = sum_of_digits(-111)

# print(f"result is = {result}")  


# How to calculate power of a number using recursion? 


# def power_of_number(base, power):
#     assert power >= 0 and int(power) == power ,"The power must be positive integer"
#     if power == 0:
#         return 1
#     elif power == 1:
#         return base
#     else:
#         return base * power_of_number(base, power-1)
    
# result = power_of_number(2,5)
# print(f"result = {result}")



# How to find GCD (Greatest common divisor) of two numbers using recursion? 

# def gcd(num1,nun2):
#     if num1 < 0:
#         num1 = -1*num1

#     elif num2 < 0:
#         num2 = -1*num2

#     elif num2 == 0:
#         return num1
#     else:
#         return gcd(num2 , num1%num2)

# result = gcd(48,18)
# print(f"result = {result}")

# arrA = [1,2,3,4,5]
# arrB = [6,7,8,9,10]

# for a in arrA:
#     print(a)

# for b in arrB:
#     print(b)


# for a in arrA:
#     for b in arrB:
#         print(a,b)

