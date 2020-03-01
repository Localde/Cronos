from random import choice

def estudo(arq):
     try:
          file = open(arq, 'at')
     except Exception:
          print('Houve um ERRO na hora de escrever os dados!')
     else:
          try:
               metodos = [
                    #'Assistir Video Aulas',
                    'Intensive reading with Skimming and Scanning;'
                    #'Resolver Atividades',
                    #'Fazer Engenharia Reversa (Recriar Softwares)',
                    #'Fazer Trabalho de Pesquisa'
                    ]
               
               #materias = [
               #     'Python',
               #     'PHP',
               #     'Javascript'
               #     ]
               
               #a = choice(metodos)
               #b = choice(metodos)
               #c = choice(materias)

               #while a == b:
               #     a = choice(metodos)

               file.write('Cronograma de Estudo\n\n')

               file.write('Domingo - CONCURSO EAGS e Python\n')
               file.write('Segunda - CONCURSO EAGS e Python\n')
               file.write('Terça - CONCURSO EAGS e Python\n')
               file.write('Quarta - CONCURSO EAGS e Python\n')
               file.write('Quinta - CONCURSO EAGS e Python\n')
               file.write('Sexta - CONCURSO EAGS e Python\n')
               file.write('Sabado - CONCURSO EAGS e Python\n\n')
               
               file.write('1# Fazer Duolingo\n')
               file.write('2# Ler 10 paginas\n')
               file.write('3# Assistir uma video aula\n')
               file.write('4# Resolver uma atividade\n\n')

               file.write('Tarefas Extras:\n')

               file.write(f'{metodos}')

               #if a == 'Fazer Engenharia Reversa (Recriar Softwares)':
               #     if c == 'Python':
               #          softwares_python = ['Estatisticas']
               #          random_python = choice(softwares_python)
               #          file.write(f'{a} - {random_python}')
               #     elif c == 'PHP':
               #          softwares_php = ['Classificados']
               #          random_php = choice(softwares_php)
               #          file.write(f'{a} - {random_php}')
               #     elif c == 'Javascript':
               #          softwares_javascript_reactnative = ['Devmaps']
               #          random_javascript = choice(softwares_javascript_reactnative)
               #          file.write(f'{a} - {random_javascript}')
               #elif b == 'Fazer Engenharia Reversa (Recriar Softwares)':
               #     if c == 'Python':
               #          softwares_python = ['Estatisticas']
               #          random_python = choice(softwares_python)
               #          file.write(f'{b} - {random_python}')
               #     elif c == 'PHP':
               #          softwares_php = ['Classificados']
               #          random_php = choice(softwares_php)
               #          file.write(f'{b} - {random_php}')
               #     elif c == 'Javascript':
               #          softwares_javascript_reactnative = ['Devmaps']
               #          random_javascript = choice(softwares_javascript_reactnative)
               #          file.write(f'{b} - {random_javascript}')
               #else:
               #     file.write(f'{a}\n')
               #     file.write(f'{b}')          
               #          
          except:
               print('Houve um ERRO na hora de escrever os dados!')
          else:
               print('Cronograma Registrado')
               file.close()

