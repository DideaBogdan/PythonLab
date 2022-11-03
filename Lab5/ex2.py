import kwargs



def my_function(*args, **kwargs):
    global tot
    tot = sum(filter(lambda el: el, kwargs.values()))
    summ = 0
    for k, v in kwargs.items():
        summ += v
    return summ


print("Sum with my_function:", my_function(1, 2, c=3, d=4))
print("Sum with lambda function:", tot)

