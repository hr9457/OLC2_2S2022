from src.Interfaces.Expresion import Expresion
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion

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
            print(f'ELSE --> {result}')

            if isinstance(result, Primitivo) and result.tipo == TipoExpresion.BREAK:
                retorno = Primitivo(None, None, TipoExpresion.BREAK, resultadoElse + str(result.valor))
                # print(f'RETORNO IF --> {retorno.valor}')
                return retorno
            elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                break 
            
            if result != None:
                resultadoElse += result + '\n'


        return resultadoElse







