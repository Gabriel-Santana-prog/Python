print('Calculando a velocidade média')
vm=''
try:
    vs=float(input('Digite a variação do espaço:'))
    vt=float(input('Digite a variação do tempo:'))
    vm=vs/vt
    print(f'A velocidade média é {vm:.2f}')
except ValueError:
    print('Por favor, digite apenas números!')
