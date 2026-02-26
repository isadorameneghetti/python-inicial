nome_escolhido = 'Isadora'
senha_escolhida = '12345'

nome_fornecido = input('Digite o nome: ')
senha_fornecida = input('Digite a senha: ')

if nome_fornecido == nome_escolhido and senha_fornecida == senha_escolhida:
    print('Acesso liberado')
else:
    print('Acesso negado')
