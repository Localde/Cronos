import sys
from packs.arquivo import manipulation
from packs.cronosestudo import estudo, ed_fisica, organizacao

arquivo_estudo = 'cronos/cronograma_de_estudo/cronograma_estudo.txt'
arquivo_ed_fisica = 'cronos/cronograma_de_ed_fisica/cronograma_ed_fisica.txt'
arquivo_organizacao = 'cronos/cronograma_de_organizacao/cronograma_organizacao.txt'

while True:
        codigo = str(input('>> ')).lower().strip().split()
        if codigo == 'x' and len(codigo) == 1:
                sys.exit('Adeus')
        elif codigo[0] == 'cronos' and len(codigo[0])  == 6:
                if codigo[1] == 'new' and len(codigo[1]) == 3:
                        if codigo[2] == 'es' and len(codigo[2]) == 2: #Cronograma de Estudo
                                if not manipulation.verificaSeExiste(arquivo_estudo):
                                        manipulation.criarDoc(arquivo_estudo)
                                        estudo.estudo(arquivo_estudo)
                        elif codigo[2] == 'ed' and len(codigo[2]) == 2: #Cronograma de Educação Fisica
                                if not manipulation.verificaSeExiste(arquivo_ed_fisica):
                                        manipulation.criarDoc(arquivo_ed_fisica)
                                        ed_fisica.edFisica(arquivo_ed_fisica)
                        elif codigo[2] == 'li' and len(codigo[2]) == 2: #Cronograma de Organização e Limpeza
                                if not manipulation.verificaSeExiste(arquivo_organizacao):
                                        manipulation.criarDoc(arquivo_organizacao)
                                        organizacao.limpeza(arquivo_organizacao)
