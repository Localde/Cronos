from datetime import datetime

def estudoMonofasico(arq):
     try:
          a = open(arq, 'at')
     except Exception:
          print('Houve um ERRO na hora de escrever os dados!')
     else:
          try:
               #metodos_de_estudo = ['Assistir Video Aulas', 'Leitura Intensiva', 'Resolver Atividades', 'Fazer Engenharia Reversa', 'Fazer Trabalho de Pesquisa']
               #materias = ['Python', 'PHP', 'Javascript']
               #aleatorio_a = choice(metodos_de_estudo)
               #aleatorio_c = choice(materias)
               #aleatorio_d = choice(metodos_de_estudo)

               dormir = float(input('Que horas vai dormir?'))

               #while aleatorio_d == aleatorio_a:
                    #aleatorio_d = choice(metodos_de_estudo)

               a.write(f'{dormir} - Dormir')
               a.write(f'{dormir + 8}')
               
          except:
               print('Houve um ERRO na hora de escrever os dados!')
          else:
               print('Cronograma Registrado')
               a.close()


