numero = contador = soma = 0
numero = int(input("Digite um número inteiro [999 para parar]: "))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input("Digite um número inteiro [999 para parar]:"))
print(f"Você digitou {contador} números e a soma entre eles é {soma} ") 