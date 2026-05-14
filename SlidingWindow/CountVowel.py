# Count vowels in every substring of size K

# str = "shubham"
# vowels = "aeiou"
# k = 3


# for i in range(len(str)-k+1):
#     count = 0
#     for j in range(i, i+k):
#         if str[j] in vowels:
#             count += 1

#     print(count)


# Optimized Sliding Window

s = "shubham"

vowels = "aeiou"

k = 3

count = 0
left = 0

for right in range(len(s)):

    # add right vowel
    if s[right] in vowels:
        count += 1

    # window reached
    if right - left + 1 == k:

        print(count)

        # remove left vowel
        if s[left] in vowels:
            count -= 1

        left += 1