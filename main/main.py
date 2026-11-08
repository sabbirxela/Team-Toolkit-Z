# Team Toolkit CLI Application

def calculator():
    print("\n--- 1. Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            print(f"Result: {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1 * num2}")
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1 / num2}")
        else:
            print("Invalid operator!")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

def unit_converter():
    print("\n--- 2. Unit Converter ---")
    print("1. Kilometer to Miles")
    print("2. Celsius to Fahrenheit")
    choice = input("Select conversion type (1-2): ").strip()
    
    try:
        if choice == '1':
            km = float(input("Enter distance in KM: "))
            print(f"{km} KM = {km * 0.621371:.2f} Miles")
        elif choice == '2':
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}°C = {(celsius * 9/5) + 32:.2f}°F")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def main():
    while True:
        print("\n==============================")
        print("      WELCOME TO TEAM TOOLKIT   ")
        print("==============================")
        print("1. Simple Calculator")
        print("2. Unit Converter")
        print("3. Exit")
        
        user_choice = input("Enter your choice (1-3): ").strip()
        
        if user_choice == '1':
            calculator()
        elif user_choice == '2':
            unit_converter()
        elif user_choice == '3':
            print("Exiting Team Toolkit. Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
