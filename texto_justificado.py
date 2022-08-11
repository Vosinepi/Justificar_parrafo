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
def justificador(text, width):
    """
    Toma una cadena y un ancho, y devuelve una cadena con las mismas palabras, pero con espacios
    agregados para que cada línea tenga exactamente el ancho de caracteres.

    :param text: el texto a justificar
    :param width: el ancho del párrafo
    """
    words = text.split()
    lines = []  # lista de líneas ajustdadas width
    line = ""
    for word in words:
        if len(line) + len(word) + 1 > width:
            lines.append(line)
            line = word + " "
        else:
            line += word + " "
    lines.append(line)

    linea = ""
    parrafo_justificado = ""
    contador = 0

    for line in lines:

        contador = 0
        lista_linea = line.split()
        contador = contador_caracteres(lista_linea)

        if len(lista_linea) == 1:
            for i in range(len(lista_linea[:-1])):
                lista_linea[i] = lista_linea[i]

        elif line != lines[-1]:
            while contador < width:

                for i in range(len(lista_linea[:-1])):

                    lista_linea[i] = lista_linea[i] + " "
                    contador += 1
                    if contador == width:
                        break
        else:
            for i in range(
                len(lista_linea[:-1])
            ):  # Ultima linea no se ajusta ni formatea.

                lista_linea[i] = lista_linea[i] + " "
        linea = "".join(lista_linea)
        parrafo_justificado += linea + "\n"

    print(parrafo_justificado)


if __name__ == "__main__":
    parrafo = input("Escribe un parrafo: ")
    ancho = int(input("Escribe el ancho del parrafo: "))

    justificador(
        parrafo,
        ancho,
    )
