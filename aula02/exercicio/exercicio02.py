idade = int(input('Digite sua idade: '))

if idade <= 12:
    print('Criança')
elif 13 <=idade <= 18:
    print('Adolescente')
elif idade > 18:
    print('Adulto')
else:
    print('Digite um número válido')