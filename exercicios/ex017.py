try:
    num=float(input("Digite um número:"))
    positivo=num>0
    neutro=num==0
    negativo=num<0
    if  positivo:
        print('Positivo')
    elif negativo:
        print('Negativo')
    elif neutro:
        print('neutro')  
except ValueError:
    print('Digite apenas números!')