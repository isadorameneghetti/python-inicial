import os

restaurantes = ['Pizza', 'Sushi']

def exibir_titulo():
    print('Sabor Express')

def exibir_opcoes():
    print("""
    1. Cadastrar restaurante
    2. Listar restaurante
    3. Ativar restaurante
    4. Sair
    """)

def voltar_menu():
    input('\nPressione qualquer tecla para continuar...')
    main()

def iniciar_opcao(texto):
    os.system('cls')

    print(texto)

def cadastrar_restaurante():
    iniciar_opcao('Cadastrar restaurante')

    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')
    
    voltar_menu()

def listar_restaurante():
    iniciar_opcao('Listar restaurante')

    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado')
    else:
        for restaurante in restaurantes:
            print(restaurante)

    voltar_menu()

def ativar_restaurante():
    print('Ativar restaurante')

def opcao_invalida():
    print('Opção inválida')
    
    voltar_menu()

def finalizar_app():
    iniciar_opcao('Finalizando app\n')
    voltar_menu()

def escolher_opcao():
    opcao_escolhida = input('Escolha uma opção: ')

    if opcao_escolhida == '1':
        cadastrar_restaurante()
    elif opcao_escolhida == '2':
        listar_restaurante()
    elif opcao_escolhida == '3':
        ativar_restaurante()
    elif opcao_escolhida == '4':
        finalizar_app()
    else:
        opcao_invalida()

# Acho desnecessário já que é so converter tudo pra String logo no começo.
# def escolher_opcao():
#     try:
#         opcao_escolhida = input('Escolha uma opção: ')

#         if opcao_escolhida == '1':
#             cadastrar_restaurante()
#         elif opcao_escolhida == '2':
#             listar_restaurante()
#         elif opcao_escolhida == '3':
#             ativar_restaurante()
#         elif opcao_escolhida == '4':
#             finalizar_app()
#         else:
#             opcao_invalida()
#     except:
#         opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()