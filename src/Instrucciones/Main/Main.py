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
            # print('paro')

            if retorno != None and isinstance(retorno, str):
                resultInstrucciones += retorno


        return resultInstrucciones



    def traducir(self, entorno, traductor3d):

        for instruccion in self.instrucciones:
            instruccion.traducir(entorno, traductor3d)

        return None