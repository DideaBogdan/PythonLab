import re

def find_words(txt):
    res = re.split("[^a-zA-Z0-9]", txt)
    res = [x for x in res if x != ""]
    print(res)


find_words("Gaseste cuvintele aici. Vor fi 6.")