valores = []
pares = []
impares = []

for _ in range(10):
    valor = int(input("Digite um valor: "))
    valores.append(valor)

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

impares_tuple = tuple(impares)

quantidade_pares = len(pares)
quantidade_impares = len(impares)
soma_pares = sum(pares)
soma_impares = sum(impares)

print("Números pares:", pares)
print("Números ímpares:", impares_tuple)
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)
print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)