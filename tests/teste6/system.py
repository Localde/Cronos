import sys
from packs.arquivo import manipulation

arquivo_a = 'cronos/cronograma_a.txt'
arquivo_b = 'cronos/cronograma_b.txt'
arquivo_c = 'cronos/cronograma_c.txt'
arquivo_d = 'cronos/cronograma_d.txt'
arquivo_e = 'cronos/cronograma_e.txt'

while True:
        comando = str(input('>> ')).lower().strip()
        if comando in 'x':
                sys.exit('Adeus')
        elif comando == 'newc a':
                if not manipulation.verificaSeExiste(arquivo_a):
                	manipulation.criarDoc(arquivo_a)
                	manipulation.modeloA(arquivo_a)
        elif comando == 'newc b':
                if not manipulation.verificaSeExiste(arquivo_b):
                	manipulation.criarDoc(arquivo_b)                                
        elif comando == 'newc c':
                if not manipulation.verificaSeExiste(arquivo_c):
                	manipulation.criarDoc(arquivo_c)                                
        elif comando == 'newc d':
                if not manipulation.verificaSeExiste(arquivo_d):
                	manipulation.criarDoc(arquivo_d)                                
        elif comando == 'newc e':
                if not manipulation.verificaSeExiste(arquivo_e):
                	manipulation.criarDoc(arquivo_e)                                
