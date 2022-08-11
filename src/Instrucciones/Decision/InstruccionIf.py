from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Expresiones.Primitivo import Primitivo
from src.Instrucciones.Imprimir import Imprimir
from src.Instrucciones.Decision import instruccionElse
from src.environment.Environment import Environment
from src.Error.Error import Error


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
        
        
        # print(f'IF --> {self.instruccionesIF}')
        # print(f'IF --> {self.nodo}')

        # la exp de ejeccutada es una variable
        if exp.tipo == TipoExpresion.ID:
            exp = entorno.getVariable(exp.valor)
        


        # verifica que la expresion se de tipo boolean
        if exp.tipo == TipoExpresion.BOOL:
            

            # verificacion del valor de la expresion true o false
            if exp.valor == 'true':

                if self.instruccionesIF != None:
                    # creacion de un nuevo entrono para el manejo del if
                    numeroEntorno = entorno.numero + 1 
                    envIf = Environment('IF', numeroEntorno, entorno)

                    for instruccion in self.instruccionesIF:

                        # print(f'IF --> {type(instruccion)}')
                        # print(f'IF --> {type(instruccion.ejecutar(entorno))}')
                        result = instruccion.ejecutar(envIf)  

                        # print(result.tipo)

                        if result != None:
                            resultadoIf += result + '\n'           

                    return resultadoIf
                
                return resultadoIf



            else:
                
                # print('IF ==> lo que viene es un if ')
                # print(type(self.nodo))


                if self.nodo != None:
                    # creacion de un nuevo entrono para el manejo del if
                    numeroEntorno = entorno.numero + 1 
                    envElse = Environment('ELSE/ELSE IF', numeroEntorno, entorno)
                    return self.nodo.ejecutar(envElse)
                    
                
                else:
                    return resultadoElse



        else:
            print('Condicion no es de tipo bool')
            return Error('IF: Condicion no es de tipo bool')
