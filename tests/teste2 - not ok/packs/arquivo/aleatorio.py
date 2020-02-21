from random import choice

def aleatorioA(a=aleatorio_a, b=aleatorio_d):
    metodos_de_estudo = ['Assistir Video Aulas', 'Leitura Intensiva', 'Resolver Atividades', 'Fazer Engenharia Reversa']
    aleatorio_a = choice(metodos_de_estudo)
    aleatorio_d = choice(metodos_de_estudo)
    while aleatorio_d == aleatorio_a:
        aleatorio_d = choice(metodos_de_estudo)
               

def aleatorioB(a=aleatorio_b, b=aleatorio_e):
    limpar = ['Cozinha', 'Sala', 'Quarto onde Dorme', 'Quarto onde não dorme', 'Banheiro do corredor', 'Banheiro do quarto onde dorme', 'Area do tanquinho']
    aleatorio_b = choice(limpar)
    aleatorio_e = choice(limpar)
    while aleatorio_e == aleatorio_b:
        aleatorio_e = choice(limpar)
               

def aleatorioC(aleatorio_c):
    linguagem = ['Python', 'PHP', 'Javascript']
    aleatorio_c = choice(linguagem)    
    
