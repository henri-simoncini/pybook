num1 = float(input("Insira o primeiro número:\n"))
num2 = float(input("Insira o segundo número:\n"))
num3 = float(input("Insira o terceiro número:\n"))

if num1 >= num2 and num1 >= num3:
    print("O maior número é o primeiro: " + str(num1))
elif num2 >= num1 and num2 >= num3:
    print("O maior número é o segundo: " + str(num2))
else:
    print("O maior número é o terceiro: " + str(num3))
