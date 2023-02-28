import random

x = int(input("Digite a quantide de números aleatórios que serão somados: "))
soma = 0

for i in range (0 , x):
    soma = soma + random.randint(1,10)

print(f"A soma total é: {soma}")


