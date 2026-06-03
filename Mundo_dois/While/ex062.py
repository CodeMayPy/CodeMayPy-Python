print('Gerador de progressão aritmética:')
print("-=-" * 20)
primeiro_termo = int(input("Digite o primeiro termo:"))
razao = int(input("Digite a razão da progressão aritmética: "))
termo = primeiro_termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = mais + total
    while contador <= total:
        print(f"{termo}", end=' ')
        termo += razao
        contador += 1
    print("Pausa")
    mais = int(input("Quantos termos a mais você quer mostrar? "))