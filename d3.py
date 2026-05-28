numeros = input("Digite os números separados por espaço: ").split()
maior = int(numeros[0])
for num in numeros:
    if int(num) > maior:
        maior = int(num)
print(maior)
