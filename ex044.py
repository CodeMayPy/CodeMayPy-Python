'''
#Versão antiga
#Gerenciador de Pagamentos
#44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/pix: 10% de desconto
# débito : 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros
preco = float(input('Qual o valor da sua compra R$:'))
print('''Qual a forma de pagamento?
[ 1 ] à vista (dinheiro ou pix)
[ 2 ] à vista (cartão de débito)
[ 3 ] 2x cartão de crédito
[ 4 ] 3x ou mais cartão de crédito''')
'''escolha = int(input('Qual a forma de pagamento?'))
if escolha == 1:
    print(f'Sua compra de R${preco} receberá desconto de 10% e ficará R${preco - (preco*0.10):.2f}.')
elif escolha == 2:
    print(f'Sua compre de R${preco} no débito ganha 5% de desconto e fica R${preco - (preco*0.05):.2f}.')
elif escolha == 3:
    print(f'Sua compre de R${preco} parcelada em 2x ficará em duas parcelas de R${preco/2:.2f}.')
elif escolha == 4:
    print(f'Sua compra de R${preco} em 3x ou mais terá a adição de 20% de juros e ficará no total R${preco +(preco*0.20):.2f}.')
'''

#Versão revisada

preco = float(input('Digite o valor do produto R$: '))

opcao = int(input('Selecione a forma de pagamento:\n[1]- Dinheiro/Pix.\n[2]- À vista cartão.\n[3]- Até 2x no cartão.\n[4]- 3x ou mais no cartão.\nOpção: '))

if opcao == 1:
    print(f'Você escolheu À vista/pix e o valor da sua compra de R$ {preco} com desconto de 10% ficou R$ {preco - (preco * 0.10):.2f}.')
elif opcao == 2:
    print(f'Você escolheu À vista no cartão e sua compra de R$ {preco} com desconto 5% ficou R$ {preco - (preco * 0.05):.2f}.')
elif opcao == 3:
    print(f'Você escolheu em Até 2x e o preço do seu produto é de R$ {preco} e parcelado fica R$ {preco/2:.2f}.')
elif opcao == 4:
    print(f'Você escolheu em 3x ou mais e seu produto de R$ {preco} com o acrescimo de 20% ficará de R$ {preco + (preco * 0.20):.2f}.')       
else:
    print('Opção inválida, tente novamente.')
