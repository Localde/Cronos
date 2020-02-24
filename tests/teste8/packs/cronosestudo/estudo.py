from random import choice

def estudoMonofasico(arq):
     try:
          a = open(arq, 'at')
     except Exception:
          print('Houve um ERRO na hora de escrever os dados!')
     else:
          try:
               metodos_de_estudo = ['Assistir Video Aulas', 'Leitura Intensiva', 'Resolver Atividades', 'Fazer Engenharia Reversa (Recriar Softwares)', 'Fazer Trabalho de Pesquisa']
               materias = ['Python', 'PHP', 'Javascript']
               aleatorio_a = choice(metodos_de_estudo)
               aleatorio_c = choice(materias)
               aleatorio_d = choice(metodos_de_estudo)

               while aleatorio_d == aleatorio_a:
                    aleatorio_d = choice(metodos_de_estudo)

               a.write('Cronograma de Estudo\n\n')

               a.write('01:30 - Dormir\n')
               a.write('09:30 - Acordar\n\n')
               
               a.write(f'Linguagem do Dia: {aleatorio_c}\n\n')
               
               a.write('1# Fazer Duolingo\n')
               a.write('2# Ler 10 paginas\n')
               a.write('3# Assistir uma video aula\n')
               a.write('4# Resolver uma atividade\n\n')

               a.write('Tarefas Extras:\n')
               

               if aleatorio_a == 'Fazer Engenharia Reversa (Recriar Softwares)':
                    if aleatorio_c == 'Python':
                         softwares_python = ['Estatisticas']
                         random_python = choice(softwares_python)
                         a.write(f'{aleatorio_a} - {random_python}')
                    elif aleatorio_c == 'PHP':
                         softwares_php = ['Classificados']
                         random_php = choice(softwares_php)
                         a.write(f'{aleatorio_a} - {random_php}')
                    elif aleatorio_c == 'Javascript':
                         softwares_javascript_reactnative = ['Devmaps']
                         random_javascript = choice(softwares_javascript_reactnative)
                         a.write(f'{aleatorio_a} - {random_javascript}')
               elif aleatorio_d == 'Fazer Engenharia Reversa (Recriar Softwares)':
                    if aleatorio_c == 'Python':
                         softwares_python = ['Estatisticas']
                         random_python = choice(softwares_python)
                         a.write(f'{aleatorio_d} - {random_python}')
                    elif aleatorio_c == 'PHP':
                         softwares_php = ['Classificados']
                         random_php = choice(softwares_php)
                         a.write(f'{aleatorio_d} - {random_php}')
                    elif aleatorio_c == 'Javascript':
                         softwares_javascript_reactnative = ['Devmaps']
                         random_javascript = choice(softwares_javascript_reactnative)
                         a.write(f'{aleatorio_d} - {random_javascript}')
               else:
                    a.write(f'{aleatorio_a}\n')
                    a.write(f'{aleatorio_d}')          
                         
          except:
               print('Houve um ERRO na hora de escrever os dados!')
          else:
               print('Cronograma Registrado')
               a.close()


def estudoBifasico(arq):
     try:
          a = open(arq, 'at')
     except Exception:
          print('Houve um ERRO na hora de escrever os dados!')
     else:
          try:
               metodos_de_estudo = ['Assistir Video Aulas', 'Leitura Intensiva', 'Resolver Atividades', 'Fazer Engenharia Reversa (Recriar Softwares)', 'Fazer Trabalho de Pesquisa']
               materias = ['Python', 'PHP', 'Javascript']
               aleatorio_a = choice(metodos_de_estudo)
               aleatorio_c = choice(materias)
               aleatorio_d = choice(metodos_de_estudo)

               while aleatorio_d == aleatorio_a:
                    aleatorio_d = choice(metodos_de_estudo)

               a.write('Cronograma de Estudo\n\n')

               a.write('01:30 - Dormir\n')
               a.write('07:30 - Acordar\n\n')
               a.write('13:30 - Dormir\n')
               a.write('14:00 - Acordar\n\n')
               
               a.write(f'Linguagem do Dia: {aleatorio_c}\n\n')
               
               a.write('1# Fazer Duolingo\n')
               a.write('2# Ler 10 paginas\n')
               a.write('3# Assistir uma video aula\n')
               a.write('4# Resolver uma atividade\n\n')

               a.write('Tarefas Extras:\n')


               if aleatorio_a == 'Fazer Engenharia Reversa (Recriar Softwares)':
                    if aleatorio_c == 'Python':
                         softwares_python = ['Estatisticas']
                         random_python = choice(softwares_python)
                         a.write(f'{aleatorio_a} - {random_python}')
                    elif aleatorio_c == 'PHP':
                         softwares_php = ['Classificados']
                         random_php = choice(softwares_php)
                         a.write(f'{aleatorio_a} - {random_php}')
                    elif aleatorio_c == 'Javascript':
                         softwares_javascript_reactnative = ['Devmaps']
                         random_javascript = choice(softwares_javascript_reactnative)
                         a.write(f'{aleatorio_a} - {random_javascript}')
               elif aleatorio_d == 'Fazer Engenharia Reversa (Recriar Softwares)':
                    if aleatorio_c == 'Python':
                         softwares_python = ['Estatisticas']
                         random_python = choice(softwares_python)
                         a.write(f'{aleatorio_d} - {random_python}')
                    elif aleatorio_c == 'PHP':
                         softwares_php = ['Classificados']
                         random_php = choice(softwares_php)
                         a.write(f'{aleatorio_d} - {random_php}')
                    elif aleatorio_c == 'Javascript':
                         softwares_javascript_reactnative = ['Devmaps']
                         random_javascript = choice(softwares_javascript_reactnative)
                         a.write(f'{aleatorio_d} - {random_javascript}')
               else:
                    a.write(f'{aleatorio_a}\n')
                    a.write(f'{aleatorio_d}')          
               
          except:
               print('Houve um ERRO na hora de escrever os dados!')
          else:
               print('Cronograma Registrado')
               a.close()

