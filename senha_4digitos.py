TAMANHO_SENHA = 4

senha = input('Digite sua senha de 4 dígitos: ')

if len(senha) == TAMANHO_SENHA:
    print('Senha válida!')
else:
    print('senha inválida, digite uma senha de 4 dígitos!')