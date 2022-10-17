def fibo(n):
    x = [0, 0, 1]
    i = 2
    while len(x) <= int(n):
        x.append(x[i]+x[i-1])
        i += 1
    return x


numb = input("Insert number for Fibonacci string:")
print("The first", numb, "-th numbers of the Fibonacci string is", fibo(numb))
