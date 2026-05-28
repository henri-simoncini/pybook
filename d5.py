lista = input("Digite os números separados por espaço: ").split()
valor = input("Digite o valor que deseja buscar: ")
if valor in lista:
    print("Valor encontrado")
else:
    print("Valor não encontrado")
