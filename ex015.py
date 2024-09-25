try:
    n=int(input("Digite um número:"))
    par_impar = f'{n} é par'if n %2 ==0 else f"{n} ímpar"
    print(par_impar)
except ValueError:
    print('Por favaor , digite apenas números!')