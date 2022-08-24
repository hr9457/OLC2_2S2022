from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Simbolo import Simbolo
from src.Error.Error import Error
from src.Instrucciones.Struct.Struct import Struct


class Declaracion(Instruccion):

    # constructor
    def __init__(self, fila, columna, identificador, tipo, valor, mutabilidad):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.tipo = tipo
        self.valor = valor
        self.mutabilidad = mutabilidad


    # metodo ejecutar
    def ejecutar(self, entorno):


        

        # verificacion de tipos
        # con tipo y el tipo del primitivo
        # esta linea altera el struct
        primitivo = self.valor.ejecutar(entorno)


        # variabel
        # TIPO == None  es una variable sin tipo
        if self.tipo == None:

            print(f'DECLARACION: {primitivo.tipo}')
            print(f'DECLARACION: {self.valor}')


            if primitivo.tipo == TipoExpresion.STRUCT:

                value_struct = self.valor.ejecutar(entorno)
                value_struct.mutabilidad = self.mutabilidad
                entorno.addVariable(self.identificador,value_struct)
                return None

            elif primitivo.tipo == TipoExpresion.ARREGLO:

                # aca estantodo el listado de los elementos del arreglo
                print(primitivo.listadoExpresiones)
                entorno.addVariable(self.identificador,primitivo)

                return None


            else:
                entorno.addVariable(self.identificador, 
                                    Simbolo(
                                        primitivo.fila, 
                                        primitivo.columna, 
                                        self.identificador, 
                                        primitivo.tipo, 
                                        primitivo.valor, 
                                        self.mutabilidad) )
                return None

        


        elif self.tipo != None:
            
            if self.tipo == primitivo.tipo:

                
                entorno.addVariable(self.identificador, 
                                    Simbolo(primitivo.fila, 
                                    primitivo.columna, 
                                    self.identificador, 
                                    primitivo.tipo, 
                                    primitivo.valor, 
                                    self.mutabilidad) )
                return None


            elif primitivo.tipo == TipoExpresion.STRUCT:

                searchStruct = entorno.getStruct(self.tipo)

                if searchStruct is not None:

                    value_struct = self.valor.ejecutar(entorno)
                    value_struct.mutabilidad = self.mutabilidad
                    entorno.addVariable(self.identificador,value_struct)
                    return None

                else:

                    return f'DECLARACION: Struct {self.tipo} no existe'


            else: 
                return 'DECLARACION: error tipos no coinciden para declaracion de variables'




        else:
            return 'DECLARACION: error tipos para declaracion de variables'




