import re


def match_at_least_one(txt, regex_list):
    result = set()
    for reg in regex_list:
        r = re.compile(reg)
        st = r.findall(txt)
        result.update(st)
    print(result)


match_at_least_one("Ceva text ca nu am inspiratie, poate merge si un numar gen 123456", ["[aeiou]+", "[0-9]+"])
