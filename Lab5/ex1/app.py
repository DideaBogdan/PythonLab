import utils

print("If you want to exit press q and enter")
while True:
    numb = input("Please enter a number:")
    if numb == 'q':
        print("Sorry to see you go!")
        break
    print("Your next prime number is:", utils.process_item(numb))
