perimetro=''
area=''
while True:
    try:
        altura=float(input('Digite a altura do triângulo:'))
        lado_a=float(input('Digite o lado a do triângulo: '))
        lado_b=float(input('Digite o lado b do triângulo:'))
        lado_c=float(input('Digite o lado c do triângulo:'))
    except ValueError:
        print('Digite apenas números!')
        continue
    perimetro=lado_a+lado_b+lado_c
    area=(lado_b*altura)/2
    print(f'A área é {area} e o perímetro {perimetro} ')