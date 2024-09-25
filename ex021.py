numeros_crescente=[]
n1=int(input('Digite um número:'))
n2=int(input('Digite um número:'))
n3=int(input('Digite um número:'))
numeros_crescente.append(n1)
numeros_crescente.append(n2)
numeros_crescente.append(n3)
numeros_crescente.sort()
print('Os números em ordem crescente são:')
for num in numeros_crescente:
    print(f'{num:.0f}' ,  end=' ')
