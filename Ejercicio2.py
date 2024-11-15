
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


n = int(input("Indica la potencia n (un número entero positivo): "))


if n <= 0:
    print("La potencia n debe ser un entero positivo.")
else:
    potencias = list(map(lambda x: x**n, numeros))

    print(f"Lista original: {numeros}")
    print(f"Potencias n-ésimas (n={n}): {potencias}")
