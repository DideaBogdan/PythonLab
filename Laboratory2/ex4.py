def music(x, y, st):
    res = [x[st]]
    for index in y:
        st += index
        if st >= len(x):
            st -= len(x)
        if st < 0:
            st = len(x) + st
        res.append(x[st])
    return res


x = ["do", "re", "mi", "fa", "sol"]
y = [1, -3, 4, 2]
st = 2
print(music(x, y, st))
