def find_number(text):
    str = ""
    for i in text:
        if i.isdigit() == True:
            str += i
        elif str != "":
            return str

text = input("Enter your string : ")
print(find_number(text))

