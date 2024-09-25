num1 = float(input("Enter the first number: ").strip())
num2 = float(input("Enter the second number: ").strip())

operation = input("Choose the operation (+, -, *, /): ").strip()

match operation:
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
            print("Division by zero is not allowed!")
    case _:
        print("Invalid operation! Please choose from (+, -, *, /).")
