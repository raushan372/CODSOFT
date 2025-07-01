def calculator():
    print("Welcome to Simple Calculator!")
    
    # Input numbers from user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")
        return

    # Show operation menu
    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter your choice (1/2/3/4): ")

    # Perform operation
    if choice == '1':
        result = num1 + num2
        print(f"\n✅ Result: {num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"\n✅ Result: {num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"\n✅ Result: {num1} * {num2} = {result}")
    elif choice == '4':
        if num2 == 0:
            print("\n❌ Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"\n✅ Result: {num1} / {num2} = {result}")
    else:
        print("\n❌ Invalid operation choice.")

# Run the calculator
calculator()
