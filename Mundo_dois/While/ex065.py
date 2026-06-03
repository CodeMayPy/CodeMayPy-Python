resposta = "S"
media = soma = quantidade = maior = menor = 0
while resposta in "Ss":
    numero = int(input("Digite um número:"))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input("Quer continuar?")).upper().strip()[0]
media = soma / quantidade
print(f"Você digitou {quantidade} e a média é {media}.")
print(f"O maior é {maior} e o menor é {menor}.")