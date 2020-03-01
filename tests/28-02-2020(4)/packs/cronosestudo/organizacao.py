from random import sample

def limpeza(arq):
     try:
          file = open(arq, 'at')
     except Exception:
          print('Houve um ERRO na hora de escrever os dados!')
     else:
          try:
               
               limpeza = [
                    'Quarto Pessoal',
                    'Quarto de Visita',
                    'Banheiro Pessoal',
                    'Banheiro de Visita',
                    'Cozinha',
                    'Area de limpeza',
                    'Sala',
                    'Corredor'
                    ]
               
               a = sample(limpeza, 3)

               file.write(f'Limpeza e Organização:\n\n')
               
               file.write('1# Lavar Louça\n')

               cont = 2
               for dado in a:
                    file.write(f'{cont}# {dado}\n')
                    cont += 1
                         
          except:
               print('Houve um ERRO na hora de escrever os dados!')
          else:
               print('Cronograma Registrado')
               file.close()

