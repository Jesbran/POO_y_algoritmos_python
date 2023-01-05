import random

def busqueda_lineal(lista, objetivo):
    match = False
    for element in lista:
        if element == objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    tamano_lista = int(input("De que tamano sera la lista?"))
    objetivo = int(input("Cual es el numero que estas buscando?"))
    lista = {random.randint(0,100) for i in range(tamano_lista)}
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') #operadores ternarios