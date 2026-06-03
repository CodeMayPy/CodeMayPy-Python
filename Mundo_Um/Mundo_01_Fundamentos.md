<a name="topo"></a>

# ✍️ Resumos de Python

➔ Foi criada por ***Guido Van Rossum***.<br>
➔ É uma linguagem de programação orientada a objeto.<br>
➔ Possui **tipagem dinâmica** (você não precisa dizer se uma variável é `int` ou `str` na hora de criar, o Python descobre sozinho).

    É um sistema de comunicação que permite criar instruções e algoritmos para que o computador execute tarefas específicas. Resumindo, permite você falar com o computador.

➔ **Funfact:**
O nome Python vem do programa de comédia da BBC chamado:"Monty Python's Flying Circus".    

<br>

## Sumário de Explorações
<br> 

1. [Variáveis](#variaveis)
2. [Tipos primitivos](#tipos-primitivos)
3. [Operadores](#operadores)
4. [Estrutura condicional](#estrutura-condicional)


<br>

## 📌 Variáveis

➔ É um nome que se refere a um valor específico. São espaços na memória que podem:<br>
🔹 Armazenar;<br>
🔹 Acessar, e <br>
🔹 Alterar dados.

➔ As variáveis possuem:<br>
🔹 **Tipo** (int, float, str, bool...);<br>
🔹 **Nome** (o que identifica elas);<br>
🔹 **Conteúdo** (o dado em si).

➔ Para declarar uma variável você usa o ***nome*** + ***atribuição de conteúdo***, ex.:
```python 
# Strings (textos) devem sempre estar entre aspas simples ou duplas
fruta = 'maçã'
fruta = "maçã"
numero = '123'

# Números e booleanos não usam aspas
idade = 31
gosta_de_python = True

#Nota: Não precisa usar pontuação no final de uma variável, o código termina em uma quebra de linha.
```

<br>

➔ Nomeando váriaveis:<br>
🔹 **Caracteres permitidos:** Pode usar letras (maiúsculas e minúsculas 'AaBbCc...), números (0123...) e o underline (_).<br>
🔹 **Primeiro caractere:** O Nome de uma váriavel **nunca** pode começar com um número, deve começar com uma letra ou um underline.<br>
🔹 **Pontuação e símbolos:** É **proibido** o uso de qualquer simbolo além do underline, tanto no início como também no final da váriavel.<br>
🔹 **Palavras chaves:** Não pode usar as palavras reservadas como: def, class, True...<br>
🔹 **Case sensitive:** Python é sensível a maiúsculas e minúsculas, `numero`, `Numero` e `NUMERO` são tratadas como variáveis totalmente diferentes. <br>

**Obs.:** Escolha nomes que facilitem a leitura do código e tenham sentido para o valor da váriavel.
Exemplos:
```Python
cor_batom_1 = 'vermelho'
fruta = 'maçã'
tipo_musica = 'pop'
_numero = 2 

#Na comunidade python usar o underline (_) na frente da váriavél pode indicar que é uma váriavel privada e que não deve ser alterada ou acessada diretamente por outras partes do programa.
```

[↑ Voltar ao topo](#topo)

## Tipos primitivos 

Mas May, o que são tipos primitivos e para que servem?

Aí é fácil jovem padawan, os **tipos primitivos** também conhecidos como **tipos de dados simples** ou **básico** são o tempero do nosso código, é o que dá sentido e lógica ao nosso código, os tipos principais são: 

🔹 **Inteiro (`int`):** Representa números inteiros, positivos ou negativos sem parte fracionária. <br>
*Exemplos:* `-5`,`0`,`7` <br>
🔹 **Ponto Flutuante (`float`):** Representa números reais, incluindo os com parte fracionária. <br>
*Exemplos:* `2.5`,`3.1415`,`-0.01`, `4.0`<br>
🔹 **String (`str`):** Representa sequência de caracteres, usadas para armazenar texto *são imutáveis* em Python.<br>
*Exemplos:* `"Olá, Mundo!"`, `'Python 3'`, `"123"`<br>
🔹 **Booleano (`bool`):** Representa tipos de dados que podem ser apenas *True* ou *False*.<br>
*Exemplos:* `True`, `False`

```python
# Descobrindo o tipo de dado com a função type()

print(type(42))        # Saída: <class 'int'>
print(type(4.2))       # Saída: <class 'float'>
print(type("42"))      # Saída: <class 'str'>
print(type(True))      # Saída: <class 'bool'>
```
--- 

###  ⚠️ **Em Python, as variáveis são divididas em: variáveis simples e compostas. A diferença entre elas está na quantidade e forma como os dados são armazenados e organizados.** <br>

➔ As variáveis **simples** são aquelas que armazenam um único valor por vez. Elas representam as unidades básicas de dados com as quais um programa trabalha. Os tipos de dados mais comuns associados a variáveis simples são:

🔹 **Inteiros (`int`)**;<br>
🔹 **Flutuantes (`float`)**;<br>
🔹 **Strings (`str`)**;<br>
🔹 **Booleanos (`bool`)**.


➔ As variáveis **compostas**, frequentemente chamadas de **estruturas de dados ou coleções**, permitem armazenar conjuntos de informações ou múltiplos valores sob um único nome. *É como coração de mãe: sempre cabe mais um e, com a estrutura certa, fica tudo organizado!*. Os principais exemplos em Python são:

🔹 **Listas (`list`):** Coleções ordenadas, mutáveis e que aceitam valores duplicados;<br>
🔹 **Tuplas (`tuple`):** Coleções ordenadas e **imutáveis** (perfeitas para dados que não devem mudar);<br>
🔹 **Dicionários (`dict`):** Coleções baseadas em chaves e valores (como uma agenda de contatos: `Nome: Telefone`);<br>
🔹 **Conjuntos (`set`):** Coleções não ordenadas e que **não aceitam elementos repetidos**.

<br>


## 🕵🏻‍♀️ Uma Curiosidade
Você sabia que a **String (str)** é uma espécie de "agente duplo"?

Embora ela seja classificada como um tipo primitivo/simples (porque armazena um único bloco de texto), o Python trata a string internamente como uma coleção de caracteres. É por isso que você consegue fazer coisas como acessar apenas a primeira letra de uma palavra usando colchetes, igualzinho a uma lista!

```python
palavra = "Python"
print(palavra[0])  # Saída: P
```

[↑ Voltar ao topo](#topo)

## Operadores

➔ **Operadores aritméticos:** <br>
São utilizados para criar expressões matemáticas comuns:<br>
🔹 **Adição: `+`**;<br>
🔹 **Subtração: `-`**;<br>
🔹 **Multiplicação: `*`**; <br>
🔹 **Divisão: `/`**;<br>
🔹 **Divisão inteira: `//`**;<br>
🔹 **Módulos (resto da divisão): `%`**;<br>
🔹 **Potência: `**`**;<br>
🔹 **Raíz: `(n ** (1/x))`**;

<br>

➔ **Operadores de comparação:** <br>
São usados para comparar dois valores:<br>
🔹 **Igual a: `==`**;<br>
🔹 **Diferente de: `!=`**;<br>
🔹 **Maior que: `>`**;<br>
🔹 **Maior ou igual a: `>=`**;<br>
🔹 **Menor que: `<`**; <br>
🔹 **Menor ou igual que: `<=`**;<br>

<br>

➔ **Operadores de atribuição:** <br>
São utilizados no momento de atribuição de valores à variáveis e controlam como a atribuição será realizada. <br>
🔹 **`=` ⟶  x = 1**; <br>
🔹 **`+=` ⟶ x = x + 1**; <br>
🔹 **`-=` ⟶ x = x - 1**; <br>
🔹 **`*=` ⟶ x = x * 1**; <br>
🔹 **`/=` ⟶ x = x / 1**; <br>
🔹 **`%=` ⟶ x = x % 1**; <br>

➔ **Operadores lógicos:** <br>
Possibilitam contruir os testes lógicos. <br>
🔹 **`and`** ⟶ Retorna `True` se **ambas** as afirmações forem **verdadeiras.** <br>
🔹 **`or`** ⟶ Retorna `True` se **uma** das afirmações for verdadeira. <br>
🔹 **`not`** ⟶ Retorna `False` se o **resultado** for **verdadeiro**. <br>

➔ **Operadores de identidade:** <br>
São utilizados para comparar ***objetos***: <br>
🔹 **`is`** ⟶ Retorna `True`se **ambas** as variáveis **são** o mesmo objeto. <br>
🔹 **`is not`** ⟶ Retorna `True` se **ambas** as variáveis **não** forem o mesmo objeto. <br>

➔ **Operadores de associação:** <br>
Verificam se determinado ***objeto*** está **associado** ou **pertence** a determinada estrutura de dados. <br> 
🔹 **`in`** ⟶ Retorna `True` caso o valor **seja** encontrado na sequência. <br>
🔹 **`not in`** ⟶ Retorna `True`caso o valor **não** seja encontrado na sequência.


[↑ Voltar ao topo](#topo)

## Estrutura condicional

➔ São estruturas que permitem que um programa tome *decisões* com base em *condições específicas*. <br>
➔ São usadas para controlar o **fluxo** de execução de um programa, permitindo que diferentes ações sejam tomadas dependendo de certas **condições**. <br>

➔ **Estrutura básica:**<br>
🔹 **`if`:** Bloco de código se a condição for **verdadeira**. <br>
🔹 **`else`:** Bloco de código se **nenhuma** das condições anteriores for verdadeira.<br>
Exemplo:
```Python
idade = 18
if idade < 18:
    print('Você é menor de idade.')
else:
    print('Você é maior de idade.')
```
[↑ Voltar ao topo](#topo)