def prime_list(n):
    z = [int(i) for i in n]
    x = [int(i) for i in z if len([y for y in range(2, i//2+1) if i % y == 0]) == 0 and i != 0 and i != 1]
    return x

numb = input("Insert list of numbers: ").split()
print("The prime numbers are", prime_list(numb))
