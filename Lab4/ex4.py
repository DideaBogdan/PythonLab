import os
import sys


def list_unique():
    unique = set()
    for file in os.listdir(sys.argv[1]):
        file = os.path.splitext(file)[1][1:]
        if file != "":
            unique.add(file)
    print(unique)


list_unique()
