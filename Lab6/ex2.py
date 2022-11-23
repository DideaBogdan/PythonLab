import re

def findSubs(regex, txt, x):
    r = re.compile(regex)
    result = r.findall(txt)
    print("Toate match-urile:", result)
    result = list(filter(lambda y: len(y) == x, result))
    print(f"Cele de lungime {x}:", result)


findSubs("a+", "Lista de a-uri de lungimi diferite: a, aa, aaa, aaaaa, aa, aaa", 5)
