from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Error.Error import Error
from src.Expresiones.Primitivo import Primitivo
from src.Instrucciones.Funciones import GetFuncion
from src.Instrucciones.Struct.PrimateStruct import PrimateStruct


# clase para manejar la instruccion println 
class Imprimir(Instruccion):

    def __init__(self, contenido, lista=None):
        self.contenido = contenido
        self.lista = lista

    # metodo para ejecutar el imprimir
    def ejecutar(self, entorno):


        # primitivo
        variables = '{}'
        countNodoDerecho = 0 

        


        # ejecucion de los nodos que trae
        result = self.contenido.ejecutar(entorno)

        


        # nodo derecho
        if self.lista is not None:
            countNodoDerecho = len(self.lista)


        if isinstance(result, Error):
            # print('es una clase error')
            return result.ejecutar()


        else:


            # contar cuantos elementos trae el nodo derecho
            if countNodoDerecho >= 1 and countNodoDerecho == result.valor.count(variables):

                # print('cantidad de {} == cantidad de elementos en lista')

            
                tempLista = []
                for instruccion in self.lista:


                    # print(type(instruccion))
                    resultadoInstruccion = instruccion.ejecutar(entorno)

                    # viene errores
                    if isinstance(resultadoInstruccion, str):
                        tempLista.append(resultadoInstruccion)




                    else:

                        # tipo para impresiones sea variables
                        if resultadoInstruccion.tipo == TipoExpresion.ID:
                            result_evn = entorno.getVariable(resultadoInstruccion.valor)
                            print(result_evn)

                            if result_evn.tipo == TipoExpresion.ARREGLO:

                                cadenaArray = '['
                                for v in result_evn.listadoExpresiones:

                                    cadenaArray += str(v.ejecutar(entorno).valor) + ', '

                                cadenaArray += ' ]'
                                tempLista.append(cadenaArray)


                            else:

                                tempLista.append(result_evn.valor)



                        # para cuando la imporesion sea una estructura
                        elif resultadoInstruccion.tipo == TipoExpresion.STRUCT:

                            var_struct = entorno.getVariable(resultadoInstruccion.identificador)

                            # buscar elemento el que se quiere imprimir
                            banderaStruct = False


                            for elemento in var_struct.elementos:

                                respuesta = elemento.ejecutar(entorno)

                                if respuesta.identificador == resultadoInstruccion.valor[0]:


                                    # print(respuesta.valor)
                                    # struct is struct
                                    # -----------------------------------------------------
                                    if isinstance(respuesta.valor,PrimateStruct):

                                        print('struct is struct')

                                        for elementSturct in respuesta.valor.elementos:
                                            elementSturct = elementSturct.ejecutar(entorno)
                                            print(elementSturct)

                                            if len(resultadoInstruccion.valor) >1:

                                                if elementSturct.identificador == resultadoInstruccion.valor[1]:
                                                    print(elementSturct.valor)
                                                    tempLista.append(elementSturct.valor)
                                                else:
                                                    tempLista.append(respuesta.valor)

                                            else:
                                                tempLista.append(respuesta.valor)
                                    # ---------------------------------------------------------


                                    # tiene que haber un proceso de struct is struct
                                    tempLista.append(respuesta.valor)
                                    banderaStruct= True


                            if banderaStruct == False:
                                return 'elemento en Struct no existe'




                        # impresiones de arreglos
                        elif resultadoInstruccion.tipo == TipoExpresion.ARREGLO:
                            print('paro obligatorio')
                            pass

                        # impresionsea valores primitivos
                        else:
                            tempLista.append(resultadoInstruccion.valor)




                print(tempLista)
                result.valor =  result.valor.format(*tempLista)
                return str(result.valor)+'\n'
            

            else:
                if result.tipo == TipoExpresion.ID:
                    result_env = entorno.getVariable(result.valor)
                    return str(result_env.valor) +'\n'

                else:
                    print(f'IMPRIMIR --> {result.tipo}')
                    print(f'IMPRIMIR --> {result.valor}')
                    return str(result.valor)+'\n'


                    