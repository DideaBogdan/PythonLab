import re


def is_CNP():
    r = re.compile('[1-9][0-9]{2}(0[0-9]|1[0-2])((0[1-9]|[1-2][0-9])|3[0-1])[0-9]{6}')
    cnp = input("Validati CNP: ")
    if r.match(cnp):
        print("CNP valid!")
    else:
        print("CNP invalid!")


is_CNP()
