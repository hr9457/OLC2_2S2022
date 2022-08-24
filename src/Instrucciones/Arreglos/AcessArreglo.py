
from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion


# clase expresion para menejar los acceso a los arreglos
class AcessArreglo(Expresion):


    def __init__(self, fila, columna, var, index):
        self.fila = fila
        self.columna = columna
        self.var = var
        self.index = index


    def ejecutar(self, entorno):

        print('******* ACCESO A ARREGLO EJECUTADO ******')

        variable = self.var.ejecutar(entorno)
        indice  = self.index.ejecutar(entorno)


        if variable.tipo == TipoExpresion.ID and variable is not None:
            print('variable donde puede estar guardado el arreglo')

            # busqueda de la variable
            arreglo = entorno.getVariable(variable.valor)

            if arreglo is not None:

                # comprobacion del indice se un i64 para poder acceder el arreglo
                if indice.tipo == TipoExpresion.INTEGER:
                    valor = arreglo.listadoExpresiones[indice.valor]
                    return valor

                else:
                    return f'indice {indice.valor} no es tipo i64'



            elif arreglo is None:

                return f'var {variable.valor} no existe'


        else:
            return f'var {variable.valor} no es una variable'
