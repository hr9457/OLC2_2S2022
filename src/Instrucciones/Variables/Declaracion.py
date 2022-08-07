from src.Interfaces.Instruccion import Instruccion
from src.environment.Simbolo import Simbolo


class Declaracion(Instruccion):

    # constructor
    def __init__(self, fila, columna, identificador, tipo, valor, mutabilidad):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.tipo = tipo
        self.valor = valor
        self.mutabilidad = mutabilidad


    # metodo ejecutar
    def ejecutar(self, entorno):

        # verificacion de tipos
        # con tipo y el tipo del primitivo        
        primitivo = self.valor.ejecutar(entorno)

        if self.tipo == primitivo.tipo:
            entorno.addVariable(self.identificador, Simbolo(primitivo.fila, primitivo.columna, self.identificador, primitivo.tipo, primitivo.valor, self.mutabilidad) )
            # return ''

        else:
            return 'Error de tipos para declaracion de variables'




