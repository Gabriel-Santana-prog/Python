try:
    n1=float(input('Digite um número :'))
    n2=float(input('Digite um número:'))
    maior_1=n1>n2
    maior_2=n2>n1
    if maior_1:
        print(f'O número {n1} é maior que {n2}')
    elif maior_2:
        print(F'O número {n2} é maior que o número {n1}')
    else:
        print('Ambos os números são iguais!')
except ValueError:
    print("Por favor digite apenas números!")