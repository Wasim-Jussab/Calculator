import os

def calculate(num1, num2, operator):
    """
    This function takes in two numbers and an operator and returns the result of the calculation.
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            return num1 / num2
    else:
        raise ValueError("Invalid operator")

def read_equations(file_name):
    """
    This function reads equations from a text file and prints them along with their results.
    """
    try:
        with open(file_name, "r") as file:
            equations = file.readlines()
        
        for equation in equations:
            try:
                num1, operator, num2 = equation.split()
                num1 = float(num1)
                num2 = float(num2)

                result = calculate(num1, num2, operator)
                print(f"{equation.strip()} = {result}")
            except ValueError:
                print(f"Invalid equation: {equation.strip()}")
            except ZeroDivisionError as e:
                print(f"{equation.strip()} = Error: {e}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """
    This function gets user input and either performs the calculation or reads equations from a text file.
    """
    while True:
        option = input("Enter '1' to calculate or '2' to read equations from a file: ")
        
        if option == "1":
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                operator = input("Enter the operator (+, -, *, /): ")

                result = calculate(num1, num2, operator)
                print("Result: ", result)

                with open("equations.txt", "a") as file:
                    file.write(f"{num1} {operator} {num2} = {result}\n")
            except ValueError as e:
                print("Error:", e)
            except ZeroDivisionError as e:
                print("Error:", e)
        elif option == "2":
            file_name = input("Enter the name of the file: ")
            read_equations(file_name)
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
