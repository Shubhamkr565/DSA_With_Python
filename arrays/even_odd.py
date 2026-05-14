# Count Odd and Even Numbers Separately

def count_even_odd(nums):
    Even = 0  
    Odd = 0
    for num in nums:
        if num%2==0:
            Even +=1
        else:
            Odd +=1
    print("Even:",Even)
    print("Odd:",Odd)




nums = [2, 5, 8, 11, 14, 17, 20]
count_even_odd(nums)