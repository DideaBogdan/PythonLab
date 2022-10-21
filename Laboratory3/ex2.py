def how_many_occ(text):
    dictionary = dict()
    for char in text:
        how_many = text.count(char)
        text = text.replace(char, "")
        if how_many != 0:
            dictionary.setdefault(char, how_many)
    print(dictionary)


how_many_occ("hello world!")