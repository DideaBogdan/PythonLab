def to_lower_underscore(s):
    str = s.lower().replace(" ", "_")
    return str


text = input("Enter your string : ")
print(to_lower_underscore(text))
