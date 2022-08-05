from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoRelacional import TipoRelacional

from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion


class Relacional(Expresion):


    def __init__(self, fila, columna, leftExp, operador, rightExp):
        self.fila = fila
        self.columna = columna
        self.leftExp = leftExp
        self.operador = operador
        self.rightExp = rightExp
        self.tipo = None


    def ejecutar(self):

        # ejecutamos nodos derecha y izquierda
        nodoIzquierda = self.leftExp.ejecutar()
        nodoDerecha = self.rightExp.ejecutar()

        # evalucacion de tipos de los primitivos
        if self.leftExp.tipo == self.rightExp.tipo:

            
            # evalucaion de tipo valor --> INTEGER
            if self.leftExp.tipo == TipoExpresion.INTEGER:


                # evaluacion del mayor que 
                if self.operador == TipoRelacional.MAYORQUE:
                    
                    if nodoIzquierda.valor > nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                        # return True
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')
                        # return False

                
                # evaluacion del menor que
                if self.operador == TipoRelacional.MENORQUE:

                    if nodoIzquierda.valor < nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')


                # evalucacion del mayor igual que
                if self.operador == TipoRelacional.MAYORIGUALQUE:

                    if nodoIzquierda.valor >= nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                # evaluacion del menor igual que
                if self.operador == TipoRelacional.MENORIGUALQUE:

                    if nodoIzquierda.valor <= nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                
                # evalucacion de la igual 
                if self.operador == TipoRelacional.IGUALDAD:

                    if nodoIzquierda.valor == nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')


            
            # evalucaion de tipo valor --> FLOAT
            if self.leftExp.tipo == TipoExpresion.FLOAT:


                # evaluacion del mayor que 
                if self.operador == TipoRelacional.MAYORQUE:
                    
                    if nodoIzquierda.valor > nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                
                # evaluacion del menor que
                if self.operador == TipoRelacional.MENORQUE:

                    if nodoIzquierda.valor < nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')


                # evalucacion del mayor igual que
                if self.operador == TipoRelacional.MAYORIGUALQUE:

                    if nodoIzquierda.valor >= nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                # evaluacion del menor igual que
                if self.operador == TipoRelacional.MENORIGUALQUE:

                    if nodoIzquierda.valor <= nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                
                # evalucacion de la igual 
                if self.operador == TipoRelacional.IGUALDAD:

                    if nodoIzquierda.valor == nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')






            # evalucaion de tipo valor --> FLOAT
            if self.leftExp.tipo == TipoExpresion.STRING:
                 # evaluacion del mayor que 
                if self.operador == TipoRelacional.MAYORQUE:
                    
                    if nodoIzquierda.valor > nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                
                # evaluacion del menor que
                if self.operador == TipoRelacional.MENORQUE:

                    if nodoIzquierda.valor < nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')


                # evalucacion del mayor igual que
                if self.operador == TipoRelacional.MAYORIGUALQUE:

                    if nodoIzquierda.valor >= nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                # evaluacion del menor igual que
                if self.operador == TipoRelacional.MENORIGUALQUE:

                    if nodoIzquierda.valor <= nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                
                # evalucacion de la igual 
                if self.operador == TipoRelacional.IGUALDAD:

                    if nodoIzquierda.valor == nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                


        else:
            return None




