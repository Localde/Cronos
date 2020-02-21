from aleatorio import *


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
               aa = Null
               bb = Null
               cc = Null
               dd = Null
               ee = Null
               
               a.write(f'Linguagem do Dia: {aleatorioC(aa)}')
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
               a.write(f'Estudar: {aleatorioA(a=bb)}')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               a.write('Almoçar: 12:30')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               a.write(f'Limpar e Organizar: {aleatorioB(a=cc)}')
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
               a.write(f'Estudar: {aleatorioA(b=dd)}')
               a.write('\n')
               a.write('-' * 30)
               a.write('\n')
               a.write(f'Limpar e Organizar: {aleatorioB(b=ee)}')
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

