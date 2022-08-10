from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Expresiones.Primitivo import Primitivo
from src.Instrucciones.Imprimir import Imprimir
from src.Instrucciones.Decision import instruccionElse


class InstruccionIf(Instruccion):

    def __init__(self, fila, columna, expresion, instruccionesIF=None, nodo=None):
        self.fila = fila
        self.columna = columna
        self.expresion = expresion
        self.instruccionesIF = instruccionesIF
        self.nodo = nodo
        



    def ejecutar(self,entorno):
        
        print('DENTRO DE LA INSTRUCCION IF')
        resultadoIf = ''
        resultadoElse = ''


        # retorna un primitivo
        exp = self.expresion.ejecutar(entorno)
        print(f'IF --> {self.instruccionesIF}')
        print(f'IF --> {self.nodo}')


        


        # verifica que la expresion se de tipo boolean
        if exp.tipo == TipoExpresion.BOOL:
            

            # verificacion del valor de la expresion true o false
            if exp.valor == 'true':
                # print(type(self.instrucciones))

                for instruccion in self.instruccionesIF:

                    # print(f'IF --> {type(instruccion)}')
                    # print(f'IF --> {type(instruccion.ejecutar(entorno))}')
                    result = instruccion.ejecutar(entorno)  
                    if result != None:
                        resultadoIf += result           

                return resultadoIf



            else:
                
                print('IF ==> lo que viene es un if ')
                print(type(self.nodo))
                return self.nodo.ejecutar(entorno)
                # listadoInstrucciones = self.nodo
                # for instruccion in listadoInstrucciones:
                #     result = instruccion.ejecutar(entorno)
                #     if result != None:
                #         resultadoElse += result

                # return resultadoElse



        else:
            print('Condicion no es de tipo bool')