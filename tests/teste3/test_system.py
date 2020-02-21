import sys
from packs.arquivo import manipulation

arquivo_monofasico_alimentacao = 'cronos/cronograma_de_alimentacao/cronograma_monofasico.txt'
arquivo_bifasico_alimentacao = 'cronos/cronograma_de_alimentacao/cronograma_bifasico.txt'
arquivo_everyman_alimentacao = 'cronos/cronograma_de_alimentacao/cronograma_everyman.txt'
arquivo_dymaxion_alimentacao = 'cronos/cronograma_de_alimentacao/cronograma_dymaxion.txt'
arquivo_uberman_alimentacao = 'cronos/cronograma_de_alimentacao/cronograma_uberman.txt'

arquivo_monofasico_ed_fisica = 'cronos/cronograma_de_ed_fisica/cronograma_monofasico.txt'
arquivo_bifasico_ed_fisica = 'cronos/cronograma_de_ed_fisica/cronograma_bifasico.txt'
arquivo_everyman_ed_fisica = 'cronos/cronograma_de_ed_fisica/cronograma_everyman.txt'
arquivo_dymaxion_ed_fisica = 'cronos/cronograma_de_ed_fisica/cronograma_dymaxion.txt'
arquivo_uberman_ed_fisica = 'cronos/cronograma_de_ed_fisica/cronograma_uberman.txt'

arquivo_monofasico_estudo = 'cronos/cronograma_de_estudo/cronograma_monofasico.txt'
arquivo_bifasico_estudo = 'cronos/cronograma_de_estudo/cronograma_bifasico.txt'
arquivo_everyman_estudo = 'cronos/cronograma_de_estudo/cronograma_everyman.txt'
arquivo_dymaxion_estudo = 'cronos/cronograma_de_estudo/cronograma_dymaxion.txt'
arquivo_uberman_estudo = 'cronos/cronograma_de_estudo/cronograma_uberman.txt'

arquivo_monofasico_trabalho = 'cronos/cronograma_de_trabalho/cronograma_monofasico.txt'
arquivo_bifasico_trabalho = 'cronos/cronograma_de_trabalho/cronograma_bifasico.txt'
arquivo_everyman_trabalho = 'cronos/cronograma_de_trabalho/cronograma_everyman.txt'
arquivo_dymaxion_trabalho = 'cronos/cronograma_de_trabalho/cronograma_dymaxion.txt'
arquivo_uberman_trabalho = 'cronos/cronograma_de_trabalho/cronograma_uberman.txt'


