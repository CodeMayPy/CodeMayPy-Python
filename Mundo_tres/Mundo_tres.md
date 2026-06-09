<a name="topo"></a>

# Mundo 3 - Estrutura de dados, funções, módulos, pacotes e tratamento de erros.

## Sumário de Explorações
<br> 

1. [Tuplas](#tuplas)
2. [Listas](#listas)
3. 
4. 

<br>

## Tuplas

➔ As tuplas (`tuple`) são estruturas de dados integradas ao Python que funcionam como uma **sequência de valores**, de forma muito semelhante às listas, porém com uma diferença crucial: elas são **imutáveis**. Isso significa que, uma vez que uma tupla é criada, seus elementos **não podem** ser alterados, adicionados ou removidos. <br>
➔ No passado, dizia-se que *"As variáveis simples usam igual (`=`), as Tuplas usam parênteses `()`"*. Nas versões modernas do Python, os parênteses são opcionais na declaração, mas o Python sempre vai te mostrar a resposta entre parênteses!<br>
Exemplo de tuplas:
```python 
# Formas de declarar uma Tupla:
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

doces = 'Chocolate', 'Bala', 'Chiclete'  # Também funciona!

sucos = ('morango',) #tupla de valor único é representada com uma vírgula(,) no final.

print(lanche)  
'''Saída: 
('Hambúrguer', 'Suco', 'Pizza', 'Pudim')'''
```
**⚠️ AS TUPLAS SÃO IMUTÁVEIS!** <br>

➔ **Dados heterogêneos:** Elas aceitam misturar tipos promitivos diferentes dentro da mesma estrutura (`int`, `str` e `float` juntos). <br>

➔ **Acesso por índice:** Cada elemento tem uma posição, começando do `0`.<br>
```Python
lanche = ('Hamburguer', 'Suco', 'Pizza')
print(lanche[0])  
'''Saída: 
Hambúrguer'''
```
➔ **Operações e Métodos:**<br>

🔹**Contar elementos (`len`):** Mostra o tamanho total da tupla. <br> 
🔹**Contar repetições (`.count()`):** Mostra quantas vezes um valor específico aparece.<br>
🔹**Descobrir a posição (`.index()`):** Mostra em qual posição (índice) está o elemento que você busca. <br>
🔹**Juntar tuplas (`+`):** Você não soma os valores, você **junta** as duas tuplas criando uma nova. <br>
Exemplo:
```Python
numeros = (2, 5, 4, 2, 8, 2)

print(len(numeros))          # Saída: 6 (total de elementos)
print(numeros.count(2))      # Saída: 3 (o número 2 aparece 3 vezes)
print(numeros.index(8))      # Saída: 4 (o número 8 está na posição 4)

a = (1, 2, 3)
b = (4, 5)
c = a + b
print(c)                     # Saída: (1, 2, 3, 4, 5)
```
<br>

🔹**Fatiamento básico:**
- `lanche[1:3]`: Pega o índice 1 até o 2. <br>
- `lanche [-1]`: Pega o último elemento (ordem reversa). <br>

🔹**Iterando com `for`:**
```Python
lanche = ('Hambúrguer', 'Suco', 'Pizza')

# Forma 1 (Mais simples - foca no elemento):
for comida in lanche:
    print(f'Eu vou comer {comida}')

# Forma 2 (Usando range - bom se precisar da posição):
for posicao in range(0, len(lanche)):
    print(f'Vou comer {lanche[posicao]} na posição {posicao}')

# Forma 3 (Usando enumerate - te dá o elemento e a posição de uma vez!):
for posicao, comida in enumerate(lanche):
    print(f'Vou comer {comida} que está na posição {posicao}')
```

<br>

[↑ Voltar ao topo](#topo)

## Listas

➔As listas (`list`) são coleções de itens organizados em uma ordem específica. Elas são representadas por colchetes `[]`, com elementos individuais separados por vírgulas. Diferente das strings e tuplas, as listas são **mutáveis**, permitindo que você altere, adicione ou remova elementos após sua criação.<br>
➔ Armazenam múltiplos valores em uma única variável, mantendo uma ordem específica baseada em índices (`0`, `1`, `2`...).<br>
➔ É possível criar uma lista vazia usando a função `list()`.<br>
Exemplo de lista:
```python 
# Formas de declarar uma Lista:
lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
valores = list()  # Cria uma lista vazia pronta para receber dados

print(lanche)  # Saída: ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
```
**⚡ AS LISTAS SÃO MUTÁVEIS!**

➔**Manipulação e Métodos Avançados:** <br>
🔹**Adicionando no final da lista `.append()`:** Adiciona o novo dado para a última posição da lista. <br>
🔹**Adicionando em uma posição específica `.insert()`:** Você informa o índice e o valor onde deseja que o novo dado apareça.<br>
Exemplos:
```Python
num = [2, 5, 9]

num.append(7)        # num vira [2, 5, 9, 7]
num.insert(1, 0)     # Insere o 0 na posição 1. num vira [2, 0, 5, 9, 7]
```
🔹**Removendo pelo índice `.pop()`:** Remove o elemento do índice indicado. Se você não informar nenhum número, ele apaga o **último** da lista.<br>
🔹**Removendo pelo valor `.remove()`:** Procura o elemento pelo nome/conteúdo e apaga a **primeira** ocorrência que encontrar. <br>
🔹**comando geral `del`:** Apaga um índice ou a lista inteira da memória.
Exemplos:
```Python

lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']

del lanche[1]        # Apaga o índice 1 ('Suco')
lanche.pop(2)        # Apaga quem ficou no índice 2 ('Pudim')
lanche.remove('Pizza') # Remove o valor 'Pizza' pelo nome
```
🔹**Ordenar `.sort()`:** Coloca a lista em **ordem** alfabética ou númerica **crescente**.<br>
🔹**Ordem reversa `.sort(reverse=True)`:** Coloca tudo da lista de trás pra frente. <br>
🔹**Tamanho total `len()`:** Conta quantos elementos existem na lista. <br>
Exemplos:
```Python

valores = [8, 2, 5, 4, 1]

valores.sort()               # Vira [1, 2, 5, 4, 8]
valores.sort(reverse=True)   # Vira [8, 5, 4, 2, 1]
print(len(valores))          # Saída: 5
```
 <br>
 
⚠️ **CUIDADO, JOVEM PADAWAN!** Esta é a maior armadilha de Listas em Python!<br>
Se você apenas igualar uma lista a outra `(a = b)`, o Python não cria uma cópia. Ele cria uma ligação entre elas. Se você mudar a lista b, a lista a também muda!<br>

➔ Como criar uma cópia real? Use o fatiamento completo de strings/listas ([:]). <br>

```Python

a = [1, 2, 3]

#Criando uma ligação (Perigoso!!!!!!!):
b = a
b[0] = 9   # Alterou b, mas 'a' também vai virar [9, 2, 3]!

#Criando uma cópia de verdade (Forma correta):
b = a[:]
b[0] = 5   # Agora apenas 'b' muda, 'a' continua intacta!
```

<br>

[↑ Voltar ao topo](#topo)

##

🔹➔ 🔹➔ 🔹➔ 

<br>

[↑ Voltar ao topo](#topo)
