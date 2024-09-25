n=int(input('Digite um número:'))
print("-------------");
print("Por for:");
print("-------------");
for c in range(0,11):
    print(f' {n} x {c} = {c*n}')
print("-------------");
print("Por while");
print("-------------");
cont=0
while cont <=10:
    print(f'{n} x {cont} = {cont*n}')
    cont+=1