lista=[]
n=int(input('Digite um número:'))
soma=0
for quantidade in range(n):
    numeros=int(input(f'Digite o {quantidade+1}° número:'))
    lista.append(numeros)
for cont in lista:
    soma+=cont
print(f"A soma dos números foi {soma}")