from src.Interfaces.Instruccion import Instruccion


# clase para manejar la instruccion println 
class Imprimir(Instruccion):

    def __init__(self, contenido):
        self.contenido = contenido

    # metodo para ejecutar el imprimir
    def ejecutar(self):

        # result = self.contenido.ejecutar().ejecutar()
        # primitivo
        


        result = self.contenido.ejecutar()

        print(f'tipo entrada en instruccion imprimir --> --> {result}')

        return result.valor