while True:
        comando = str(input('>> ')).lower().strip().split()
        if comando == 'x' and len(comando) == 1:
                sys.exit('Adeus')
        elif codigo[0] == 'cronos' and len(codigo[0])  == 6:
                if codigo[1] == 'new' and len(codigo[1]) == 3:
                        if codigo[2] == 'al' and len(codigo[2]) == 2:
                                if len(codigo[3]) == 2:
                                        if codigo[3] == 'mo':
                                                if not manipulation.verificaSeExiste(arquivo_monofasico_alimentacao):
                                                        manipulation.criarDoc(arquivo_monofasico_alimentacao)
                                                        manipulation.modeloMonofasico(arquivo_monofasico_alimentacao)
                                        elif codigo[3] == 'bi':
                                                if not manipulation.verificaSeExiste(arquivo_bifasico_alimentacao):
                                                        manipulation.criarDoc(arquivo_bifasico_alimentacao)
                                                        manipulation.modeloBifasico(arquivo_bifasico_alimentacao)
                                        elif codigo[3] == 'ev':
                                                if nor manipulation.verificaSeExiste(arquivo_everyman_alimentação):
                                                        manipulation.criarDoc(arquivo_everyman_alimentacao)
                                                        manipulation.modeloEveryman(arquivo_everyman_alimentacao)
                                        elif codigo[3] == 'dy':
                                                if not manipulation.verificaSeExiste(arquivo_dymaxion_alimentacao):
                                                        manipulation.criarDoc(arquivo_dymaxion_alimentacao)
                                                        manupulation.modeloDymaxion(arquivo_dymaxion_alimentacao)
                                        elif codigo[3] == 'ub':
                                                if not manipulation.verificaSeExiste(arquivo_uberman_alimentacao):
                                                        manipulation.criarDoc(arquivo_uberman_alimentacao)
                                                        manipulation.modeloUberman(arquivo_uberman_alimentacao)
                       elif codigo[2] == 'ed' and len(codigo[2]) == 2:
                               if len(codigo[3]) == 2:
                                        if codigo[3] == 'mo':
                                                if not manipulation.verificaSeExiste(arquivo_monofasico_ed_fisica):
                                                        manipulation.criarDoc(arquivo_monofasico_ed_fisica)
                                                        manipulation.modeloMonofasico(arquivo_monofasico_ed_fisica)
                                        elif codigo[3] == 'bi':
                                                if not manipulation.verificaSeExiste(arquivo_bifasico_ed_fisica):
                                                        manipulation.criarDoc(arquivo_bifasico_ed_fisica)
                                                        manipulation.modeloBifasico(arquivo_bifasico_ed_fisica)
                                        elif codigo[3] == 'ev':
                                                if nor manipulation.verificaSeExiste(arquivo_everyman_ed_fisica):
                                                        manipulation.criarDoc(arquivo_everyman_ed_fisica)
                                                        manipulation.modeloEveryman(arquivo_everyman_ed_fisica)
                                        elif codigo[3] == 'dy':
                                                if not manipulation.verificaSeExiste(arquivo_dymaxion_ed_fisica):
                                                        manipulation.criarDoc(arquivo_dymaxion_ed_fisica)
                                                        manupulation.modeloDymaxion(arquivo_dymaxion_ed_fisica)
                                        elif codigo[3] == 'ub':
                                                if not manipulation.verificaSeExiste(arquivo_uberman_ed_fisica):
                                                        manipulation.criarDoc(arquivo_uberman_ed_fisica)
                                                        manipulation.modeloUberman(arquivo_uberman_ed_fisica)
                        elif codigo[2] == 'es' and len(codigo[2]) == 2:
                               if len(codigo[3]) == 2:
                                        if codigo[3] == 'mo':
                                                if not manipulation.verificaSeExiste(arquivo_monofasico_estudo):
                                                        manipulation.criarDoc(arquivo_monofasico_estudo)
                                                        manipulation.modeloMonofasico(arquivo_monofasico_estudo)
                                        elif codigo[3] == 'bi':
                                                if not manipulation.verificaSeExiste(arquivo_bifasico_estudo):
                                                        manipulation.criarDoc(arquivo_bifasico_estudo)
                                                        manipulation.modeloBifasico(arquivo_bifasico_estudo)
                                        elif codigo[3] == 'ev':
                                                if nor manipulation.verificaSeExiste(arquivo_everyman_estudo):
                                                        manipulation.criarDoc(arquivo_everyman_estudo)
                                                        manipulation.modeloEveryman(arquivo_everyman_estudo)
                                        elif codigo[3] == 'dy':
                                                if not manipulation.verificaSeExiste(arquivo_dymaxion_estudo):
                                                        manipulation.criarDoc(arquivo_dymaxion_estudo)
                                                        manupulation.modeloDymaxion(arquivo_dymaxion_estudo)
                                        elif codigo[3] == 'ub':
                                                if not manipulation.verificaSeExiste(arquivo_uberman_estudo):
                                                        manipulation.criarDoc(arquivo_uberman_estudo)
                                                        manipulation.modeloUberman(arquivo_uberman_estudo)
                        elif codigo[2] == 'tr' and len(codigo[2]) == 2:
                               if len(codigo[3]) == 2:
                                        if codigo[3] == 'mo':
                                                if not manipulation.verificaSeExiste(arquivo_monofasico_trabalho):
                                                        manipulation.criarDoc(arquivo_monofasico_trabalho)
                                                        manipulation.modeloMonofasico(arquivo_monofasico_trabalho)
                                        elif codigo[3] == 'bi':
                                                if not manipulation.verificaSeExiste(arquivo_bifasico_trabalho):
                                                        manipulation.criarDoc(arquivo_bifasico_estudo)
                                                        manipulation.modeloBifasico(arquivo_bifasico_trabalho)
                                        elif codigo[3] == 'ev':
                                                if nor manipulation.verificaSeExiste(arquivo_everyman_trabalho):
                                                        manipulation.criarDoc(arquivo_everyman_estudo)
                                                        manipulation.modeloEveryman(arquivo_everyman_trabalho)
                                        elif codigo[3] == 'dy':
                                                if not manipulation.verificaSeExiste(arquivo_dymaxion_trabalho):
                                                        manipulation.criarDoc(arquivo_dymaxion_estudo)
                                                        manupulation.modeloDymaxion(arquivo_dymaxion_trabalho)
                                        elif codigo[3] == 'ub':
                                                if not manipulation.verificaSeExiste(arquivo_uberman_trabalho):
                                                        manipulation.criarDoc(arquivo_uberman_trabalho)
                                                        manipulation.modeloUberman(arquivo_uberman_trabalho)



