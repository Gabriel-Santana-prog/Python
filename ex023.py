idade=int(input('Digite sua idade:'))
nao_vota=idade<16
optativa= (idade>=16 and idade<=17) or idade>=70
obrigatorio= idade>=18 and idade<=69
if obrigatorio:
    print('Você é obrigado a votar')
elif nao_vota:
    print('Você não pode votar')
elif optativa:
    print('Seu voto é facultativo')