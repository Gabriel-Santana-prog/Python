contadorMaioridade=0
contadorMenoridade=0
for c in range(5):
    idade=int(input("Digite uma idade:"));
    if(idade<=0):
        print("Digite apenas números inteiros maiores que zero");
        continue
    if(idade>=18):
        contadorMaioridade+=1;
    else:
        contadorMenoridade+=1;
print(f"Ao todo são {contadorMaioridade} pessoas maiores de idade. ")
print(f"Ao todo são {contadorMenoridade} pessoas menores de idade.")