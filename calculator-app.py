def calculator():
    print("Welcome to the Python Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input
    choice = input("Enter the number corresponding to the operation (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"The result is: {num1 + num2}")
            elif choice == '2':
                print(f"The result is: {num1 - num2}")
            elif choice == '3':
                print(f"The result is: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"The result is: {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Error: Please enter valid numbers.")
    else:
        print("Invalid choice. Please select a valid operation.")

# Run the calculator
calculator()