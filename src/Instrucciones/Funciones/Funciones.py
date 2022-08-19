from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment


class Funciones(Instruccion):


    def __init__(self, fila, columna, nombreFuncion, listaParamentros, listaInstrucciones, tipoFuncion):
        self.fila = fila
        self.columna = columna
        self.nombreFuncion = nombreFuncion
        self.listaParametros = listaParamentros
        self.listaInstrucciones = listaInstrucciones
        self.tipoFuncion = tipoFuncion
        self.retornoFuncion = ''
        self.expReturn = None


    def ejecutar(self,entorno):
        entorno.addFuncion(self.nombreFuncion,self)
        return None




