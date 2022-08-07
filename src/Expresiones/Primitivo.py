# importacion de para Expresiones
from src.Interfaces.Expresion import Expresion

# clse para manejar numero primitivos
class Primitivo(Expresion):

    def __init__(self, fila, columna, tipo, valor):
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.valor = valor


    # metodo abstracto
    def ejecutar(self, entorno):
        return Primitivo(
            self.fila,
            self.columna,
            self.tipo,
            self.valor
            )

    

    # retorno de tipo
    def getTipo(self):
        return self.tipo