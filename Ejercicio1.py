
autos = [
    {'make': 'Ford', 'model': 'Focus', 'year': 2012},
    {'make': 'Tesla', 'model': 'Model S', 'year': 2018},
    {'make': 'Ford', 'model': 'Fiesta', 'year': 2014},
    {'make': 'BMW', 'model': 'X5', 'year': 2016}
]


def ordenar_por_clave(lista, clave):
    try:
        return sorted(lista, key=lambda x: x[clave])
    except KeyError:
        print(f"Error: La clave '{clave}' no existe en los diccionarios.")
        return lista


clave = input("Indica la clave por la que quieres ordenar la lista: Make, Model o Year: ")


resultado = ordenar_por_clave(autos, clave)


print(f"Lista ordenada por '{clave}':")
for item in resultado:
    print(item)
