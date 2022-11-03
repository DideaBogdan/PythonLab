import os


def unique_ext(path):
    dir_list = os.listdir(path)
    ext = set()
    for file in dir_list:
        result = os.path.splitext(file)
        ext.add(result[1])
    ext = [i[1:] for i in ext]
    print(ext)


unique_ext("D:\STUDENT")
