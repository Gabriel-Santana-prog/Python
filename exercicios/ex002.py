
def conversor_Kcal_para_calorias():
    kcal=float(input('Digite as calorias em kcal:'))
    c=kcal*1000
    print(F'{kcal:.0f} kcal é o mesmo que {c:.0f} calorias')

def conversor_calorias_para_kcal():
    calorias=float(input('Digite as calorias:'))
    kcal=calorias/1000
    print(f'{calorias:.0f} calorias é o mesmo que {kcal:.0f} kcal')

print('-'*20)
print('1-Conversor de kcal para calorias')
print('2-Conversor de calorias para Kcal')
print('-'*20)
try:
    resp=int(input('Digite uma opção:'))
    if  resp!=1 and resp!=2:
        raise ValueError('Opção inválida, tente novamente depois')
    else:
     if resp==1:
            conversor_Kcal_para_calorias()
     elif resp==2:
        conversor_calorias_para_kcal()
except ValueError as e:
 print(e)

    
    
    




