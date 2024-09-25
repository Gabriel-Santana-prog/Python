n=int(input("Digite a quantidade de vezes:"))
lista=[]
for i in range(n):
    numero=int(input(f"Digite o {i+1}° número:"))
    lista.append(numero)
soma=0
for m in lista:
    soma+=m
    media=soma/n
print(f"A media dos números digitados foi {media:.0f}")
