from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoNativas import TipoNativas
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion
import math


class Nativas(Instruccion):

    def __init__(self, fila, columna, nodo, tipo):
        self.fila = fila
        self.columna = columna
        self.nodo = nodo
        self.tipo = tipo
        


    def ejecutar(self, entorno):
        
        # retonro de un primitivo
        result = self.nodo.ejecutar(entorno)


        # comprobacion si es una variable
        if result.tipo == TipoExpresion.ID:
            result = entorno.getVariable(result.valor)
            



        # verficacionde los tipos 
        if self.tipo == TipoNativas.TOSTRING:
            return Primitivo(
                self.fila,
                self.columna,
                TipoExpresion.STRING,
                result.valor
            )

        elif self.tipo == TipoNativas.ABS:

            if result.tipo == TipoExpresion.INTEGER or result.tipo == TipoExpresion.FLOAT:
                return Primitivo(
                    self.fila,
                    self.columna,
                    result.tipo,
                    abs(result.valor)
                )
            else:
                print('NATIVAS --> eror conversion abs')
                return None

        elif self.tipo == TipoNativas.SQRT:

            if result.tipo == TipoExpresion.FLOAT:
                print(math.sqrt(float(result.valor)))
                return Primitivo(
                    self.fila,
                    self.columna,
                    result.tipo,
                    math.sqrt(float(result.valor))
                )
            
            else:
                print('NATIVAS --> eror conversion sqrt')
                return None

        
        elif self.tipo == TipoNativas.CLONE:

            return Primitivo(
                self.fila,
                self.columna,
                result.tipo,
                result.valor
            )
