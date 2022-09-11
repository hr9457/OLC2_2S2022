
from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Expresiones.Primitivo import Primitivo
from src.environment.Simbolo import Simbolo


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


                    
                    posicion_acceso_arreglo = 0
                    print(f'-------------------------------------------------------->{type(arreglo)}')

                    # return self.obtenerValorArreglo(arreglo, indice, posicion_acceso_arreglo, entorno)

                    if isinstance(arreglo,Simbolo):
                        tamanioArreglo = len(arreglo.valor) - 1

                        if indice.valor <= tamanioArreglo:

                            valor = arreglo.valor[indice.valor]

                            if valor.tipo == TipoExpresion.ARREGLO:
                                pri = Primitivo(None, None, TipoExpresion.ARREGLO, valor.listadoExpresiones)
                                return pri

                            return valor


                    elif arreglo.tipo == TipoExpresion.VECTOR:

                        valor = arreglo.lista[indice.valor]
                        if valor.tipo == TipoExpresion.VECTOR:
                            pri = Primitivo(None, None, TipoExpresion.VECTOR, valor.lista)
                            return pri
                        return valor



                    else:
                        tamanioArreglo = len(arreglo.listadoExpresiones) - 1

                        if indice.valor <= tamanioArreglo:

                            valor = arreglo.listadoExpresiones[indice.valor]


                            if valor.tipo == TipoExpresion.ARREGLO:
                                pri = Primitivo(None,None, TipoExpresion.ARREGLO, valor.listadoExpresiones)
                                return pri

                            return valor



                    
                    # else:
                    #     # para reportes
                    #     self.tablaErrores.append([f'index excede el tamanio del arreglo',entorno.nombre,self.fila,self.columna])
                    #     # --------------------------------

                    #     return f'index excede el tamanio del arreglo'



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






    # funcion recursiva cambiar el varlor del arreglo
    def obtenerValorArreglo(self, var, indice, posicion_acceso_arreglo, entorno):

        # ******************************************
        # revision si el index si es una variable
        if self.exp[posicion_acceso_arreglo].tipo == TipoExpresion.ID:
            varIndex = entorno.getVariable(self.exp[posicion_acceso_arreglo].ejecutar(entorno).valor)
            index = varIndex.valor
        else:
            index = self.exp[posicion_acceso_arreglo].ejecutar(entorno).valor

        # *********************************************


        # print(f'------------------------------------------>{type(var)}')
        if isinstance(var,Simbolo):
            var.valor[index].ejecutar(entorno)

            posicion_acceso_arreglo += 1

            if var.valor[index].tipo == TipoExpresion.ARREGLO:
                self.modidificarValorArreglo(var.valor[index], posicion_acceso_arreglo, entorno)

            else:
                return var.valor[index]

        else:
            var.listadoExpresiones[index].ejecutar(entorno)

            posicion_acceso_arreglo += 1

            if var.listadoExpresiones[index].tipo == TipoExpresion.ARREGLO:
                self.modidificarValorArreglo(var.listadoExpresiones[index], posicion_acceso_arreglo, entorno)

            else:
                return var.listadoExpresiones[index]
