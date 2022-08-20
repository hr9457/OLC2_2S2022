from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Error.Error import Error
from src.Expresiones.Primitivo import Primitivo
from src.Instrucciones.Funciones import GetFuncion


# clase para manejar la instruccion println 
class Imprimir(Instruccion):

    def __init__(self, contenido, lista=None):
        self.contenido = contenido
        self.lista = lista

    # metodo para ejecutar el imprimir
    def ejecutar(self, entorno):


        # primitivo
        variables = '{}'
        countNodoDerecho = 0 

        


        # ejecucion de los nodos que trae
        result = self.contenido.ejecutar(entorno)

        


        # nodo derecho
        if self.lista is not None:
            countNodoDerecho = len(self.lista)
            print(f'elementos en lista {countNodoDerecho}')


        if isinstance(result, Error):
            # print('es una clase error')
            return result.ejecutar()


        else:


            # contar cuantos elementos trae el nodo derecho
            if countNodoDerecho >= 1 and countNodoDerecho == result.valor.count(variables):

                print('cantidad de {} == cantidad de elementos en lista')

            
                tempLista = []
                for instruccion in self.lista:

                    resultadoInstruccion = instruccion.ejecutar(entorno)

                    print(resultadoInstruccion.tipo)
                    print(resultadoInstruccion.valor)

                    # tipo para impresiones
                    if resultadoInstruccion.tipo == TipoExpresion.ID:
                        result_evn = entorno.getVariable(resultadoInstruccion.valor)
                        tempLista.append(result_evn.valor)

                    elif resultadoInstruccion.tipo == TipoExpresion.STRUCT:
                        print('se va imprimir un valor de un struct')
                        return None

                    else:
                        tempLista.append(resultadoInstruccion.valor)


                print(tempLista)
                result.valor =  result.valor.format(*tempLista)
                return str(result.valor+'\n')
            

            else:
                if result.tipo == TipoExpresion.ID:
                    result_env = entorno.getVariable(result.valor)
                    return str(result_env.valor)

                else:
                    print(f'IMPRIMIR --> {result.tipo}')
                    print(f'IMPRIMIR --> {result.valor}')
                    return str(result.valor+'\n')