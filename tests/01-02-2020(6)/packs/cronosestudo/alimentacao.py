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

               cafe_da_manha_random = choice(cafe_da_manha)

               cafe_da_manha2 = [
                    'banana: 1 unidade',
                    'abacate: 4 pedaços'
                    ]

               cafe_da_manha2_random = choice(cafe_da_manha2)

               lanche_da_manha = [
                    'Iogurte natural'
                    ]

               lanche_da_manha_random = choice(lanche_da_manha)
               
               lanche_da_manha2 = [
                    'Maçã vermelha: 1 unidade',
                    'Pera: 1 unidade',
                    'Melão: 1 fatia',
                    'Kiwi: 1 unidade',
                    'Mamão: 1 fatia',
                    'Banana: 1 unidade'
                    ] # Pode picar e acrescentar 01 colher de sopa de farelo de aveia + 01 colher de sobremesa de canela em pó.

               lanche_da_manha2_random = choice(lanche_da_manha2)

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

               almoço_salada_folhas_random = choice(almoço_salada_folhas)

               almoço_salada = [
                    'Tomate picadinho: 05 colheres de sopa',
                    'Pepino: 05 colheres de sopa',
                    'Cenoura crua ralada: 04 colheres de sopa',
                    'Beterraba crua ralada: 06 colheres de sopa'
                    ]

               almoço_salada_random = choice(almoço_salada)

               almoço_carboidrato = [
                    'Batata doce cozida: 1 unidade média',
                    'Arroz integral: 01 escumadeira',
                    'Purê de Batata doce: 04 colheres de sopa',
                    'Mandioca: 03 pedaços',
                    'Macarrão Integral: 01 1/2 pegador'
                    ]

               almoço_carboidrato_random = choice(almoço_carboidrato)

               almoço_ferro = [
                    'Feijão Carioca: 01 concha média',
                    'Feijão Preto: 01 concha média',
                    'Ervilha: 04 colheres de sopa'
                    ]

               almoço_ferro_random = choice(almoço_ferro)

               almoço_proteina = [
                    'Bife bovino grelhado: 01 unidade grande',
                    'Carne moida: 05 colheres de sopa',
                    'Almondegas: 5 unidades médias',
                    'Carne bovina de panela: 03 pedaços médios',
                    'Carne bovina picadinha: 05 colheres de sopa',
                    'Omelete: 01 unidade de 4 claras e 1 gema.'
                    ]
               
               almoço_proteina_random = choice(almoço_proteina)

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

               almoço_sopa_random = choice(almoço_sopa)

               almoço_suco = [
                    'Suco de frutas natural(30 min após refeição): 1 copo de 200 ml'
                    ]

               almoço_suco_random = choice(almoço_suco)

               lanche_da_tarde = [
                    'Ovos mexidos: 03 claras e 01 gema + Torrada c/ orégano + fio de azeite: 3 unidades',
                    'Panqueca de clara de ovos: 1 unidade de 4 ovos + farelo de aveia: 02 colheres de sopa + Banana: 1 unidade',
                    'Omelete: 1 unidade de 4 claras e 1 gema + Queijo ricota picadinha: 1 fatia + Farelo de aveia: 1 colher de sopa',
                    'Ovos cozidos: 03 unidades + fio de azeite e orégano(opcional) + Batata doce cozida: 1 unidade(100g)',
                    'Crepioca: 01 unidade pequena + Chia: 1 colher de sopa + File de frango desfiado: 1 unidade pequena',
                    'Tapioca: 01 unidade + Ovos mexidos: 02 unidades + Ricota: 01 fatia + Chia: 01 colher de sopa'
                    ]

               lanche_da_tarde_random = choice(lanche_da_tarde)

               jantar_salada_folhas = [
                    'Alfaca: A vontade',
                    'Acelga: A vontade',
                    'Agrião: A vontade',
                    'Repolho roxo: A vontade',
                    'Espinafre: A vontade',
                    'Couve manteiga: A vontade',
                    'Repolho: A vontade',
                    ]

               jantar_salada_folhas_random = choice(jantar_salada_folhas)

               jantar_salada = [
                    'Salada de cenoura cozida: 03 colheres de sopa',
                    'Brotinho de couve-flor cozida: 05 unidades',
                    'Beterraba cozida: 04 colheres de sopa.'
                    'Brotinho de Brócolis cozido: 05 unidades'
                    ]

               jantar_salada_random = choice(jantar_salada)
               
               jantar_carbo = [
                    'Batata doce cozida: 1 unidade'
                    ]

               jantar_carbo_random = choice(jantar_carbo)
               
               jantar_proteina = [
                    'Peixe grelhado: 01 filé médio',
                    'Peixe Assado: 01 filé',
                    'Peixe molho(cozido): 01 filé',
                    'Bife de Frango Grelhado: 01 unidade média',
                    'Frango Cozido: 02 pedaços',
                    'Omelete: 1 unidade de 4 claras e 1 gema(pode acrescentar queijo magro, cenoura crua ralada, 01 colher de sopa de farinha de aveia, frango desfiado e etc)',
                    ]

               jantar_proteina_random = choice(jantar_proteina)
               
               jantar_sopa = [
                    'Quiabo: 04 colheres de sopa',
                    'Milho Refogado: 03 colheres de sopa',
                    'Abobrinha verde: 03 colheres de sopa',
                    'Abobora cabotiã: 05 pedaços pequenos',
                    'Berinjela cozida: 04 colheres de sopa',
                    'Chuchu cozido: 03 colheres'
                    ]

               jantar_sopa_random = choice(jantar_sopa)

               jantar_suco = [
                    'Suco natural de frutas: 1 copo de 200 ml + Pedrinhas de gelo de suco de tomate - Se tiver dor  muscular (30 min após refeição)'
                    ]

               jantar_suco_random = choice(jantar_suco)

               ceia = [
                    'Iogurte natural: 01 unidade + mel: 01 colher de chá + morangos: 03 unidades',
                    'Iogurte natural: 01 unidade + mel: 01 colher de chá + banana: 01 unidade + canela: 01 colher de sobremesa',
                    'Iogurte natural: 01 unidade + mel: 01 colher de chá + abacate: 03 pedaços + cacau em pó: 01 colher de sobremesa'
                    ]

               ceia_random = choice(ceia)

               file.write('\n\nCAFÉ DA MANHÃ 08:00\n\n')

               file.write(f'{cafe_da_manha_random}\n')

               file.write(f'{cafe_da_manha2_random}')
          
               file.write('\n\nLANCHE DA MANHÃ 11:00\n\n')

               file.write(f'{lanche_da_manha_random}\n')

               file.write(f'{lanche_da_manha2_random}')

               file.write('\n\nALMOÇO 13:00\n\n')

               file.write(f'{almoço_salada_folhas_random}\n')

               file.write(f'{almoço_salada_random}\n')

               file.write(f'{almoço_carboidrato_random}\n')

               file.write(f'{almoço_ferro_random}\n')

               file.write(f'{almoço_proteina_random}\n')

               file.write(f'{almoço_sopa_random}\n')

               file.write(f'{almoço_suco_random}')

               file.write('\n\nLANCHE DA TARDE 16:00 - PÓS TREINO\n\n')

               file.write(f'{lanche_da_tarde_random}')

               file.write('\n\nJANTAR 18:30\n\n')

               file.write(f'{jantar_salada_folhas_random}\n')

               file.write(f'{jantar_salada_random}\n')

               file.write(f'{jantar_carbo_random}\n')

               file.write(f'{jantar_proteina_random}\n')

               file.write(f'{jantar_sopa_random}\n')

               file.write(f'{jantar_suco_random}')

               file.write('\n\nCEIA 22:30\n\n')

               file.write(f'{ceia_random}')
               
          except:
               print('Houve um ERRO na hora de escrever os dados!')
          else:
               print('Cronograma Registrado')
               file.close()

