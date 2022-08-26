from src.Interfaces.Instruccion import Instruccion


class FuncionMain(Instruccion):

    def __init__(self, fila, columna, instrucciones):
        self.fila = fila
        self.columna = columna
        self.instrucciones = instrucciones



    def ejecutar(self, entorno):

        resultInstrucciones =''

        # ejecucion de todas las intrucciones del metodo main
        for instruccion in self.instrucciones:
            retorno = instruccion.ejecutar(entorno)

            if retorno != None:
                resultInstrucciones += retorno


        return resultInstrucciones
