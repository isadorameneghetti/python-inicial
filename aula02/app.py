import os

def exibir_titulo():
    print('Sabor Express')

def exibir_menu():
    print("""
    1. Cadastrar restaurante
    2. Listar restaurante
    3. Ativar restaurante
    4. Sair
    """)

def escolher_opcao():
    opcao_escolhida = input('Escolha uma opção: ')

    if opcao_escolhida == '1':
        print('Cadastrar restaurante')
    elif opcao_escolhida == '2':
        print('Listar restaurante')
    elif opcao_escolhida == '3':
        print('Ativar restaurante')
    elif opcao_escolhida == '4':
        finalizar_app()
    else:
        print('Opção inválida')

def finalizar_app():
    os.system('cls')
    print('Finalizando app\n')

def main():
    exibir_titulo()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()