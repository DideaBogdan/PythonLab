def count_characters(text):
    count = {}
    for i in text:
        count[i] = text.count(i)
    print(count)


text = input("Enter your string : ")
count_characters(text)
