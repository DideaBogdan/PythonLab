import re


def censure_vowels(txt):
    r = re.split('[^a-zA-Z0-9]', txt)
    result = str()
    for word in r:
        if re.match('^[aeiou].*[aeiou]$', word):
            for i in range(0, len(word)):
                if i % 2 != 0:
                    word = word[0:i] + '*' + word[i+1:]
        result += word + ' '
    print(result)


censure_vowels("Gaseste aici cuvintele care incep si se termina cu vocale aceasta era avioane")