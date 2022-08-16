from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment



class GetFuncion(Instruccion):

    def __init__(self, fila, columna, identificador):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.retornoFuncion = ''


    def ejecutar(self, entorno):

        # crear un nuevo entorno para la funcion
        numeroEntrono = entorno.numero + 1
        envFn = Environment(self.identificador, numeroEntrono, entorno)

        lista = entorno.getFuncion(self.identificador)

        for instruccion in lista:

            result = instruccion.ejecutar(envFn)

            if result is not None:
                self.retornoFuncion += result

        # print(self.retornoFuncion)
        return self.retornoFuncion





