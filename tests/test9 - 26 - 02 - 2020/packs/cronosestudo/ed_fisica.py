from random import choice

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
               
               materias = [
                    'Superior',
                    'Inferior',
                    'Centro'
                    ]

               submetodos_de_isotonico = [
                    'Múltiplas Séries',
                    'Pirâmide',
                    'Bi-Set – (hipertrofia)',
                    'Tri-Set – (hipertrofia)',
                    'Super-Set',
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
               
               a = choice(metodos)
               b = choice(submetodos_de_isotonico)
               c = choice(materias)

               file.write('Cronograma de Ed.Fisica\n\n')

               file.write(f'Treino do Dia: {c}\n\n')
               
               file.write('1# Descansar Bem.\n')
               file.write('2# Estudar o metodo do dia.\n')
               file.write('3# Fazer aquecimento da materia.\n')
               file.write('4# Se alimentar direito.\n\n')

               file.write('Tarefas Extras:\n')
               

               if a == 'Isotônico':
                    if b == 'Múltiplas Séries':
                         multiplas_series = ['hipertrofia', 'força']
                         random_mult = choice(multiplas_series)
                         file.write(f'{a} - {b} - {random_mult}')
                    elif b == 'Pirâmide':
                         piramide = ['força', 'hipertrofia']
                         random_pira = choice(piramide)
                         file.write(f'{a} - {b} - {random_pira}')
                    elif c == 'Super-Set':
                         superset = ['hipertrofia','força e hipertrofia']
                         random_superset = choice(superset)
                         file.write(f'{a} - {b} {random_superset}')
                    else:
                         file.write(f'{a} - {b}')
               else:
                    file.write(f'{a}')
                         
          except:
               print('Houve um ERRO na hora de escrever os dados!')
          else:
               print('Cronograma Registrado')
               file.close()

