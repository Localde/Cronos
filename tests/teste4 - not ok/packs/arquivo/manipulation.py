from random import choice

def verificaSeExiste(arq):
     try:
          a = open(arq, 'rt')
          a.close()
     except FileNotFoundError:
          return False
     else:
          return True
          
     
def criarDoc(arq):
     try:
          a = open(arq, 'wt+')
          a.close()
     except Exception:
          print('Houve um erro inesperado.')
     else:
          print('Arquivo criado com sucesso.')


