def palindrome(text):
   if text == text[::-1]:
        return True
   else: return False

text = input("Enter your string : ")
print(palindrome(text))