# Write a program to find the HCF of two number:

def find_HCF(a,b):
    for i in range(1, min(a,b)+1):
        if a%i == 0 and b%i == 0:
            result = i
    return result

print(find_HCF(48,18))