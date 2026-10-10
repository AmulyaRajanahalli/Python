text = input("Enter a string:")

vowels = "aeiouAEIOU"
vowel_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1

word_count = len(text.split())
char_count = len(text)

print("Number of vowels:",vowel_count)
print("Number of words:",word_count)
print("Number of characters:",char_count) 
