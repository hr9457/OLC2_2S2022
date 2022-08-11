from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Error.Error import Error


# clase para manejar la instruccion println 
class Imprimir(Instruccion):

    def __init__(self, contenido, lista=None):
        self.contenido = contenido
        self.lista = lista

    # metodo para ejecutar el imprimir
    def ejecutar(self, entorno):

        # result = self.contenido.ejecutar().ejecutar()
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

               
                # if nodoDerecho.tipo == TipoExpresion.ID:
                # result_env = entorno.getVariable(nodoDerecho.valor)
                # return str(result.valor.replace(variables, str(result_env.valor)))
                retornoPrint = ''

                for instruccion in self.lista:
                    resultLista = instruccion.ejecutar(entorno)
                    result_env = entorno.getVariable(resultLista.valor)
                    posicion = result.valor.find(variables)
                    result.valor = result.valor.replace(variables,str(result_env.valor),1)
                
                return str(result.valor)
            

            else:
                print(f'IMPRIMIR --> {result.tipo}')
                print(f'IMPRIMIR --> {result.valor}')
                return str(result.valor)