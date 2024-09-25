def encontrar_maior_numero(lista_numeros):
    maior=max(lista_numeros)
    return maior


lista_numeros=[]
for i in range(0,4):
    lista_numeros.append(int(input('Digite um número:')))
print(lista_numeros)
print("------O maior numéro da lista é-----------")
print(encontrar_maior_numero(lista_numeros))
