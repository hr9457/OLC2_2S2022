from src.Interfaces.Instruccion import Instruccion


# clase para manejar la instruccion println 
class Imprimir(Instruccion):

    def __init__(self, contenido):
        self.contenido = contenido

    # metodo para ejecutar el imprimir
    def ejecutar(self):
        # result = self.contenido.ejecutar().ejecutar()
        result = self.contenido.ejecutar()
        return result