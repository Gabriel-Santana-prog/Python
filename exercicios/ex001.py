
def media_notas(n1,n2,n3,n4):
    media=(n1+n2+n3+n4)/4
    if media >=7:
        print('Aprovado')
    elif media<7 and media>=4 :
        print('Recuperação')
    elif media <4:
        print('Reprovado')
try:
    n1=float(input('Digite a primeira nota:'))
    n2=float(input('Digite a segunda nota:'))
    n3=float(input('Digite a terceira nota:'))
    n4=float(input('Digite a quarta nota:'))
       
except ValueError:
    print('Erro:')
    print('Digite apenas núemros inteiros de 1 a 10.')

media_notas(n1,n2,n3,n4) 


 



            
 

        
        