numeros = [1, 2, 3, 4, 5]
soma = 0

try:
    for numero in numeros:
        soma += numero
        print(soma)
except:
    print("Ocorreu um erro ao somar os números.")