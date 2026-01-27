import random
import string

print("-" * 30 + " Welcome to password generator " + "-" * 30)

message = """
1- Add random numbers
2- Add random letters
3- Add random symbols
4- Change the whole password
"""

password = ""

while True:
    print(message)
    pick = input("Pick a number between 1 and 4: ")

    if not pick.isdigit():
        print("Type a number")
        continue

    pick = int(pick)

    if pick < 1 or pick > 4:
        print("Please choose a valid number")
        continue

    if pick == 1:
        if password == "":
            password = input("Type your password: ")
        for i in range(4):
            password += str(random.randint(0, 9))
        print(password)

    elif pick == 2:
        if password == "":
            password = input("Type your password: ")
        for i in range(4):
            password += random.choice(string.ascii_letters)
        print(password)

    elif pick == 3:
        if password == "":
            password = input("Type your password: ")
        for i in range(4):
            password += random.choice(string.punctuation)
        print(password)

    elif pick == 4:
        length = int(input("Enter password length: "))
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        print(password)
