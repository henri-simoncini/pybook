nums = input(int("Insira o número:")).split()
pares = 0
for num in nums:
  if num % 2 == 0:
    pares += 1
print("Números pares encontrados: " + str(pares))
