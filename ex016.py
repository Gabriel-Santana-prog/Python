
try:
    num=float(input('Digite um número:'))
    par= num % 2 ==0
    impar= num % 2 !=0
    if par:
        print(f'O número {num} é par')
    elif impar:
        print(f'O número {num} é impar')
except ValueError:
    print('Por favor digite apenas números!')