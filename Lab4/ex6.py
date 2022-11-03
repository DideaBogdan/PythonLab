import os

def callback(param):
    if param == ValueError:
        raise ValueError("Target must be a directory!")
    if param == Exception:
        raise OSError("File can't be opened!")



def search(target, to_search, callback):
    result = []
    if os.path.isdir(target) is False:
        callback(ValueError)
    for root, dirs, files in os.walk(target):
        for file in files:
            try:
                fl = open(file, 'r')
                rd = fl.read()
            except OSError:
                callback(OSError)
            index = rd.find(to_search)
            if index != -1:
                result.append(file)
    print(result)



search("D:\FACULTATE\Anul_3_Sem_1\Python\PythonLab\Lab4", "ex", callback)
search("D:\FACULTATE\Anul_3_Sem_1\Python\PythonLab\Lab4\ex1.py", "ex", callback)
