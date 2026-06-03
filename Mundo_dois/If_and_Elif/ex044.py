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