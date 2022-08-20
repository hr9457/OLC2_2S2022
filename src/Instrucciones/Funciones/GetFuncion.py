from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.environment.Simbolo import Simbolo
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion



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
        if funcion is not None:
            parametrosFuncion = funcion.listaParametros
            listaInstrucciones = funcion.listaInstrucciones
        else:
            return f'Fn --> {self.identificador} no encontrada'
        # --------------------------------------------------------




        # agregacion de variables que estan en los parametros con sus valores
        if parametrosFuncion is not None and len(parametrosFuncion) == len(self.listadoParametros):

            contadorParametros = 0
            for parametro in parametrosFuncion:

                # ejecutar el parametro antes de comparar
                parametroFuncion = self.listadoParametros[contadorParametros].ejecutar(entorno)

                # revision si es una variable para ser buscada
                if parametroFuncion.tipo == TipoExpresion.ID:
                    parametroFuncion = envFn.getVariable(parametroFuncion.valor)

                # revision de los tipo para los parametros
                if parametro.tipo == parametroFuncion.tipo:
                    envFn.addVariable(parametro.identificador,Simbolo(
                        parametro.fila, 
                        parametro.columna, 
                        parametro.identificador, 
                        parametro.tipo, 
                        parametroFuncion.valor,
                        parametro.mutabilidad))
                    contadorParametros += 1

                else:
                   return f'FN -> {self.identificador}() error tipo parametros ' 

        elif parametrosFuncion is not None and len(parametrosFuncion) != len(self.listadoParametros):
            return f'FN -> {self.identificador}() error parametros '

      






        # ejecucion de las instrucciones de la funcion
        if listaInstrucciones is not None:

            for instruccion in listaInstrucciones:

                result = instruccion.ejecutar(envFn)


                # manejo para return en las funciones
                if isinstance(result, Primitivo) and result.tipo == TipoExpresion.RETURN:

                    
                    result = result.valor.ejecutar(envFn)
                    print('RETURN DENTTRO DE LA FUNCION')
                    print(result.valor)
                    retorno = Primitivo(
                        self.fila,
                        self.columna,
                        result.tipo,
                        result.valor
                    )
                    return retorno


                # concatenacion si las instrucciones no retorna un null
                if result is not None:
                    self.retornoFuncion += result



            # verificacion si la funcion tiene un tipo
            if funcion.tipoFuncion is None:
                return self.retornoFuncion
            else:
                return f'FN -> {self.identificador}() error tipo de retorno'



        elif listaInstrucciones is None:
            return ''




        else:
            return f'FN -> {self.identificador}() error instrucciones '





