import os


def absolute_paths(dir, file):
    fl = open(file, "w")
    for files in os.listdir(dir):
        if files[0] == "a":
            fl.write(os.path.abspath(files))


absolute_paths("D:\FACULTATE\Anul_3_Sem_1\Python\PythonLab\Lab4", "ex2.txt")
