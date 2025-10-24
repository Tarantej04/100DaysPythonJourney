import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("\n✨😁Welcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

store = []
if nr_letters >= 0:
    for letter in range(1, nr_letters + 1):
        store += random.choices(letters)
else:
    print("Enter positive values only..")
    quit()

if nr_symbols >= 0:
    for symbol in range(1, nr_symbols + 1):
        store += random.choices(symbols)
else:
    print("Enter positive values only.. ")
    quit()

if nr_numbers >= 0:
    for number in range(1, nr_numbers + 1):
        store += random.choices(numbers)
else:
    print("Enter positive values only..")
    quit()

print(store)
random.shuffle(store)
print(store)
password = ""
for i in store:
    password += i
print(f"Your password is: {password}")
