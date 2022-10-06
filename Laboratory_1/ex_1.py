def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

def MGCD(x):
    if x[-1] == 0:
        return x[-1]
    index = 0
    while len(x) > 1:
        print("Greatest common divisor of (" , x[index], ",", x[index+1], ") =", GCD(x[index], x[index+1]))
        x.insert(0, GCD(x[index], x[index + 1]))
        x.pop(index+1)
        x.pop(index+1)

        print(index,"  ",x)

x = [int (x) for x in input("Enter numbers: ").split()]
MGCD(x)
