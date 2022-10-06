def count_vowels(s):
    vowels = 'aeiou'
    count = 0
    s.lower()
    for vowel in vowels:
        for character in s:
            if vowel == character:
                count = count + 1
    return count


text = input("Enter your string : ")
print(count_vowels(text))
