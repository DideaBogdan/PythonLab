import os


def list_dir(dir_path):
    if os.path.isdir(dir_path) is False:
        raise ValueError("dir_path must be a directory")
    dir_lst = []
    for file in os.listdir(dir_path):
        if os.path.isfile(file) is True:
            dir_lst.append(os.path.abspath(file))
    print(*dir_lst, sep="\n")


list_dir("D:\FACULTATE\Anul_3_Sem_1\Python\PythonLab\Lab4")
