from random import choice

def alimentacao(arq):
     try:
          file = open(arq, 'at')
     except Exception:
          print('Houve um ERRO na hora de escrever os dados!')
     else:
          try:
               
               cafe_da_manha = [
                    'Café preto: 1 xícara, Ovos cozidos: 3 unidades, Torrada Integral c/ fio de azeite: 3 unidades',
                    'Ovos mexidos: 3 unidades, Ricota: 1 fatia, Tapioca: 1 unidade',
                    'Omelete: 4 claras + 1 gema, Farelo de aveia: 1 colher de sopa, Ricota ou Cottage: 1 fatia / 2 colheres de sopa',
                    'Panqueca: 1 unidade de 3 ovos, Farelo de aveia: 2 colheres de sopa, Frange desfiado: 4 colheres de sopa'
                    ]

               cafe_da_manha2 = [
                    'banana: 1 unidade',
                    'abacate: 4 pedaços'
                    ]

               lanche_da_manha = [
                    'Iogurte natural'
                    ]
               
               lanche_da_manha2 = [
                    'Maçã vermelha: 1 unidade',
                    'Pera: 1 unidade',
                    'Melão: 1 fatia',
                    'Kiwi: 1 unidade',
                    'Mamão: 1 fatia',
                    'Banana: 1 unidade'
                    ] # Pode picar e acrescentar 01 colher de sopa de farelo de aveia + 01 colher de sobremesa de canela em pó.

               almoço_salada_folhas = [
                    'Salada de folhas (temperado com azeite extra-virgem): Á vontade',
                    'Alface',
                    'acelga',
                    'agrião',
                    'repolho roxo',
                    'espinafre',
                    'couve manteiga',
                    'repolho'
                    ]

               almoço_salada = [
                    'Tomate picadinho: 05 colheres de sopa',
                    'Pepino: 05 colheres de sopa',
                    'Cenoura crua ralada: 04 colheres de sopa',
                    'Beterraba crua ralada: 06 colheres de sopa'
                    ]

               almoço_carboidrato = [
                    'Batata doce cozida: 1 unidade média',
                    'Arroz integral: 01 escumadeira',
                    'Purê de Batata doce: 04 colheres de sopa',
                    'Mandioca: 03 pedaços',
                    'Macarrão Integral: 01 1/2 pegador'
                    ]

               almoço_ferro = [
                    'Feijão Carioca: 01 concha média',
                    'Feijão Preto: 01 concha média',
                    'Ervilha: 04 colheres de sopa'
                    ]

               almoço_proteina = [
                    'Bife bovino grelhado: 01 unidade grande',
                    'Carne moida: 05 colheres de sopa',
                    'Almondegas: 5 unidades médias',
                    'Carne bovina de panela: 03 pedaços médios',
                    'Carne bovina picadinha: 05 colheres de sopa',
                    'Omelete: 01 unidade de 4 claras e 1 gema.'
                    ]
               almoço_sopa = [
                    'Quiabo: 04 colheres de sopa',
                    'Milho refogado: 03 colheres de sopa',
                    'Brotinho de Brócolis cozido: 5 unidades',
                    'Abobrinha verde: 03 colheres de sopa',
                    'Abobora cabotiã: 05 pedaços pequenos',
                    'Berinjela cozida: 04 colheres de sopa',
                    'Chuchu cozido: 03 colheres',
                    'brotinho de couve-flor: 05 colheres '
                    ]

               almoço_suco = [
                    'Suco de frutas natural(30 min após refeição): 1 copo de 200 ml'
                    ]

               lanche_da_tarde = [
                    'Ovos mexidos: 03 claras e 01 gema + Torrada c/ orégano + fio de azeite: 3 unidades',
                    'Panqueca de clara de ovos: 1 unidade de 4 ovos + farelo de aveia: 02 colheres de sopa + Banana: 1 unidade',
                    'Omelete: 1 unidade de 4 claras e 1 gema + Queijo ricota picadinha: 1 fatia + Farelo de aveia: 1 colher de sopa',
                    'Ovos cozidos: 03 unidades + fio de azeite e orégano(opcional) + Batata doce cozida: 1 unidade(100g)',
                    'Crepioca: 01 unidade pequena + Chia: 1 colher de sopa + File de frango desfiado: 1 unidade pequena',
                    'Tapioca: 01 unidade + Ovos mexidos: 02 unidades + Ricota: 01 fatia + Chia: 01 colher de sopa'
                    ]

               jantar_salada_folhas = [
                    'Alfaca: A vontade',
                    'Acelga: A vontade',
                    'Agrião: A vontade',
                    'Repolho roxo: A vontade',
                    'Espinafre: A vontade',
                    'Couve manteiga: A vontade',
                    'Repolho: A vontade',
                    ]

               jantar_salada = [
                    'Salada de cenoura cozida: 03 colheres de sopa',
                    'Brotinho de couve-flor cozida: 05 unidades',
                    'Beterraba cozida: 04 colheres de sopa.'
                    'Brotinho de Brócolis cozido: 05 unidades'
                    ]
               jantar_carbo = [
                    'Batata doce cozida: 1 unidade'
                    ]
               jantar_proteina = [
                    'Peixe grelhado: 01 filé médio',
                    'Peixe Assado: 01 filé',
                    'Peixe molho(cozido): 01 filé',
                    'Bife de Frango Grelhado: 01 unidade média',
                    'Frango Cozido: 02 pedaços',
                    'Omelete: 1 unidade de 4 claras e 1 gema(pode acrescentar queijo magro, cenoura crua ralada, 01 colher de sopa de farinha de aveia, frango desfiado e etc)',
                    ]
               jantar_sopa = [
                    'Quiabo: 04 colheres de sopa',
                    'Milho Refogado: 03 colheres de sopa',
                    'Abobrinha verde: 03 colheres de sopa',
                    'Abobora cabotiã: 05 pedaços pequenos',
                    'Berinjela cozida: 04 colheres de sopa',
                    'Chuchu cozido: 03 colheres'
                    ]
          except:
               print('Houve um ERRO na hora de escrever os dados!')
          else:
               print('Cronograma Registrado')
               file.close()

