import os


def info(param):
    if os.path.isfile(param) is not True:
        raise ValueError("No such file!")
    dictionary = dict()
    dictionary["full_path"] = os.path.abspath(param)
    dictionary["file_size"] = os.stat(param).st_size
    dictionary["file_extension"] = os.path.splitext(param)[1][1:]
    dictionary["can_read"] = os.access(param, os.R_OK)
    dictionary["can_write"] = os.access(param, os.W_OK)

    print(dictionary, sep="\n")


info("D:\FACULTATE\Anul_3_Sem_1\Python\PythonLab\Lab4\ex7.py")
info("D:\FACULTATE\Anul_3_Sem_1\Python\PythonLab\Lab4\ex7.txt")

