n1=float(input('Digite um número:'))
n2=float(input('Digite um número:'))
n3=float(input('Digite um número:'))
somaNumbersTrue=(n1+n2+n3)>0
somaNumbersNegative=(n1+n2+n3)<0

if somaNumbersTrue:
    print('A soma dos números é positiva')
elif somaNumbersNegative:
    print('A soma dos números é negativa')
else:
    print('A soma dos números é igual a zero')
