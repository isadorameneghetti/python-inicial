escolha_usuario = int(input('Digite um número: '))

if escolha_usuario % 2 == 0:
    print('O número é par')
elif escolha_usuario % 2 != 0:
    print('O número é ímpar')
else:
    print('Digite um número válido')