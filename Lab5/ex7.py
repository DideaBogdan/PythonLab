def sum_digits(x):
    return sum(map(int, str(x)))


def process_numbers(**kwargs):
    fib = [0, 1, 1]
    ct = 3
    while ct < 1000:
        fib.append(fib[ct-1]+fib[ct-2])
        ct += 1
    if 'filters' in kwargs.keys():
        for l in kwargs['filters']:
            fib = list(i for i in fib if l(i))
    if 'offset' in kwargs.keys():
        fib = fib[kwargs['offset']:]
    if 'limit' in kwargs.keys():
        print(fib[:kwargs['limit']])


process_numbers(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2, offset=2)
