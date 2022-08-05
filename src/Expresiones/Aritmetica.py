
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoOperador import TipoOperador
from src.Interfaces.TipoExpresion import TipoExpresion




# clase para manejar las sumas
class Aritmetica(Expresion):

    # constructor usando el constructor de la clase Nodo
    def __init__(self, fila, columna, lefExp, operador ,rigthExp):
        self.fila = fila 
        self.columna = columna
        self.leftExp = lefExp
        self.operador = operador
        self.rigthExp = rigthExp
        self.tipo = None

    def ejecutar(self):

        # ejecucion de nodo derecho y izquierdo
        nodoIzquierda = self.leftExp.ejecutar()
        nodoDerecha = self.rigthExp.ejecutar()

        # print(nodoIzquierda)
        # print(nodoDerecha)

        

        # evalucacion de tipos de los primitivos
        if self.leftExp.tipo == self.rigthExp.tipo:


            # evaluacion de tipo valor --> INTEGER
            if self.leftExp.tipo == TipoExpresion.INTEGER:

                # suma
                if self.operador == TipoOperador.MAS:
                    result = nodoIzquierda.valor + nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, result)

                # resta
                elif self.operador == TipoOperador.MENOS:
                    result = nodoIzquierda.valor - nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, result)

                
                # multiplacion
                elif self.operador == TipoOperador.POR:
                    result = nodoIzquierda.valor * nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, result)

                # division
                elif self.operador == TipoOperador.DIV:
                    result = nodoIzquierda.valor / nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, result)


            # evaluacion de tipo de valor --> FLOAT
            if self.leftExp.tipo == TipoExpresion.FLOAT:

                # suma
                if self.operador == TipoOperador.MAS:
                    result = nodoIzquierda.valor + nodoDerecha.valor
                    self.tipo = TipoExpresion.FLOAT
                    return Primitivo(self.fila, self.columna, TipoExpresion.FLOAT, result)

                # resta
                elif self.operador == TipoOperador.MENOS:
                    result = nodoIzquierda.valor - nodoDerecha.valor
                    self.tipo = TipoExpresion.FLOAT
                    return Primitivo(self.fila, self.columna, TipoExpresion.FLOAT, result)

                
                # multiplacion
                elif self.operador == TipoOperador.POR:
                    result = nodoIzquierda.valor * nodoDerecha.valor
                    self.tipo = TipoExpresion.FLOAT
                    return Primitivo(self.fila, self.columna, TipoExpresion.FLOAT, result)

                # division
                elif self.operador == TipoOperador.DIV:
                    result = nodoIzquierda.valor / nodoDerecha.valor
                    self.tipo = TipoExpresion.FLOAT
                    return Primitivo(self.fila, self.columna, TipoExpresion.FLOAT, result)

        # caso para tipos diferentes   
        else:
            return None