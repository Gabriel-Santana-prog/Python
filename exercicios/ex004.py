
n=int(input("Digite um número:"))
primo=True
if n <=1:
    primo=False
divisor=2
while divisor*divisor<= n and primo:
    if n% divisor==0:
        primo=False
    divisor+=1
if primo:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')
    




    