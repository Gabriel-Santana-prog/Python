import math

def calcular_media_geometrica(numeros):
    produto = 1
    for numero in numeros:
        produto *= numero
    return math.pow(produto, 1 / len(numeros))

numeros = []
while True:
    numero = float(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

if numeros:
    media_geometrica = calcular_media_geometrica(numeros)
    print(f"A média geométrica dos números é {media_geometrica:.2f}")
else:
    print("Nenhum número foi informado.")