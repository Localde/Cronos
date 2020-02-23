from random import sample

lista = []

print('[A] Mundo 1')
print('[B] Mundo 2')
print('[C] Mundo 3')
escolha = str(input()).lower()
while True:
    if escolha == 'a':
        for cont in range(1, 36):
            lista.append(cont)
        aleatorio = sample(lista, 10)
        for a in range(0, 10):
            print(f'Exercicio {aleatorio[a]};')
    elif escolha == 'b':
        for cont in range(36, 72):
            lista.append(cont)
        aleatorio = sample(lista, 10)
        for a in range(0, 10):
            print(f'Exercicio {aleatorio[a]};')
    elif escolha == 'c':
        for cont in range(72, 96):
            lista.append(cont)
        aleatorio = sample(lista, 10)
        for a in range(0, 10):
            print(f'Exercicio {aleatorio[a]};')
    if 'abc' in escolha:
        break
    else:
        lista.clear()
        escolha = str(input()).lower()

print('-=-' * 30)
print('''
Area para salvar:



''')
print('-=-' * 30)
input()
