# Find Anagrams in String
"""What is an Anagram?

Two strings are anagrams if:

they contain same characters
same frequency
order can be different"""

str = "abcets"
p = "abc"
k = len(p)
count = 0
for i in range(len(str) -k+1):
    # print(f"{str[i:k]}")

    window = str[i:i+k]

    if sorted(window) == sorted(p):
        print(i)