n=int(input('Digite a quantidade de números:'))
lista=[]
for quantidade in range(n):
    numeros=int(input(f"Digite o {quantidade+1}° número:"))
    lista.append(numeros)
maior=lista[0]
for num in lista:
    if num>maior:
        maior=num
print(f"O maior número digitado foi {maior}")
    