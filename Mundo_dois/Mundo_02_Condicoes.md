<a name="topo"></a>

# Mundo 2 - Condicões em Python

## Sumário de Explorações
<br> 

1. [Revisão](#revisao)
2. [Operadores](#operadores)
3. [Condições aninhadas](#condicoes-aninhadas)
4. [Estrutura de repetição](#estrutura-de-repeticao)

<br>

## Revisão:

➔ São estruturas que permitem que um programa tome *decisões* com base em *condições específicas*. <br>
➔ São usadas para controlar o **fluxo** de execução de um programa, permitindo que diferentes ações sejam tomadas dependendo de certas **condições**. <br>

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
<br>


## Condições aninhadas

➔ **Condições em cadeia (Múltiplas vias):** É quando usamos o `if`, `elif` e `else` para testar várias opções em sequência. O programa testa uma por uma; assim que encontra uma verdadeira, executa a tarefa e ignora o resto do bloco.<br>
➔ **Condições Aninhadas:** Em Python, chamamos de "aninhamento" o ato de colocar uma estrutura condicional *dentro* de outra (como uma boneca russa). Para o Python entender que uma estrutura está dentro da outra, usamos os espaços (**indentação**).<br>

    As condições aninhadas fazem parte da execução condicional. Elas são usadas quando o seu programa precisa tomar decisões baseadas em múltiplos critérios, funcionando como uma "pergunta dentro de outra".

➔ **Estrutura básica:**<br>
🔹 **`if`:** Bloco de código se a condição for **verdadeira**. <br>
🔹 **`elif`:** Bloco de código se a outra condição for **verdadeira**.<br>
🔹 **`else`:** Bloco de código se **nenhuma** das condições anteriores for verdadeira.<br>
Exemplo:
```Python
idade = 18
if idade < 18:
    print('Você é menor de idade.')
elif idade == 18:
    print('Você tem 18 anos de idade.')    
else:
    print('Você é maior de idade.')
```
[↑ Voltar ao topo](#topo)

## Estrutura de repetição

➔ Também conhecidas como **iteração** ou **laços (loops)**, as estruturas de repetição são blocos básicos de qualquer linguagem de programação.<br>
➔ São usadaspara executar um bloco de códigos várias vezes, enquanto uma condição for **verdadeira** ou para iterar sobre uma **sequência** de elementos (como listas, tuplas, strings, etc...). <br>
➔ Existem dois tipos principais de estruturas de repetição: o **`for`** e o **`while`**.

🔹**Estrutura for:** <br>
- É utilizado para percorrer elementos de uma sequência (como uma lista, string, ou intervalo) de forma **iterativa**.<br>
- Sintaxe:
```python
for elemento in sequência:
    #bloco a ser executado
```
- O `range()` é usado para **gerar** números em uma sequência. <br>

🔹**Estrutura while:** <br>
- O `while`executa um bloco de código enquanto uma condição for **verdadeira**.<br>
- Sintaxe:
```python
while condição:
    #bloco a ser executado.
```
<br>

➔ **Comandos chaves:** <br>    
- **`break`:** Interrompe a execução do laço. <br>
Exemplo:
```python
for numero in range(10):
    if numero == 5:
        break
    print(numero)
'''Saída:
0
1
2
3
4 '''
```    
<br>

- **`continue`:** Pula para a próxima iteração do laço.
Exemplo:
```python
for numero in range(5):
    if numero == 2:
        continue
    print(numero)
'''Saída:
0
1
3
4'''
```
<br>

➔ Use `for`para percorrer sequências ou intervalos conhecidos.<br>
➔ Use `while` para repetir algo enquanto uma condição for **verdadeira**. <br>
➔ Combine com `break`, `continue` e `else` para controlar melhor o fluxo do laço.<br>

[↑ Voltar ao topo](#topo)