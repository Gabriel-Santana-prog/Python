'''
for numero in range(1,11):
    print('Tabuada do', numero)
    for i in range(1,11):
        resultado=i*numero
        print(f'{numero} x {i} = {resultado}')
'''
contador=1
while contador <=10:
    print(f'tabuada do {contador}:')
    multi=0
    while multi <=10:
        resultado=contador*multi
        print(f'{contador} x {multi} = {resultado}')
        multi+=1
    contador+=1
