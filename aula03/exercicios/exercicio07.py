numeros = [2, 4, 6, 8, 10]
media = 0

try:
    for numero in numeros:
        media += numero
        media/= len(numeros)
        print(media)
except:
    print("Ocorreu um erro ao calcular a média dos números.")