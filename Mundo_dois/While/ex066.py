soma = 0
while True:
    numero = int(input("Digite um número inteiro [999 para parar]: "))
    if numero == 999:
        break
    soma += numero
print(f"A soma dos números é {soma}")