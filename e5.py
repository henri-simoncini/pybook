soma = 0
quantidade = 0
while True:
    nota = float(input("Digite uma nota (-1 para sair): "))
    if nota == -1:
        break
    soma += nota
    quantidade += 1
if quantidade > 0:
    media = soma / quantidade
    print(f"Média final: {media:.2f}")
else:
    print("Nenhuma nota foi digitada.")
