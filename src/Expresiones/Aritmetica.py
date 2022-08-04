
from fileinput import filename
from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoOperador import TipoOperador
from src.Interfaces.TipoExpresion import TipoExpresion




# clase para manejar las sumas
class Aritmetica(Expresion):

    # constructor usando el constructor de la clase Nodo
    def __init__(self, lefExp, operador ,rigthExp):
        self.leftExp = lefExp
        self.operador = operador
        self.rigthExp = rigthExp
        self.tipo = None

    def ejecutar(self):

        # ejecucion de nodo derecho y izquierdo
        izquierda = self.leftExp.ejecutar()
        derecha = self.rigthExp.ejecutar()

        

        # evalucacion de tipos de los primitivos
        if self.leftExp.tipo == self.rigthExp.tipo:


            # evaluacion de tipo valor --> INTEGER
            if self.leftExp.tipo == TipoExpresion.INTEGER:

                # suma
                if self.operador == TipoOperador.MAS:
                    result = izquierda + derecha
                    self.tipo = TipoExpresion.INTEGER
                    return result
                    # primitivo = Primitivo(0, 0, TipoExpresion.INTEGER, result)
                    # return primitivo 

                # resta
                elif self.operador == TipoOperador.MENOS:
                    result = izquierda - derecha
                    self.tipo = TipoExpresion.INTEGER
                    return result

                
                # multiplacion
                elif self.operador == TipoOperador.POR:
                    result = izquierda * derecha
                    self.tipo = TipoExpresion.INTEGER
                    return result

                # division
                elif self.operador == TipoOperador.DIV:
                    result = izquierda / derecha
                    self.tipo = TipoExpresion.INTEGER
                    return result


            # evaluacion de tipo de valor --> FLOAT
            if self.leftExp.tipo == TipoExpresion.FLOAT:

                # suma
                if self.operador == TipoOperador.MAS:
                    result = izquierda + derecha
                    self.tipo = TipoExpresion.FLOAT
                    return result
                    # primitivo = Primitivo(0, 0, TipoExpresion.FLOAT, result)
                    # return primitivo 

                # resta
                elif self.operador == TipoOperador.MENOS:
                    result = izquierda - derecha
                    self.tipo = TipoExpresion.FLOAT
                    return result

                
                # multiplacion
                elif self.operador == TipoOperador.POR:
                    result = izquierda * derecha
                    self.tipo = TipoExpresion.FLOAT
                    return result

                # division
                elif self.operador == TipoOperador.DIV:
                    result = izquierda / derecha
                    self.tipo = TipoExpresion.FLOAT
                    return result

        # caso para tipos diferentes   
        else:
            return None
            
