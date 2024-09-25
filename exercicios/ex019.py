n1=int(input('Digite um número:'))
n2=int(input('Digite um número:'))
n3=int(input('Digite um número:'))
divisivel_5=(n1+n2+n3) % 5==0
if divisivel_5:
    print('A soma dos números é divisivel por 5')
else:
    print('A soma dos números não é divisivel por 5')
    