try:
    p1=float(input('Digite a nota da primeira prova :'))
    p2=float(input('Digite a nota da segunda prova:'))
    media_aritimeica=(p1+p2)/2
    aprovado=media_aritimeica>=6
    reprovado=media_aritimeica<6
    if aprovado:
        print(f'Aprovado com nota igual a {media_aritimeica:.1f}')
    elif reprovado:
        print(f'Reprovado com nota igual a {media_aritimeica:.1f}')
except ValueError:
    print('Digite apenas número')   
