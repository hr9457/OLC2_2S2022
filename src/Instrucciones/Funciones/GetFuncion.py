from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.environment.Simbolo import Simbolo



class GetFuncion(Instruccion):

    def __init__(self, fila, columna, listadoParametros=None, identificador=None):
        self.fila = fila
        self.columna = columna
        self.listadoParametros = listadoParametros
        self.identificador = identificador
        self.retornoFuncion = ''


    def ejecutar(self, entorno):


        # crear un nuevo entorno para la funcion
        numeroEntrono = entorno.numero + 1
        envFn = Environment(self.identificador, numeroEntrono, entorno)


        # --------------------------------------------------------
        # llamado a la funcion con toda su estructura y atributos
        funcion = entorno.getFuncion(self.identificador)
        parametrosFuncion = funcion.listaParametros
        listaInstrucciones = funcion.listaInstrucciones
        # --------------------------------------------------------




        # agregacion de variables que estan en los parametros con sus valores
        if parametrosFuncion is not None and len(parametrosFuncion) == len(self.listadoParametros):

            contadorParametros = 0
            for parametro in parametrosFuncion:

                # revision de los tipo para los parametros
                if parametro.tipo == self.listadoParametros[contadorParametros].tipo:
                    envFn.addVariable(parametro.identificador,Simbolo(
                        parametro.fila, 
                        parametro.columna, 
                        parametro.identificador, 
                        parametro.tipo, 
                        self.listadoParametros[contadorParametros].valor, 
                        parametro.mutabilidad))
                    contadorParametros += 1

                else:
                   return f'FN {self.identificador} error tipo parametros ' 

        else:
            return f'FN {self.identificador} error parametros '

      


        # ejecucion de las instrucciones de la funcion
        if listaInstrucciones is not None:

            for instruccion in listaInstrucciones:

                result = instruccion.ejecutar(envFn)

                if result is not None:
                    self.retornoFuncion += result


            # print(self.retornoFuncion)
            return self.retornoFuncion



        elif listaInstrucciones is None:
            return ''


        else:
            return f'FN {self.identificador} error instrucciones '





