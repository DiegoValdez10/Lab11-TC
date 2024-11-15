
lista_inicial = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']


elementos_a_eliminar = ['amarillo', 'café', 'blanco']


lista_filtrada = list(filter(lambda x: x not in elementos_a_eliminar, lista_inicial))


print("Lista inicial:")
print(lista_inicial)

print("\nElementos a eliminar:")
print(elementos_a_eliminar)

print("\nLista resultante:")
print(lista_filtrada)
