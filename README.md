# Intership_-task_month1
Project 1: Calculator (Functions + Conditions)
📄 Code :
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("1.Add  2.Subtract  3.Multiply  4.Divide")
choice = int(input("Enter choice: "))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if choice == 1:
    print(add(x, y))
elif choice == 2:
    print(subtract(x, y))
elif choice == 3:
    print(multiply(x, y))
elif choice == 4:
    print(divide(x, y))
else:
    print("Invalid choice")
