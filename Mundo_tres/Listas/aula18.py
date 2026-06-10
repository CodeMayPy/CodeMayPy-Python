# listas dentro de listas
lista = list()
lista.append('bender')
lista.append(1)
cachorros = list()
cachorros.append(lista[:])
lista[0]='cachorro'
lista[1]=2
cachorros.append(lista[:]) #[:] -> copia da lista, sem isso, a lista cachorros teria 2 vezes a mesma lista, ou seja, a mesma referência de memória
print(cachorros)

'''
# exibindo os dados de uma lista dentro de outra lista
galera = [['João', 22],['Maria', 25],['Pedro', 30]]
print(galera[0][0]) #João
print(galera[1]) #['Maria', 25]
print(galera[1][0]) #Maria
print(galera[2][1]) #30


for pessoa in galera:
    print(pessoa)
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
'''
galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #limpa a lista dado para receber os próximos dados

totmaior = totmenor = 0
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
        