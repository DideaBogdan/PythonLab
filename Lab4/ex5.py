import os


def search(target, to_search):
    result = []
    if os.path.isdir(target) is False:
        raise ValueError("Target must be a directory!")
    for root, dirs, files in os.walk(target):
        for file in files:
            try:
                fl = open(file)
                rd = fl.read()
            except Exception as e:
                print("File can't be opened!")
            index = rd.find(to_search)
            if index != -1:
                result.append(file)
    print(result)


search("D:\FACULTATE\Anul_3_Sem_1\Python\PythonLab\Lab4", "ex")
search("D:\FACULTATE\Anul_3_Sem_1\Python\PythonLab\Lab4\ex1.py", "ex")
