
from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoMutable import TipoMutable


class ModificarValorArreglo(Instruccion):

    def __init__(self, fila, columna, tablaErrores, variable, exp, newValue):
        self.fila = fila
        self.columna = columna
        self.tablaErrores = tablaErrores
        self.variable = variable
        self.exp = exp
        self.newValue = newValue


    def ejecutar(self, entorno):

        print('************ MODIFICANDO VALOR DE UN ARREGLO **************')


        # primer filtro saber si la variable tiene existencia
        # solo me viene el identificador de la variable

        var = entorno.getVariable(self.variable)



        # filtro para entender que la variable tiene existencia en el entorno y que sea tipo arreglo
        if var.tipo == TipoExpresion.ARREGLO and var is not None:
            
            
            if var.mutabilidad == TipoMutable.MUTABLE:

                tamanioArreglo = len(var.listadoExpresiones) - 1


                # revision si el index si es una variable
                if self.exp[0].tipo == TipoExpresion.ID:
                    varIndex = entorno.getVariable(self.exp[0].ejecutar(entorno).valor)
                    index = varIndex.valor
                else:
                    index = self.exp[0].ejecutar(entorno).valor





                valorPosicion = var.listadoExpresiones[index].ejecutar(entorno)
                # valorPosicion.valor

                nuevoValor = self.newValue.ejecutar(entorno)


                # si el nuevo valores es una variable hay que buscarla
                if nuevoValor.tipo == TipoExpresion.ID:
                    nuevoValor = entorno.getVariable(nuevoValor.valor)


                var.listadoExpresiones[index].valor = nuevoValor.valor


                entorno.addVariable(self.variable,var)


                print('paro')





            else:
                # para reportes
                self.tablaErrores.append([f'variable {self.variable} no es mutable', entorno.nombre, self.fila, self.columna])
                # --------------------------------
                return f'variable {self.variable} no es mutable'






        else:
            # para reportes
            self.tablaErrores.append([f'variable {self.variable} no es de tipo arreglo', entorno.nombre, self.fila, self.columna])
            # --------------------------------
            return f'variable {self.variable} no es de tipo arreglo'


        return None