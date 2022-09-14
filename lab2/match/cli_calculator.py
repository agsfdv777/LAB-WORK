num1 = float(input("Enter first number: "))

operator = input("Enter math operator ")

num2 = float(input("Enter second number: "))


match operator:
    case "/":
        num3 = num1 / num2
    case "*":
        num3 = num1 * num2
    case "+":
        num3 = num1 + num2
    case "-":
        num3 = num1 - num2
    case "^":
        num3 = pow(num1, num2)
    case _:
        num3 = "error"

print(num3)