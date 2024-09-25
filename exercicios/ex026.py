idade=int(input('Digite sua idade:'))
criança=idade<=12
adolescente= idade >=13 and idade <=17
adulto= idade>=18 and idade <=59
idoso=idade>60
if criança:
    print('A idade é de uma criança')
elif adolescente:
    print('A idade é de um adolescente')
elif adulto:
    print('A idade é de um adulto')
else :
    print('A idade é de um idoso')