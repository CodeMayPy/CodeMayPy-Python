lista = []
lista_ordenada = []

for c in range(0, 5):
    numero = int(input(f'Digite o {c+1}º número da sua lista: '))
    lista.append(numero)

for item in lista:
    if not lista_ordenada:
        lista_ordenada.append(item)
    else:
        inserido = False
        for i in range(len(lista_ordenada)):
            if item < lista_ordenada[i]:
                lista_ordenada.insert(i, item)
                inserido = True
                break
        if not inserido:
            lista_ordenada.append(item)

print(f'Sua lista em ordem crescente é: {lista_ordenada}')