
lista1=[]
lista2=[]
for i in range(0,4):
 lista1.append(int(input("Digite um número para a primeira lista:")))
print(f"Primeira lista {lista1}")
for i in range(0,4):
    lista2.append(int(input("Digite um número para outra lista:")))
print(f'Segunda lista{lista2}')
print(f'A concatenação das listas é {lista1+lista2}')