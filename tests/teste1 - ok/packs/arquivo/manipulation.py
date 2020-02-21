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


def modeloA(arq):
     try:
          a = open(arq, 'at')
     except Exception:
          print('Houve um ERRO na hora de escrever os dados!')
     else:
          try:
               metodos_de_estudo = ['Assistir Video Aulas', 'Leitura Intensiva', 'Resolver Atividades', 'Fazer Engenharia Reversa']
               limpar = ['Cozinha', 'Sala', 'Quarto onde Dorme', 'Quarto onde não dorme', 'Banheiro do corredor', 'Banheiro do quarto onde dorme', 'Area do tanquinho']                              
               materias = ['Python', 'PHP', 'Javascript']
               aleatorio_a = choice(metodos_de_estudo)
               aleatorio_b = choice(limpar)
               aleatorio_c = choice(materias)
               aleatorio_d = choice(metodos_de_estudo)
               aleatorio_e = choice(limpar)

               a.write(f'Linguagem do Dia: {aleatorio_c}')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               a.write('Dormir: 01:30')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               a.write('Acordar: 07:30')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               a.write('Tomar Banho')
               a.write('\n')
               a.write('Ir ao mercado')
               a.write('\n')
               a.write('Café da manhã')
               a.write('\n')
               a.write('Fazer Duolingo')
               a.write('\n')
               a.write('Ler 10 paginas')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               a.write(f'Estudar: {aleatorio_a}')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               a.write('Almoçar: 12:30')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               a.write(f'Limpar e Organizar: {aleatorio_b}')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               a.write('Dormir: 13:30')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               a.write('Acordar: 14:00')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               while aleatorio_d == aleatorio_a:
                    aleatorio_d = choice(metodos_de_estudo)
               a.write(f'Estudar: {aleatorio_d}')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               while aleatorio_e == aleatorio_b:
                    aleatorio_e = choice(limpar)
               a.write(f'Limpar e Organizar: {aleatorio_e}')
               a.write('\n')             
               a.write('-' * 30)
               a.write('\n')
               a.write('Ir para o Trabalho: 13:30')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               a.write('Voltar do Trabalho: 00:40')
               a.write('\n')
          except:
               print('Houve um ERRO na hora de escrever os dados!')
          else:
               print('Cronograma Registrado')
               a.close()

