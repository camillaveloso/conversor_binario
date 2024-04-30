import numpy as np
for numero in [32, 57, 101, 77]:
        print(f'O número {numero} em código binário é: {np.binary_repr(numero)}')
print("Deseja testar números aleatórios? Se sim, digite qualquer número. Se não, digite 0 pra sair: ")
while True:
    continuar = int(input("Digite um número: "))
    if continuar == 0:
        break
    
    else:
        print(f'O número {continuar} em código binário é: {np.binary_repr(continuar)}')