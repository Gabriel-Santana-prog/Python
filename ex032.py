soma =0
while True:
    num=int(input("Digite um número ou '<0'para parar:"))
    if num>=0:
        soma+=num
    elif num <0:
        print(f'A soma dos núemros positivos é {soma}')
        break
        