# Given an array of integers, calculate the ratios of its elements that are ,Positive,Negative and Zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

arr = [-4, 3, -9, 0, 4, 1]

def calculate_ratios(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for num in arr:
        if num > 0:
            positive_count +=  1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    total_count = len(arr)
    positive_ratio = positive_count / total_count
    negative_ratio = negative_count / total_count
    zero_ratio = zero_count / total_count
    return positive_ratio, negative_ratio, zero_ratio  
def print_ratios(positive_ratio, negative_ratio, zero_ratio):
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")                  
if __name__ == "__main__":
    positive_ratio, negative_ratio, zero_ratio = calculate_ratios(arr)
    print_ratios(positive_ratio, negative_ratio, zero_ratio)
