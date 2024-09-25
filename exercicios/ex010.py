
def numero_vogais(word):
    contador_de_vogais=['A','E','I','O','U','a','e','i','o','u']
    total_de_vogais=0
    for i in word:
        if i in contador_de_vogais:
            total_de_vogais+=1
    print(f'O texto "{word}" tem ao todo {total_de_vogais} vogais')
            
word=input('Digite uma palavra:')
numero_vogais(word)
