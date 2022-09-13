from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Error.Error import Error
from src.Expresiones.Primitivo import Primitivo
from src.Instrucciones.Funciones import GetFuncion
from src.Instrucciones.Struct.PrimateStruct import PrimateStruct
from src.environment.Simbolo import Simbolo


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

            tempLista = []
            # contar cuantos elementos trae el nodo derecho
            if countNodoDerecho >= 1 and countNodoDerecho == result.valor.count(variables):

                # print('cantidad de {} == cantidad de elementos en lista')

            

                for instruccion in self.lista:


                    # print(type(instruccion))
                    resultadoInstruccion = instruccion.ejecutar(entorno)

                    # viene errores
                    if isinstance(resultadoInstruccion, str):
                        tempLista.append(resultadoInstruccion)


                    elif resultadoInstruccion.tipo == TipoExpresion.VECTOR:
                        cadenaVector = '['
                        tempLista.append(self.imprimiVector(resultadoInstruccion.valor, cadenaVector, entorno))


                    else:

                        # tipo para impresiones sea variables
                        if resultadoInstruccion.tipo == TipoExpresion.ID:
                            result_evn = entorno.getVariable(resultadoInstruccion.valor)
                            print(result_evn)

                            if result_evn.tipo == TipoExpresion.ARREGLO and result_evn is not None:

                                cadenaArray = '['

                                tempLista.append(self.imprimirArreglo(result_evn, entorno, cadenaArray))


                            elif result_evn.tipo == TipoExpresion.VECTOR and result_evn is not None:

                                cadenaVector = '['
                                tempLista.append(self.imprimiVector(result_evn.lista,cadenaVector,entorno))


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


                            concatenacionArreglo = '['
                            tempLista.append(self.imprimirArreglo(resultadoInstruccion,entorno, concatenacionArreglo))
                            concatenacionArreglo = ''

                        # elif result_evn.tipo == TipoExpresion.ARREGLO and result_evn is not None:
                        #
                        #     cadenaArray = '['
                        #
                        #     tempLista.append(self.imprimirArreglo(result_evn, entorno, cadenaArray))


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


                    




    # funcion para la impresion variables tipo arreglo
    def imprimirArreglo(self, arreglo, entorno, concatenacionArreglo):


        # concatenacionArreglo = '['


        if isinstance(arreglo, Simbolo):

            for v in arreglo.valor:

                if v.tipo != TipoExpresion.ARREGLO:
                    concatenacionArreglo += str(v.ejecutar(entorno).valor) + ', '

                else:
                    concatenacionArreglo += self.imprimirArreglo(v,entorno,concatenacionArreglo)

        else: 

            for v in arreglo.valor:

                if v.tipo != TipoExpresion.ARREGLO:
                    concatenacionArreglo += str(v.ejecutar(entorno).valor) + ', '
                else:
                    concatenacionArreglo += self.imprimirArreglo(v,entorno,concatenacionArreglo)


        concatenacionArreglo += ' ]'

        return concatenacionArreglo



    def imprimiVector(self, lista, cadenaVector, entorno):

        for elementoLista in lista:

            if elementoLista.tipo == TipoExpresion.VECTOR:
                cadenaVector += self.imprimiVector(elementoLista.lista, cadenaVector, entorno)


            else:
                elemento = elementoLista.ejecutar(entorno)

                cadenaVector += str(elemento.valor)

            cadenaVector += ','

        cadenaVector += ']'

        return cadenaVector





















    # traduccion a 3d
    def traducir(self, entorno, traductor3d):


        # traduccion a 3d
        cadenaTraduccion3d = ''

        # primitivo
        variables = '{}'
        countNodoDerecho = 0

        # obtener el contenido que va imprimir
        # tien que retornar un Simbolo
        resultado = self.contenido.traducir(entorno, traductor3d)




        # impresion de expresiones tipo integer y tipo float
        if resultado.tipo == TipoExpresion.INTEGER:
            # ************ traduccion ******************
            cadenaTraduccion3d += f'printf("%d", (int){resultado.valor}); \n'
            cadenaTraduccion3d += 'printf("%c", (int)10);\n'

            traductor3d.setContenidoMain(cadenaTraduccion3d)
            # ******************************************




        # impresion de expresiones tipo  float
        elif resultado.tipo == TipoExpresion.FLOAT:
            # ************ traduccion ******************
            cadenaTraduccion3d += f'printf("%f", {resultado.valor}); \n'
            cadenaTraduccion3d += 'printf("%c", (int)10);\n'

            traductor3d.setContenidoMain(cadenaTraduccion3d)
            # ******************************************



        elif resultado.tiop == TipoExpresion.CHAR:
            # ************ traduccion ******************
            cadenaTraduccion3d += f'printf("%c", {resultado.valor}); \n'
            cadenaTraduccion3d += 'printf("%c", (int)10);\n'

            traductor3d.setContenidoMain(cadenaTraduccion3d)
            # ******************************************


        # impresion de expresiones tipo  booleanos
        elif resultado.tipo == TipoExpresion.BOOL:
            
            if resultado.valor == 'true':
                # ************ traduccion ******************
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*--------- BOOLEANO ------------*/\n'
                cadenaTraduccion3d += 'printf("%c", (int)116);\n'
                cadenaTraduccion3d += 'printf("%c", (int)114);\n'
                cadenaTraduccion3d += 'printf("%c", (int)117);\n'
                cadenaTraduccion3d += 'printf("%c", (int)101);\n'
                cadenaTraduccion3d += 'printf("%c", (int)10);\n'
                traductor3d.setContenidoMain(cadenaTraduccion3d)
                # ******************************************

            elif resultado.valor == 'false':
                # ************ traduccion ******************
                cadenaTraduccion3d += '\n'
                cadenaTraduccion3d += '/*--------- BOOLEANO ------------*/\n'
                cadenaTraduccion3d += 'printf("%c", (int)102);\n'
                cadenaTraduccion3d += 'printf("%c", (int)97);\n'
                cadenaTraduccion3d += 'printf("%c", (int)108);\n'
                cadenaTraduccion3d += 'printf("%c", (int)115);\n'
                cadenaTraduccion3d += 'printf("%c", (int)101);\n'
                cadenaTraduccion3d += 'printf("%c", (int)10);\n'
                cadenaTraduccion3d += 'printf("%c", (int)13);\n'
                cadenaTraduccion3d += 'printf("%c", (int)10);\n'
                traductor3d.setContenidoMain(cadenaTraduccion3d)
                # ******************************************



        # impiresion de expresiones tipo string
        elif resultado.tipo == TipoExpresion.STRING:

            # ************ traduccion ******************

            # guardo va iniciar el arreglo en el stack
            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*--------- MOVIMIENTOS PARA UN STRING ------------*/\n'
            cadenaTraduccion3d += 'stack[(int)P] = H;\n'
            cadenaTraduccion3d += 'P = P + 1;\n'

            # guardo el tambio del arreglo en la primera posicion del heap
            cadenaTraduccion3d += f'heap[(int)H] = {len(resultado.valor)};\n'
            cadenaTraduccion3d += 'H = H + 1;\n'

            # guardo el tamanio del arreglo en t0
            cadenaTraduccion3d += f't0 = {len(resultado.valor)};\n'

            # guardo donde inicio el arreglo
            cadenaTraduccion3d += f't1 = H;\n'

            # for para recorrer caracter a caracter el string
            for letra in resultado.valor:
                cadenaTraduccion3d += f'heap[(int)H] = {ord(letra)};\n'
                cadenaTraduccion3d += f'H = H + 1;\n'


            cadenaTraduccion3d += '\n'
            cadenaTraduccion3d += '/*--------- IMPRESION DE UN STRING -----------*/\n'
            cadenaTraduccion3d += 'printString();\n'
            cadenaTraduccion3d += '\n'  
            cadenaTraduccion3d += 'printf("%c", (int)10);\n'

            traductor3d.setContenidoMain(cadenaTraduccion3d)
                

            # ******************************************



        return None