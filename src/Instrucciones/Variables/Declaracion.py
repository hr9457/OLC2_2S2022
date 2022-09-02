from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Simbolo import Simbolo
from src.Error.Error import Error
from src.Instrucciones.Struct.Struct import Struct
from src.Instrucciones.Arreglos.ExpArreglo import ExpArreglo
from src.Instrucciones.Arreglos.TipoArreglo import TipoArreglo


class Declaracion(Instruccion):

    # constructor
    def __init__(self, fila, columna, identificador, tipo, valor, mutabilidad, tablaSimbolos, tablaErrores):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.tipo = tipo
        self.valor = valor
        self.mutabilidad = mutabilidad
        self.tablaSimbolos = tablaSimbolos
        self.tablaErrores = tablaErrores


    # metodo ejecutar
    def ejecutar(self, entorno):


        

        # verificacion de tipos
        # con tipo y el tipo del primitivo
        # esta linea altera el struct
        primitivo = self.valor.ejecutar(entorno)


        # variabel
        # TIPO == None  es una variable sin tipo
        # VARIABLES DONDE NO SE LE ESPECIFICA EL TIPO DE LA VARIABLE
        if self.tipo == None:

            print(f'DECLARACION: {primitivo.tipo}')
            print(f'DECLARACION: {self.valor}')


            if primitivo.tipo == TipoExpresion.STRUCT:

                value_struct = self.valor.ejecutar(entorno)
                value_struct.mutabilidad = self.mutabilidad
                entorno.addVariable(self.identificador,value_struct)

                # para reportes
                self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                # -------------


                return None



            elif primitivo.tipo == TipoExpresion.ARREGLO:

                # aca estantodo el listado de los elementos del arreglo
                # print(primitivo.listadoExpresiones)
                primitivo.mutabilidad = self.mutabilidad
                entorno.addVariable(self.identificador,primitivo)

                # para reportes
                self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                # -------------

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

                # para reportes
                self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                # -------------
                
                return None

        


        elif self.tipo != None:


            # REVISION DE LOS TIPOS DE DATOS PAR ARREGLOS
            if isinstance(self.tipo,TipoArreglo):
                print('TIPO DE DECLARACION ES DE TIPO ARREGLO')
                type = self.tipo.ejecutar(entorno)

                if type.tipo == primitivo.tipo:
                    print('ARREGLO SON DEL MISMO TIPO')

                    primitivo.mutabilidad = self.mutabilidad
                    entorno.addVariable(self.identificador,
                                        Simbolo(
                                         primitivo.fila,
                                         primitivo.columna,
                                         self.identificador,
                                         primitivo.tipo,
                                         primitivo.listadoExpresiones,
                                         self.mutabilidad
                                        ))
                    # antes mandaba el primitivo Arreglo directo

                    # para reportes
                    self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                    # -------------

                    return None
                    


            if primitivo.tipo == TipoExpresion.ARREGLO:
                print('ARREGLO SON DEL MISMO TIPO')

                primitivo.mutabilidad = self.mutabilidad
                entorno.addVariable(self.identificador,
                                    Simbolo(
                                        primitivo.fila,
                                        primitivo.columna,
                                        self.identificador,
                                        primitivo.tipo,
                                        primitivo.listadoExpresiones,
                                        self.mutabilidad
                                    ))
                # antes mandaba el primitivo Arreglo directo

                # para reportes
                self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                # -------------

                return None


            elif self.tipo == primitivo.tipo:

                entorno.addVariable(self.identificador, 
                                    Simbolo(primitivo.fila, 
                                    primitivo.columna, 
                                    self.identificador, 
                                    primitivo.tipo, 
                                    primitivo.valor, 
                                    self.mutabilidad) )


                # para reportes
                self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                # -------------

                return None


            elif primitivo.tipo == TipoExpresion.STRUCT:

                searchStruct = entorno.getStruct(self.tipo)

                if searchStruct is not None:

                    value_struct = self.valor.ejecutar(entorno)
                    value_struct.mutabilidad = self.mutabilidad
                    entorno.addVariable(self.identificador,value_struct)

                    # para reportes
                    self.tablaSimbolos.append([self.identificador,'Variable',primitivo.tipo,entorno.nombre,self.fila,self.columna])
                    # -------------

                    return None

                else:
                    # para reportes
                    self.tablaErrores.append([f'DECLARACION: Struct {self.tipo} no existe',entorno.nombre,self.fila,self.columna])
                    # --------------------------------
                    return f'DECLARACION: Struct {self.tipo} no existe'


            else: 
                # para reportes
                self.tablaErrores.append(['DECLARACION: error tipos no coinciden para declaracion de variables',entorno.nombre,self.fila,self.columna])
                # --------------------------------
                return 'DECLARACION: error tipos no coinciden para declaracion de variables'




        else:
            # para reportes
            self.tablaErrores.append(['DECLARACION: error tipos para declaracion de variables',entorno.nombre,self.fila,self.columna])
            # --------------------------------
            return 'DECLARACION: error tipos para declaracion de variables'




