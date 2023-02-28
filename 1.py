#Ler 2 números e imprimir se são pares ou ímpares.

A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))

if (A % 2) == 0:
    print("O primeiro número é par.")
else:
    print("O primeiro número é impar.")
if (B % 2) == 0:
    print("O segundo número é par.")
else:
    print("O segundo número é impar.")