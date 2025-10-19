lista_de_numeros = [5, 2, 9, 1, 5, 6]   
lista_de_numeros_2 = [3, 4, 2, 8, 7, 1]
lista_de_numeros_3 = [10, 20, 15, 25, 5]

def ordenar_lista_de_numeros(numeros: list) -> list:
    """
    Ordena uma lista de números em ordem crescente.

    Args:
        lista (list): A lista de números a ser ordenada.

    Returns:
        list: A lista de números ordenada.
    """
    nova_lista_de_numeros = numeros.copy()
    nova_lista_de_numeros.sort()
    return nova_lista_de_numeros

nova_lista = ordenar_lista_de_numeros(lista_de_numeros)
nova_lista_2 = ordenar_lista_de_numeros(lista_de_numeros_2)
nova_lista_3 = ordenar_lista_de_numeros(lista_de_numeros_3)
print(nova_lista)
print(nova_lista_2)
print(nova_lista_3)