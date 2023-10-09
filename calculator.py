num1 = int(input("Введите первое число: "))
operation = input("Выберите действие (+,-,*,/): ")
num2 = int(input("Введите второе число: "))

if operation == "+":
    print("Ответ: ", num1 + num2)
elif operation == "-":
    print("Ответ: ",num1 - num2)
elif operation == "*":
    print("Ответ: ",num1 * num2)
elif operation == "/" and num2 != 0:
    print("Ответ: ",num1 / num2)
elif operation == "/" and num2 == 0:
    print("На ноль делить нельзя")