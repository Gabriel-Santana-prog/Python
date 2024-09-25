
def quociente_e_resto(a,b):
    q=a//b
    r=a%b
    return f'O quociente da divisão é {q} enquanto o resto vale {r}'
    
a=int(input('Digite o dividendo:'))
b=int(input('Digite o divisor:'))
print(quociente_e_resto(a,b))