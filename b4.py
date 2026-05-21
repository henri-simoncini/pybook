num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))
op = str(input("Digite o operador (+ , - , * , /):\n"))

if op == "+":
    print("O resultado é:\n")
    print(num1 + num2)
elif op == "-":
    print("O resultado é:\n")
    print(num1 - num2)
elif op == "*":
    print("O resultado é:\n")
    print(num1 * num2)
elif op == "/":
    if num2 and num1 != 0:
        print("O resultado é:\n")
        print(num1 / num2)
    else:
        print("Divisão inválida!")
else:
    print("Operador inválido!")
    
