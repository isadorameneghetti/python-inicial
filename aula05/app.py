import os

restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False},   
                {'nome': 'Sushi', 'categoria': 'Japonesa', 'ativo': True},
                {'nome': 'Hamburguer', 'categoria': 'Americana', 'ativo': False}]

def exibir_titulo():
    '''
    Essa função é responsável por exibir o título do aplicativo. Ela simplesmente imprime o nome do aplicativo na tela.

    Outputs:
    - Imprime o título do aplicativo na tela.

    Inputs:
    - Nenhum.
    '''
    print('Sabor Express')

def exibir_opcoes():
    '''
    Essa função é responsável por exibir as opções do menu para o usuário. Ela utiliza uma string de múltiplas linhas para formatar a exibição das opções disponíveis.

    Outputs:
    - Imprime as opções do menu na tela.

    Inputs:
    - Nenhum.
    '''
    print("""
    1. Cadastrar restaurante
    2. Listar restaurante
    3. Ativar ou Desativar restaurante
    4. Sair
    """)

def voltar_menu():
    '''
    Essa função é responsável por pausar a execução do programa e aguardar o usuário pressionar uma tecla para continuar. Ela utiliza a função input() para ler a entrada do usuário e, em seguida, chama a função main() para retornar ao menu principal.

    Outputs:
    - Pausa a execução do programa e aguarda o usuário pressionar uma tecla para continuar

    Inputs:
    - Nenhum.
    '''
    input('\nPressione qualquer tecla para continuar...')
    main()

def iniciar_opcao(texto):
    '''
    Essa função é responsável por limpar a tela e exibir o título da opção escolhida. Ela recebe um texto como parâmetro, que é o título da opção, e utiliza a função os.system('cls') para limpar a tela no Windows. Em seguida, exibe o título e uma linha de separação.
    
    Outputs:
    - Limpa a tela e exibe o título da opção escolhida.

    Inputs:
    - texto: O título da opção escolhida a ser exibido.
    '''
    os.system('cls')
    linha = '-' * (len(texto) + 4)
    print(texto)
    print(linha)
    print()    

def cadastrar_restaurante():
    '''
    Essa função é responsável por cadastrar um novo restaurante. Ela solicita ao usuário o nome e a categoria do restaurante, cria um dicionário com essas informações e adiciona à lista de restaurantes.
    
    Outputs:
    - Solicita ao usuário o nome e a categoria do restaurante.
    - Adiciona o restaurante à lista de restaurantes.
    - Exibe uma mensagem de sucesso após o cadastro.

    Inputs:
    - nome_restaurante: O nome do restaurante a ser cadastrado.
    - categoria_restaurante: A categoria do restaurante a ser cadastrado.
    '''
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
    '''
    Essa função é responsável por listar todos os restaurantes cadastrados. Ela verifica se a lista de restaurantes está vazia e, caso contrário, exibe o nome, a categoria e o status de cada restaurante.
    
    Outputs:
    - Verifica se a lista de restaurantes está vazia e exibe uma mensagem caso esteja
    - Exibe o nome, a categoria e o status de cada restaurante cadastrado.

    Inputs:
    - Nenhum.
    '''
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
    '''
    Essa função é responsável por ativar ou desativar um restaurante. Ela solicita ao usuário o nome do restaurante que deseja alterar o status, verifica se o restaurante existe na lista e, caso exista, alterna o valor do campo 'ativo' e exibe uma mensagem de sucesso.
    
    Outputs:
    - Solicita ao usuário o nome do restaurante que deseja alterar o status.
    - Verifica se o restaurante existe na lista e, caso exista, alterna o valor do campo 'ativo'.
    - Exibe uma mensagem de sucesso após a alteração do status.

    Inputs:
    - restaurante_procurado: O nome do restaurante que o usuário deseja ativar ou desativar.
    '''
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
    '''
    Essa função é responsável por exibir uma mensagem de erro quando o usuário escolhe uma opção inválida no menu. Ela simplesmente imprime uma mensagem informando que a opção escolhida não é válida e, em seguida, chama a função voltar_menu() para retornar ao menu principal.
    
    Outputs:
    - Exibe uma mensagem de erro informando que a opção escolhida é inválida.
    - Retorna ao menu principal.

    Inputs:
    - Nenhum.
    '''
    iniciar_opcao('Opção inválida')
    
    voltar_menu()

def finalizar_app():
    '''
    Essa função é responsável por finalizar o aplicativo. Ela exibe uma mensagem de finalização e, em seguida, chama a função voltar_menu() para retornar ao menu principal.
    
    Outputs:
    - Exibe uma mensagem de finalização.
    - Retorna ao menu principal.
    
    Inputs:
    - Nenhum.
    '''
    iniciar_opcao('Finalizando app\n')
    voltar_menu()

def escolher_opcao():
    '''
    Essa função é responsável por ler a opção escolhida pelo usuário e chamar a função correspondente. Ela exibe uma mensagem solicitando ao usuário que escolha uma opção e, em seguida, lê a entrada do usuário.
    
    Outputs:
    - Solicita ao usuário que escolha uma opção.
    - Lê a entrada do usuário e chama a função correspondente à opção escolhida.

    Inputs:
    - opcao_escolhida: A opção escolhida pelo usuário, lida a partir da entrada do usuário.
    '''

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
    '''
    Essa função é a função principal do aplicativo. Ela é responsável por limpar a tela, exibir o título do aplicativo, exibir as opções do menu e chamar a função escolher_opcao() para ler a opção escolhida pelo usuário.
    
    Outputs:
    - Limpa a tela.
    - Exibe o título do aplicativo.
    - Exibe as opções do menu.
    - Chama a função escolher_opcao() para ler a opção escolhida pelo usuário.
    
    Inputs:
    - Nenhum.
    '''
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()