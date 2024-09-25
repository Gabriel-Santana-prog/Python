num_1=input('Digite um número:')
num_2=input('Digite um número:')
verificador=num_1.isdigit() and num_2.isdigit()
if verificador:  
    num_convert_1=int(num_1)
    num_convert_2=int(num_2)
    print(f'A soma entre {num_2} + {num_2} é {num_convert_1+num_convert_2}')
    print(f'A Subtração entre {num_1} - {num_2} é {num_convert_1-num_convert_2} ')
    print(f'A multiplicação entre {num_1} x {num_2} é {num_convert_2*num_convert_1}')
    print(f'A divisão entre {num_1} / {num_2} é {num_convert_1/num_convert_2}')
else:
    print('Digite apenas números.')
