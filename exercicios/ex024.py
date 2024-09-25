dias_uteis=['segunda-feira','terça-feira','quarta-feira', 'quinta-feira', 'sexta-feira'];
fim_semana=['sábado', 'domingo'];
dia=input('Digite o nome de um dia da semana:').lower();
if dia in dias_uteis:
    print('É um dia útil');
elif dia in fim_semana:
    print('É um dia de fim de semana');