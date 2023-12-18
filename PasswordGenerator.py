import random

print("................Welcome to password generator!😎....................\n")

CapAlphabets ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SmallAlphabets ="abcdefghijklmnopqrstuvwxyz"
Numbers = "0123456789"

pwd = CapAlphabets + SmallAlphabets + Numbers

length = int(input("Enter the length of password: "))

password = "".join(random.sample(pwd, length))

print(password)