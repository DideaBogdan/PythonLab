import os


def count_ext(my_path):
    ext_tuple = dict()
    if os.path.isfile(my_path):
        fl = open(my_path, 'r')
        content = fl.read()
        print(content[-20:])
    else:
        for root, dirs, files in os.walk(my_path):
            for file in files:
                ext = os.path.splitext(file)
                if ext[1] != "":
                    if ext[1] not in ext_tuple:
                        ext_tuple.setdefault(ext[1], 1)
                    else:
                        ext_tuple[ext[1]] += 1
        ext_tuple = [(k, v) for k, v in ext_tuple.items()]
        ext_tuple = sorted(ext_tuple, key=lambda i: i[1], reverse=True)
        print(ext_tuple, sep="\n")


count_ext("D:\FACULTATE")
