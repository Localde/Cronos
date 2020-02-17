def verificaSeExiste(arq):
     try:
          a = open(arq, 'r')
     except FileNotFoundError:
          print('Arquivo não encontrado.')
     else:
          print('Arquivo encontrado.')
          a.close()
     
def criarDoc(arq):
     try:
          a = open(arq, 'w')
     except Exception:
          print('Houve um erro inesperado.')
     else:
          print('Arquivo Criado com sucesso.')
          a.close()
