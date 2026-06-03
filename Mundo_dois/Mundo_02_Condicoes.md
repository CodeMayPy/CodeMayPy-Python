<a name="topo"></a>

# Mundo 2 - Condicões em Python

## Sumário de Explorações
<br> 

1. [Revisão](#revisao)
2. [Operadores](#operadores)
3. [Condições aninhadas](#condicoes-aninhadas)
4.

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