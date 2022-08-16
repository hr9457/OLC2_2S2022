from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment


class Funciones(Instruccion):


    def __init__(self, fila, columna, nombreFuncion, listaInstrucciones):
        self.fila = fila
        self.columna = columna
        self.nombreFuncion = nombreFuncion
        self.listaInstrucciones = listaInstrucciones
        self.retornoFuncion = ''


    def ejecutar(self,entorno):


        # crear un nuevo entorno para la funcion
        numeroEntrono = entorno.numero + 1
        envFn = Environment(self.nombreFuncion,numeroEntrono,entorno)


        entorno.addFuncion(self.nombreFuncion,self.listaInstrucciones)


        return None




