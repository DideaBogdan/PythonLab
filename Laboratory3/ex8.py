def loop(mapping):
    is_loop = False
    solution = []
    curr_key = mapping.get("start")
    solution.append(curr_key)
    while True:
        curr_key = mapping.get(curr_key)
        if curr_key in solution:
            return solution
        solution.append(curr_key)


mp = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': 'y', 'y': 'start'}
print((loop(mp)))

