def vowels1(text):
    vow = []
    for i in text:
        if i in "aeiou":
            vow.append(i)
    return vow


vowels2 = list(filter(lambda el: el in "aeiou", "Programming in Python is fun"))
vowels3 = [v for v in "Programming in Python is fun" if v in "aeiou"]

print("Result with iteration thru string", vowels1("Programming in Python is fun"))
print("Result with lambda and filter", vowels2)
print("Result with list comprehension??", vowels3)
