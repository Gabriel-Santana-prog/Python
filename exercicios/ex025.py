num=int(input('Digite um número:'))
divisivel_3_5= num % 3==0 and num % 5==0
divisivel_3=num %3==0 
divisivel_5= num%5==0
if divisivel_3_5:
    print(f'{num} é divisivel por 3 e 5.')
elif divisivel_3:
    print(f'{num} é divisivel apenas por 3!')
elif divisivel_5:
    print(f'{num} é divisivel apenas por 5!')