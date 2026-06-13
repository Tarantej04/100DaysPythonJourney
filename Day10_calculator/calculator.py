import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
def calc():
    print(art.logo)
    rep = True
    while True:
        try:
            first_number = float(input("What is your first number?: "))
            break
        except ValueError:
            print("Please Enter a Valid Number..")
    while rep:
        while True:
            operation = input("Choose the operation you want to perform (+, -, *, /): ")
            if operation in math_dict:
                break
            print("Invalid Operation. Try Again from +, -, *, /...")
        while True:
            try:
                second_number = float(input("What is your second number?: "))
                break
            except ValueError:
                print("Please Enter a Valid Number..")
        if operation == "/" and second_number == 0:
            print("Error: Cannot divide by Zero")
            continue
        result = math_dict[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        repeat = input(f"Type 'y' if you want to continue with {result} or type 'n' if you want to start a new calculation.. Or type 'e' to exit the program..  ").lower()
        if repeat == 'y':
            first_number = result
        elif repeat == 'n':
            print("\n" * 20)
            calc()
        elif repeat == 'e':
            quit()
        else:
            print("Wrong choice. Choose either 'y' or 'n' only.. Program beginning again..")
            calc()

calc()
