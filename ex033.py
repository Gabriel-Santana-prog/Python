contador=0
soma=0
while True:
    num=int(input('Digite um número ou "0"para parar :'))
    if num !=0:
        contador+=1
        soma+=num
        media=soma/contador
    elif num ==0:
        break
print(f'A média dos números digitadoes foi {media:.0f}')