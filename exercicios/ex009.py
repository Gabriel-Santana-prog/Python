
def par_ou_impar(n):
    if n % 2==0:
        return f"{n} é par"
    else:
        return f'{n} é impar'
        
n=int(input("Digite um número:"))
print(par_ou_impar(n))        
