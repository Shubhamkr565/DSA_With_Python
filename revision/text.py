# Write a factorial of a given number

# def factorial(num):
#     if num == 0:
#         return 1
#     if num >=1:
#         result = num * factorial(num-1)
#     return result
# n = 5
# print(factorial(n))

# Write a  program to find the sum of digit

# def sum_of_digits(num):
#     if num ==0:
#         return 0
#     if num>=1:
#         result = int(num%10)+ sum_of_digits(int(num/10))
#     return result

# n = 25
# print(sum_of_digits(n))

# write a program to find the power of number

# def power_of_number(num, power):
#     if power == 0:
#         return 0
#     if power == 1:
#         return num
#     return num* power_of_number(num, power-1)
# print(power_of_number(2,6))

# Write a program to find the HCF 

def fun_HCF(num1, num2):
    result = 1
    for i in range(1, min(num1,num2)+1):
        if num1%i == 0 and num2%i == 0:
            result = i
    return result

print(fun_HCF(3,9)) 
        