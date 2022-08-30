
from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Expresiones.Primitivo import Primitivo


# clase expresion para menejar los acceso a los arreglos
class AcessArreglo(Expresion):


    def __init__(self, fila, columna, tablaErrores,var, index):
        self.fila = fila
        self.columna = columna
        self.tablaErrores = tablaErrores
        self.var = var
        self.index = index
        self.tipo = TipoExpresion.ARREGLO


    def ejecutar(self, entorno):

        # print('******* ACCESO A ARREGLO EJECUTADO ******')

        variable = self.var.ejecutar(entorno)
        indice = self.index.ejecutar(entorno)

        if indice.tipo == TipoExpresion.ID:
            varIndice = entorno.getVariable(indice.valor)
            indice = varIndice


        if variable.tipo == TipoExpresion.ID and variable is not None:
            # print('variable donde puede estar guardado el arreglo')

            # busqueda de la variable

            arreglo = entorno.getVariable(variable.valor)

            if arreglo is not None:

                # comprobacion del indice se un i64 para poder acceder el arreglo
                if indice.tipo == TipoExpresion.INTEGER:


                    tamanioArreglo = len(arreglo.listadoExpresiones) - 1

                    if indice.valor <= tamanioArreglo:

                        valor = arreglo.listadoExpresiones[indice.valor]


                        if valor.tipo == TipoExpresion.ARREGLO:
                            pri = Primitivo(None,None, TipoExpresion.ARREGLO, valor.listadoExpresiones)
                            return pri

                        return valor



                    
                    else:
                        # para reportes
                        self.tablaErrores.append([f'index excede el tamanio del arreglo',entorno.nombre,self.fila,self.columna])
                        # --------------------------------

                        return f'index excede el tamanio del arreglo'



                else:

                    # para reportes
                    self.tablaErrores.append([f'indice {indice.valor} no es tipo i64',entorno.nombre,self.fila,self.columna])
                    # --------------------------------

                    return f'indice {indice.valor} no es tipo i64'



            elif arreglo is None:

                # para reportes
                self.tablaErrores.append([f'var {variable.valor} no existe',entorno.nombre,self.fila,self.columna])
                # --------------------------------

                return f'var {variable.valor} no existe'
                


        elif variable.tipo == TipoExpresion.ARREGLO and variable is not None:


                # revision si el indice que recibe es numero entero para acceder al arreglo
                if indice.tipo == TipoExpresion.INTEGER:

                    # verifico que no se salga del rango del arreglo
                    tamanioArreglo = len(variable.valor) - 1

                    if indice.valor <= tamanioArreglo:

                        valor = variable.valor[indice.valor]

                        if valor.tipo == TipoExpresion.ARREGLO:
                            pri = Primitivo(None,None, TipoExpresion.ARREGLO, valor.listadoExpresiones)
                            return pri

                        return valor






        else:
            # para reportes
            self.tablaErrores.append([f'var {variable.valor} no es una variable',entorno.nombre,self.fila,self.columna])
            # --------------------------------
            return f'var {variable.valor} no es una variable'
