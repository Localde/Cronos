from random import choice
from packs.atividadesaleatorias import brainstorm_exercicios

def estudoMonofasico(arq):
     try:
          a = open(arq, 'at')
     except Exception:
          print('Houve um ERRO na hora de escrever os dados!')
     else:
          try:
               metodos_de_estudo = ['Assistir Video Aulas', 'Leitura Intensiva', 'Resolver Atividades', 'Fazer Engenharia Reversa', 'Fazer Trabalho de Pesquisa']
               materias = ['Python', 'PHP', 'Javascript']
               aleatorio_a = choice(metodos_de_estudo)
               aleatorio_c = choice(materias)
               aleatorio_d = choice(metodos_de_estudo)

               while aleatorio_d == aleatorio_a:
                    aleatorio_d = choice(metodos_de_estudo)

               if aleatorio_a or aleatorio_d == 'Resolver Atividades':
                    

               a.write('Cronograma de Estudo\n\n')

               a.write('01:30 - Dormir\n')
               a.write('09:30 - Acordar\n\n')
               
               a.write(f'Linguagem do Dia: {aleatorio_c}\n\n')
               
               a.write('1# Fazer Duolingo\n')
               a.write('2# Ler 10 paginas\n')
               a.write('3# Assistir uma video aula\n')
               a.write('4# Resolver uma atividade\n\n')

               a.write('Tarefas Extras:\n')
               a.write(f'{aleatorio_a}\n')
               a.write(f'{aleatorio_d}')
               
          except:
               print('Houve um ERRO na hora de escrever os dados!')
          else:
               print('Cronograma Registrado')
               a.close()


