num1 = float(input("Enter the first number:").strip())
num2 = float(input("Enter the second number:").strip())

operations = input("Choose the operation (+, -, *, /):")

match operations:
    case "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    case "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    case "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print(f"Division by zero is not allowed here!")
    case _:
        print("invalid!!!, choose within the given operations(+,-,*,/)")
        
