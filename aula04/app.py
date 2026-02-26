import os

restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False},   
                {'nome': 'Sushi', 'categoria': 'Japonesa', 'ativo': True},
                {'nome': 'Hamburguer', 'categoria': 'Americana', 'ativo': False}]

def exibir_titulo():
    print('Sabor Express')

def exibir_opcoes():
    print("""
    1. Cadastrar restaurante
    2. Listar restaurante
    3. Ativar ou Desativar restaurante
    4. Sair
    """)

def voltar_menu():
    input('\nPressione qualquer tecla para continuar...')
    main()

def iniciar_opcao(texto):
    os.system('cls')
    linha = '-' * (len(texto) + 4)
    print(texto)
    print(linha)
    print()    

def cadastrar_restaurante():
    iniciar_opcao('Cadastrar restaurante')

    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante,
                         'categoria': categoria_restaurante,
                         'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')
    
    voltar_menu()

def listar_restaurante():
    iniciar_opcao('Listar restaurante')

    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado')
    else:
        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            ativo = restaurante['ativo']

            print(f'- Nome: {nome_restaurante.ljust(20)} | Categoria: {categoria_restaurante.ljust(20)} | Status: Ativo' if ativo else f'- Nome: {nome_restaurante.ljust(20)} | Categoria: {categoria_restaurante.ljust(20)} | Status: Inativo')

    voltar_menu()

def alternar_status_restaurante():
    iniciar_opcao('Alternar status restaurante')

    restaurante_procurado = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante_procurado == restaurante['nome']:
            restaurante['ativo'] = not restaurante['ativo']
            restaurante_encontrado = True
            print(f'Restaurante {restaurante_procurado} ativado com sucesso!' if restaurante['ativo'] else f'Restaurante {restaurante_procurado} desativado com sucesso!')

    voltar_menu()

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
        alternar_status_restaurante()
    elif opcao_escolhida == '4':
        finalizar_app()
    else:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()