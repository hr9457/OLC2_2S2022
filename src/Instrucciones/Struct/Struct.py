from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Interfaces.TipoExpresion import TipoExpresion


class Struct(Instruccion):


    def __init__(self, fila, columna, identificador, elementos):
        self.fila = fila
        self.columna = columna  
        self.identificador = identificador
        self.elementos = elementos
        self.tipo = TipoExpresion.STRUCT



    def ejecutar(self, entorno):
        entorno.addStruct(self.identificador, self)
        return None