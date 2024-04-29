import random as random

for inteiro in [32, 57, 101, 77]:
    binario = bin(inteiro)[2:]
    print(f'O número {inteiro} em código binário é: {binario}')

while True:
    continuar = int(input("Deseja testar números aleatórios? Se sim, digite qualquer número. Se não, digite 0 pra sair: "))
    if continuar == 0:
        break
    
    else:
        aleatorio = random.randint(0, 1000)
        binario = bin(aleatorio)[2:]
        print(f'O número {aleatorio} em código binário é: {binario}')