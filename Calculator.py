import math
def add(x,y):
    return x+y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Select an operation -\n"
      "1- Add\n"
      "2- Subtract\n"
      "3- Multiply\n"
      "4- Divide\n")

while True:
    choice = input("\nEnter your choice (1/2/3/4): ")
    if choice in ("1", "2", "3", "4"):
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))

        if choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))
        elif choice == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))
        elif choice == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))
        elif choice == '4':
            print(n1, "/", n2, "=", divide(n1, n2))
        break
    else:
        print("Thank you for using this calculator")