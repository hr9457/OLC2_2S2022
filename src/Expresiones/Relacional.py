from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoRelacional import TipoRelacional


class Relacional(Expresion):


    def __init__(self, leftExp, operador, rightExp):
        self.leftExp = leftExp
        self.operador = operador
        self.rightExp = rightExp
        self.tipo = None


    def ejecutar(self):

        # ejecutamos nodos derecha y izquierda
        izquierda = self.leftExp.ejecutar()
        derecha = self.rightExp.ejecutar()

        # evalucacion de tipos de los primitivos
        if self.leftExp.tipo == self.rightExp.tipo:

            
            # evalucaion de tipo valor --> INTEGER
            if self.leftExp.tipo == TipoExpresion.INTEGER:


                # evaluacion del mayor que 
                if self.operador == TipoRelacional.MAYORQUE:
                    
                    if izquierda > derecha:
                        return True
                    else:
                        return False

                
                # evaluacion del menor que
                if self.operador == TipoRelacional.MENORQUE:

                    if izquierda < derecha:
                        return True
                    else:
                        return False


                # evalucacion del mayor igual que
                if self.operador == TipoRelacional.MAYORIGUALQUE:

                    if izquierda >= derecha:
                        return True
                    else:
                        return False

                # evaluacion del menor igual que
                if self.operador == TipoRelacional.MENORIGUALQUE:

                    if izquierda <= derecha:
                        return True
                    else:
                        return False

                
                # evalucacion de la igual 
                if self.operador == TipoRelacional.IGUALDAD:

                    if izquierda == derecha:
                        return True
                    else:
                        return False


            
            # evalucaion de tipo valor --> FLOAT
            if self.leftExp.tipo == TipoExpresion.FLOAT:


                # evaluacion del mayor que 
                if self.operador == TipoRelacional.MAYORQUE:
                    
                    if izquierda > derecha:
                        return True
                    else:
                        return False

                
                # evaluacion del menor que
                if self.operador == TipoRelacional.MENORQUE:

                    if izquierda < derecha:
                        return True
                    else:
                        return False


                # evalucacion del mayor igual que
                if self.operador == TipoRelacional.MAYORIGUALQUE:

                    if izquierda >= derecha:
                        return True
                    else:
                        return False

                # evaluacion del menor igual que
                if self.operador == TipoRelacional.MENORORIGUALQUE:

                    if izquierda <= derecha:
                        return True
                    else:
                        return False

                
                # evalucacion de la igual 
                if self.operador == TipoRelacional.IGUALDAD:

                    if izquierda == derecha:
                        return True
                    else:
                        return False


        else:
            return None




