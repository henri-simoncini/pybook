senha = input("Digite a senha: ")
tem_numero = False
tem_letra = False
for caractere in senha:
    if caractere.isdigit():
        tem_numero = True
    if caractere.isalpha():
        tem_letra = True
if len(senha) >= 8 and tem_numero and tem_letra:
    print("Senha válida")
else:
    print("Senha inválida")
