def search_string(s1, s2):
    index = 0
    count = 0
    while index < len(s2)-len(s1):
        index = s2.find(s1, index+1)
        if index >= 0:
            count += 1
    if s2.find(s1, len(s2)-len(s1)) > 0:
        count +=1
    return count


text1 = input("Enter your first string : ")

text2 = input("Enter your second string : ")


print(search_string(text1, text2))
