# from src.Interfaces.Expresion import Expresion
from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Environment import Environment
from src.Error.Error import Error





class While(Instruccion):

    def __init__(self, fila, columna, expresion, nodo=None):
        self.fila = fila
        self.columna = columna
        self.expresion = expresion
        self.nodo = nodo


    def ejecutar(self, entorno):
        
        retornoWhile = ''
        
        # ejecucion y evalucacion de la expresion
        exp = self.expresion.ejecutar(entorno)

        # la exp de ejeccutada es una variable
        if exp.tipo == TipoExpresion.ID:
            exp = entorno.getVariable(exp.valor)


        # revision de la expresion sea una expresion tipo bool
        if exp.tipo == TipoExpresion.BOOL:


            # creacion de un nuevo entrono para el while
            numeroEntorno = entorno.numero + 1
            envWhile = Environment('WHILE', numeroEntorno, entorno)


            # el valor sea un valor true
            # mientras sea verdadero
            while exp.valor == 'true' and self.nodo != None:
                
                # ciclo para repetir las instrucciones
                for instruccion in self.nodo:
                    result = instruccion.ejecutar(envWhile)
                    if result != None:
                        retornoWhile += result + '\n'
                
                # ejecutar una vez mas la expresion
                print(exp)
                exp = self.expresion.ejecutar(entorno)
                if exp.tipo == TipoExpresion.ID:
                    exp = entorno.getVariable(exp.valor)
                # print(f'WHILE -->{exp.valor}')
                

            
            # caso contrario
            return retornoWhile


        # la expresion no sea de tipo bool
        else:
            print('Condicion no es tipo bool')
            return Error('WHILE: Condicion no es tipo bool').ejecutar()