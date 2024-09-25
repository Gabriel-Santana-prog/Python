
frase=input('Digite uma frase:').lower();
vogais='a','e','i','o','u';
vogaisDigitadas='';
contador=0;
for letra in frase:
    if letra in vogais:
        vogaisDigitadas+=letra
        contador+=1
print(f'As {contador} vogais da frase "{frase}" são: {vogaisDigitadas.upper()}')
         