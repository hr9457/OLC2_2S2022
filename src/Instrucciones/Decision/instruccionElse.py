from src.Interfaces.Expresion import Expresion


class InstruccionElse(Expresion):


    # constructor
    def __init__(self, fila, columna, instrucciones=None):
        self.fila = fila
        self.columna = columna
        self.instrucciones = instrucciones
        


    # ejecucion del else 
    def ejecutar(self, entorno):


        resultadoElse = ''

        for instruccion in self.instrucciones:
            result = instruccion.ejecutar(entorno)
            if result != None:
                resultadoElse += result


        return resultadoElse







