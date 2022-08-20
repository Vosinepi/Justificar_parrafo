# contador


# Una clase que toma una cadena y la justifica a un cierto ancho.
class Justificador:
    """
    Pasando un parrafo y un ancho de parrafo se justifica modificando el espacio entre
    palabras.

    Args:
        texto (str): texto a justificar
        ancho (int): ancho del parrafo
    Returns:
        str: texto justificado

    """

    def __init__(self, texto, ancho=15):
        self.texto = texto
        self.ancho = ancho

    def ancho_parrafo(self, numero):
        self.ancho = numero

    def justificador(self):

        palabras = self.texto.split()
        parrafo_lista = []  # lista de líneas ajustdadas width
        linea = ""
        for palabra in palabras:
            if len(linea) + len(palabra) + 1 > self.ancho:
                parrafo_lista.append(linea)
                linea = palabra + " "
            else:
                linea += palabra + " "
        parrafo_lista.append(linea)

        linea_justificada = ""
        parrafo_justificado = ""

        for linea in parrafo_lista:

            lista_linea = linea.split()
            cont_caract_linea = lambda lista: sum(
                map(len, lista)
            )  # contador de caracteres por linea
            contador = cont_caract_linea(lista_linea)

            if len(lista_linea) == 1:
                for i in range(len(lista_linea[:-1])):
                    lista_linea[i] = lista_linea[i]

            elif linea != parrafo_lista[-1]:
                while contador < self.ancho:

                    for i in range(len(lista_linea[:-1])):

                        lista_linea[i] = lista_linea[i] + " "
                        contador += 1
                        if contador == self.ancho:
                            break
            else:
                for i in range(
                    len(lista_linea[:-1])
                ):  # Ultima linea no se ajusta ni formatea.

                    lista_linea[i] = lista_linea[i] + " "
            linea_justificada = "".join(lista_linea)
            parrafo_justificado += linea_justificada + "\n"

        return parrafo_justificado


parrafo = Justificador(
    "La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera."
)
parrafo.ancho_parrafo(30)

print(parrafo.justificador())


# if __name__ == "__main__":
#     Justificador()
