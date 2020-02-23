from random import sample

def escolhaAtividade(arq):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            lista = []

            print('[A] Mundo 1')
            print('[B] Mundo 2')
            print('[C] Mundo 3')
            escolha = str(input()).lower()
            
            if escolha == 'a':
                for cont in range(1, 36):
                    lista.append(cont)
                aleatorio = sample(lista, 10)
                for a in range(0, 10):
                    continue
            elif escolha == 'b':
                for cont in range(36, 72):
                    lista.append(cont)
                aleatorio = sample(lista, 10)
                for b in range(0, 10):
                    continue
            elif escolha == 'c':
                for cont in range(72, 96):
                    lista.append(cont)
                aleatorio = sample(lista, 10)
                for c in range(0, 10):
                    continue
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print('Registro adicionado com sucesso!')
            a.close()

