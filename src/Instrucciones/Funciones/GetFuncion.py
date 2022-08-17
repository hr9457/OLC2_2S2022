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
        # print(f'LLAMADO --> {self.listadoParametros[0].tipo}')


        # crear un nuevo entorno para la funcion
        numeroEntrono = entorno.numero + 1
        envFn = Environment(self.identificador, numeroEntrono, entorno)


        # --------------------------------------------------------
        # llamado a la funcion con toda su estructura y atributos
        funcion = entorno.getFuncion(self.identificador)
        parametrosFuncion = funcion.listaParametros
        # --------------------------------------------------------



        # agregacion de variables que estan en los parametros con sus valores
        contadorParametros = 0
        for parametro in parametrosFuncion:          

            print(f'TIPO DEL PARAMETRO ES --> {parametro.tipo}')
            envFn.addVariable(parametro.identificador,Simbolo(
                parametro.fila, 
                parametro.columna, 
                parametro.identificador, 
                parametro.tipo, 
                self.listadoParametros[contadorParametros].valor, 
                parametro.mutabilidad))
            contadorParametros += 1


      


        # cantidad de parametros sean los mismo de la funcion
        if len(parametrosFuncion) == len(self.listadoParametros):

            for instruccion in funcion.listaInstrucciones:

                print('INST')
                print(instruccion)
                result = instruccion.ejecutar(envFn)

                if result is not None:
                    self.retornoFuncion += result


            # print(self.retornoFuncion)
            return self.retornoFuncion

        
        else:
            return f'FN {self.identificador} cantidad de parametros '





