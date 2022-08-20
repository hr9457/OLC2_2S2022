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
        self.resultadoIf = ''
        self.resultadoElse = ''

    def ejecutar(self, entorno):

        print('DENTRO DE LA INSTRUCCION IF')
        

        # retorna un primitivo
        exp = self.expresion.ejecutar(entorno)

        # verifica que la expresion se de tipo boolean
        if exp.tipo == TipoExpresion.BOOL:

            # verificacion del valor de la expresion true o false
            if exp.valor == 'true':

                if self.instruccionesIF != None:

                    # creacion de un nuevo entrono para el manejo del if
                    numeroEntorno = entorno.numero + 1
                    envIf = Environment('IF', numeroEntorno, entorno)
                    self.resultadoIf = ''

                    for instruccion in self.instruccionesIF:

                        result = instruccion.ejecutar(envIf)
                        print(f'IF --> {result}')


                        # manejo para break y continue
                        if isinstance(result, Primitivo) and result.tipo == TipoExpresion.BREAK:
                            if result is not None and result.valor is not None:
                                self.resultadoIf += result.valor
                            retorno = Primitivo(None, None, TipoExpresion.BREAK, self.resultadoIf)
                            return retorno

                        elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                            if result is not None and result.valor is not None:
                                self.resultadoIf += result.valor
                            retorno = Primitivo(None, None, TipoExpresion.CONTINUE, self.resultadoIf)
                            return retorno


                        elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.RETURN:
                            result = result.ejecutar(envIf)
                            retorno = Primitivo(
                                None, 
                                None, 
                                TipoExpresion.RETURN, 
                                result.valor
                                )
                            return retorno

                        
                        if result != None:
                            self.resultadoIf += result


                    return self.resultadoIf


                else:
                    return self.resultadoIf



            else:

                if self.nodo != None:
                    # creacion de un nuevo entrono para el manejo de else y else if
                    numeroEntorno = entorno.numero + 1
                    envElse = Environment('ELSE/ELSE IF', numeroEntorno, entorno)
                    # self.resultadoElse = ''
                    return self.nodo.ejecutar(envElse)


                else:
                    return self.resultadoElse



        else:
            print('Condicion no es de tipo bool')
            return 'IF: Condicion no es de tipo bool'