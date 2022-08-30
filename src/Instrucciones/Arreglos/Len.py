from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoMutable import TipoMutable
from src.environment.Simbolo import Simbolo

class Len(Expresion):


    def __init__(self, variable):
        self.variable = variable


    def ejecutar(self, entorno):


        print('************* LEN de arreglos ******************')

        # primer filtro con la variable sea tipo arreglo
        if self.variable is not None and self.variable.tipo == TipoExpresion.ID:

            varrArreglo = entorno.getVariable(self.variable.valor)


            # que la variable sea tipo arreglo
            if varrArreglo.tipo == TipoExpresion.ARREGLO:

                tamanioArreglo = len(varrArreglo.listadoExpresiones)

                return Simbolo(
                    0,
                    0,
                    None,
                    TipoExpresion.INTEGER,
                    tamanioArreglo,
                    TipoMutable.MUTABLE
                )



        return f'eror en la funcion len del arreglo'