frase = 'Último exercício do curso!'
contagem_palavras = {}
palavras = frase.split()

for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

print(contagem_palavras)