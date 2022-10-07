def count_1_s(numb):
    binary = bin(int(numb)).replace("0b", "")
    count = binary.count("1")
    print("Binary number", binary)
    return count

number = input("Enter your number: ")
print("The binary form has", count_1_s(number), "one's")
