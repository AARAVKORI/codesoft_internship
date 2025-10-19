# Simple Calculator Program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice == '1':
    print(f"\nResult: {num1} + {num2} = {num1 + num2}")

elif choice == '2':
    print(f"\nResult: {num1} - {num2} = {num1 - num2}")

elif choice == '3':
    print(f"\nResult: {num1} * {num2} = {num1 * num2}")

elif choice == '4':
    if num2 != 0:
        print(f"\nResult: {num1} / {num2} = {num1 / num2}")
    else:
        print("\nError: Division by zero is not allowed.")

else:
    print("\nInvalid choice! Please select a valid operation.")
