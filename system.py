from packs.arquivo import manipulation

arquivo = 'cronograma/cronograma.txt'

if not manipulation.verificaSeExiste(arquivo):
	manipulation.criarDoc(arquivo)

escolha = str(input('Deseja atualizar o cronograma? [s/n]')).strip().lower()

if escolha == 's':
    pass
else:
    print('Tenha um bom dia!')
