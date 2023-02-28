#Calcule a soma dos números pares entre 102 e 150

contador = 102
soma = 0

while contador < 150:
    contador = contador + 1
    if (contador % 2) == 0:
        soma = soma + contador
print(f"A soma dos números pares entre 102 e 150 é {soma}")