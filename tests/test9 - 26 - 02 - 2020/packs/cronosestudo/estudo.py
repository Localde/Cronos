from random import choice

def estudo(arq):
     try:
          file = open(arq, 'at')
     except Exception:
          print('Houve um ERRO na hora de escrever os dados!')
     else:
          try:
               metodos = [
                    'Assistir Video Aulas',
                    'Leitura Intensiva',
                    'Resolver Atividades',
                    'Fazer Engenharia Reversa (Recriar Softwares)',
                    'Fazer Trabalho de Pesquisa'
                    ]
               
               materias = [
                    'Python',
                    'PHP',
                    'Javascript'
                    ]
               
               a = choice(metodos_de_estudo)
               b = choice(metodos_de_estudo)
               c = choice(materias)

               while a == b:
                    a = choice(metodos)

               file.write('Cronograma de Estudo\n\n')

               file.write(f'Linguagem do Dia: {c}\n\n')
               
               file.write('1# Fazer Duolingo\n')
               file.write('2# Ler 10 paginas\n')
               file.write('3# Assistir uma video aula\n')
               file.write('4# Resolver uma atividade\n\n')

               file.write('Tarefas Extras:\n')
               

               if a == 'Fazer Engenharia Reversa (Recriar Softwares)':
                    if c == 'Python':
                         softwares_python = ['Estatisticas']
                         random_python = choice(softwares_python)
                         file.write(f'{a} - {random_python}')
                    elif c == 'PHP':
                         softwares_php = ['Classificados']
                         random_php = choice(softwares_php)
                         file.write(f'{a} - {random_php}')
                    elif c == 'Javascript':
                         softwares_javascript_reactnative = ['Devmaps']
                         random_javascript = choice(softwares_javascript_reactnative)
                         file.write(f'{a} - {random_javascript}')
               elif b == 'Fazer Engenharia Reversa (Recriar Softwares)':
                    if c == 'Python':
                         softwares_python = ['Estatisticas']
                         random_python = choice(softwares_python)
                         file.write(f'{b} - {random_python}')
                    elif c == 'PHP':
                         softwares_php = ['Classificados']
                         random_php = choice(softwares_php)
                         file.write(f'{b} - {random_php}')
                    elif c == 'Javascript':
                         softwares_javascript_reactnative = ['Devmaps']
                         random_javascript = choice(softwares_javascript_reactnative)
                         file.write(f'{b} - {random_javascript}')
               else:
                    file.write(f'{aleatorio_a}\n')
                    file.write(f'{aleatorio_d}')          
                         
          except:
               print('Houve um ERRO na hora de escrever os dados!')
          else:
               print('Cronograma Registrado')
               file.close()


def edFisica(arq):
     try:
          file = open(arq, 'at')
     except Exception:
          print('Houve um ERRO na hora de escrever os dados!')
     else:
          try:
               metodos = [
                    'Isotônico',
                    'Isométrico',
                    'Isocinético',
                    'Pliométrico',
                    ]
               materias = ['Superior', 'Inferior', 'Centro']
               a = choice(metodos)
               b = choice(metodos)
               c = choice(materias)

               while a == b:
                    a = choice(metodos)

               file.write('Cronograma de Ed.Fisica\n\n')

               file.write(f'Treino do Dia: {c}\n\n')
               
               file.write('1# Fazer Duolingo\n')
               file.write('2# Ler 10 paginas\n')
               file.write('3# Assistir uma video aula\n')
               file.write('4# Resolver uma atividade\n\n')

               file.write('Tarefas Extras:\n')
               

               if a == 'Isotônico':
                    submetodos = [
                         'Múltiplas Séries (força, hipertrofia, resistência muscular e potência)',
                         'Pirâmide – (força e hipertrofia)',
                         'Bi-Set – (hipertrofia)',
                         'Tri-Set – (hipertrofia)',
                         'Super-Set – (hipertrofia)',
                         'Treinamento em Circuito – (condicionamento físico e resistência muscular)',
                         'Pré-Exaustão – (força e hipertrofia)',
                         'Exaustão – (força, hipertrofia e resistência muscular)',
                         'Repetições Forçadas (Excêntrica) – (força e hipertrofia)',
                         'Blitz – (hipertrofia)',
                         'Drop-Set – (força e hipertrofia)',
                         'Repetições Roubada – (força e hipertrofia)',
                         'Fadiga Excêntrica – (hipertrofia e força)',
                         'SuperLento ou Super Slow – (resistência muscular e hipetrofia)',
                         'Ondulatório – (força, hipertrofia e potência)',
                         'Pausa/Descanso – (força e resistência a fadiga)',
                         'Repetições parciais (oclusão vascular)',
                         'Set 21 – (resistência muscular)',
                         'Repetições parciais pós-fadiga concêntrica – (força)'
                         ]
                    random_submetodos = choice(submetodos)
                    file.write(f'{a} - {random_submetodos}')
               elif b == 'Isotônico':
                    softwares_python = ['Estatisticas']
                    random_python = choice(softwares_python)
                    file.write(f'{aleatorio_d} - {random_python}')
               else:
                    file.write(f'{aleatorio_a}\n')
                    file.write(f'{aleatorio_d}')          
                         
          except:
               print('Houve um ERRO na hora de escrever os dados!')
          else:
               print('Cronograma Registrado')
               file.close()

