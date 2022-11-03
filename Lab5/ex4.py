def my_function(*args, **kwargs):
    lst = list(
        filter(lambda el: type(el) is dict and len(el) >= 2 and list(filter(lambda k: len(str(k)) >= 3, el.keys())),
               args))
    lst += list(
        filter(lambda el: type(el) is dict and len(el) >= 2 and list(filter(lambda k: len(str(k)) >= 3, el.keys())),
               kwargs.values()))
    print(lst)
    '''
    res = []
    for item in args:
        if type(item) is dict:
            if len(item) >= 2:
                for k in item.keys():
                    if len(str(k)) >= 3:
                        res.append(item)
                        break
    for item in kwargs.values():
        if type(item) is dict:
            if len(item) >= 2:
                for k in item.keys():
                    if len(str(k)) >= 3:
                        res.append(item)
                        break
    print(res)
    '''

my_function({1: 2, 3: 4, 5: 6},
            {'a': 5, 'b': 7, 'c': 'e'},
            {2: 3},
            [1, 2, 3],
            {'abc': 4, 'def': 5},
            3764,
            dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
            test={1: 1, 'test': True})
