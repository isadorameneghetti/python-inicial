escolha_usuario = input("Escolha um número: ")

for i in range(1, 11):
    resultado = int(escolha_usuario) * i
    print(f"{escolha_usuario} x {i} = {resultado}")