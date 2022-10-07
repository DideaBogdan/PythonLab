def count_words(text):
    res = text.count(" ")
    return res+1


text = input("Enter your string : ")
print("Your text has", count_words(text), "words.")