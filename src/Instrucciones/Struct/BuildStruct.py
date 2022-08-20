from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Instrucciones.Struct.Struct import Struct


class BuildStruct(Instruccion):

    def __init__(self, fila, columna, identificador, listadoParametros=None):
        self.fila = fila 
        self.columna = columna
        self.identificador = identificador
        self.listadoParametros = listadoParametros



    def ejecutar(self,entorno):

        
        # ========================================
        # busqueda y traer elementos del struct
        # ========================================
        struct = entorno.getStruct(self.identificador)
        if struct is not None:
            listaElementos = struct.elementos
        elif struct is None:
            return f' Struct --> {self.identificador} no encontrado '





        

        # ==============================================
        # limintacion de cantidad de elementos del struct
        # =============================================== 
        if listaElementos is not None and len(listaElementos) == len(self.listadoParametros):
            

            contadorElemento = 0
            # listadoElementos la estructura base
            for elemento in listaElementos:


                # ejecucion elemento a elmento del listado recibido
                # elementos o parametros recibidos cuando se quiere contruir un struct
                elementoStruct = self.listadoParametros[contadorElemento].ejecutar(entorno)


                # comparacion de tipo de los elementos a asignar
                if elemento.identificador == elementoStruct.identificador:
                    
                    # se econtro el mismo identificador
                    # ejecuto para sacar el valor que se tiene que agregar al struct
                    primate = elementoStruct.primate.ejecutar(entorno)

                    # comparacion de tipos para poder ser asignado
                    if elemento.tipo == primate.tipo:
                        # primate = elementoStruct.primate.ejecutar(entorno)
                        # este es el que trae el valor a asignar
                        elemento.valor = primate.valor                        


                else:
                    return f'Struct {self.identificador} parametro {elementoStruct.identificador} no econtrado'

                contadorElemento += 1


            # print('DESPUES DEL EJECUTAR EL STRUCT')
            # print(listaElementos[0].identificador)
            # print(listaElementos[0].tipo)
            # print(listaElementos[0].valor)

            return Struct(
                self.fila, 
                self.columna, 
                self.identificador,
                listaElementos
                )


        #  eeror cantidad de tipos no coinciden
        elif listaElementos is not None and len(listaElementos) != len(self.listadoParametros):
            return f'Struct --> {self.identificador} error de parametros '


