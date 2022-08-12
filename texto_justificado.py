# contador
def contador_caracteres(lista):
    """
    Cuenta el número de caracteres en una lista de strings

    :param lista: lista de cadenas
    :return: El número de caracteres en la lista.
    """
    contador = 0
    for i in lista:
        contador += len(i)

    return contador


# justicador
def justificador(texto, ancho):
    """
    Toma una cadena y un ancho, y devuelve una cadena con las mismas palabras, pero con espacios
    agregados para que cada línea tenga exactamente el ancho de caracteres.

    :param text: el texto a justificar
    :param width: el ancho del párrafo
    """
    palabras = texto.split()
    parrafo_lista = []  # lista de líneas ajustdadas width
    linea = ""
    linea_justificada = ""
    parrafo_justificado = ""

    for palabra in palabras:
        if len(linea) + len(palabra) + 1 > ancho:
            parrafo_lista.append(linea)
            linea = palabra + " "
        else:
            linea += palabra + " "
    parrafo_lista.append(linea)

    for linea in parrafo_lista:

        lista_linea = linea.split()
        contador = contador_caracteres(lista_linea)

        if len(lista_linea) == 1:
            for i in range(len(lista_linea[:-1])):
                lista_linea[i] = lista_linea[i]

        elif linea != parrafo_lista[-1]:
            while contador < ancho:

                for i in range(len(lista_linea[:-1])):

                    lista_linea[i] = lista_linea[i] + " "
                    contador += 1
                    if contador == ancho:
                        break
        else:
            for i in range(
                len(lista_linea[:-1])
            ):  # Ultima linea no se ajusta ni formatea.

                lista_linea[i] = lista_linea[i] + " "
        linea_justificada = "".join(lista_linea)
        parrafo_justificado += linea_justificada + "\n"

    print(parrafo_justificado)


if __name__ == "__main__":
    parrafo = input("Escribe un parrafo: ")
    ancho = int(input("Escribe el ancho del parrafo deseado: "))
    # parrafo = "La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera."
    # ancho = 40

    justificador(
        parrafo,
        ancho,
    )
