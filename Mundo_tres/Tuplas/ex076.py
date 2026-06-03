#076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No
# final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ( 'cleasing oil', 69.99,
             'Gloss', 10.90,
             'Serúm', 15.99,
             'Sombra', 25.90,
             'Batom matte', 12.90,
             'Protetor solar', 49.99,
             'Base', 22.99,
             'Blush', 15.99,
             'Base em pó', 23.99)
print('Lojinha da May:')
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<20}', end=' ')
    else:
     print(f'R$ {produtos[pos]:>5.2f}')