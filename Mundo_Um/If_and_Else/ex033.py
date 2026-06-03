primeiro = int(input('Digite um número: '))
segundo = int(input('Digite outro número: '))
terceiro = int(input('Digite mais um número: '))
menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
print(f'O maior valor é {maior}.')
print(f'O menor valor é {menor}.')