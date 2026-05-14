# Write a program to find maximum number of vowel in subString

s = "Hello, My Name is Shubham "
k = 3
vowel = "aeiouAEIOU"
max_num_of_vowel = 0
count = 0
for i in range(k):
    if s[i] in vowel:
        count += 1
max_num_of_vowel = max(max_num_of_vowel, count)
print(f"{s[0:k]} -> {count} vowel")

for j in range(k, len(s)):
    # remove outgoing char
    if s[j-k] in vowel:
        count -= 1
    
    # add incoming char
    if s[j] in vowel:
        count += 1
    max_num_of_vowel = max(max_num_of_vowel, count)

    window = s[j-k+1 : j+1]
    print(f"{window} -> {count} vowel")

print("\nMaximum vowels in any substring:", max_num_of_vowel)