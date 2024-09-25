numero = int(input('Digite um número:'))
expoente = int(input("Digite um expoente:"))

resultado = 1
if expoente == 0:
    resultado = 1
else:
    for n in range(expoente, 0, -1):
        resultado *= numero

print(resultado)