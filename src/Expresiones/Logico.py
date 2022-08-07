from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoLogico import TipoLogico
from src.Interfaces.TipoExpresion import TipoExpresion


class Logico(Expresion):
    

    def __init__(self, fila, columna, leftExp, operador, rightExp):
        self.fila = fila 
        self.columna = columna
        self.leftExp = leftExp
        self.operador = operador
        self.rightExp = rightExp
        self.tipo = None


    def ejecutar(self, entorno):
        

        # evualicion de la compuert NOT
        if self.rightExp is None:

            # ejecutamos solo el nodo izquierdo
            nodoIzquierda = self.leftExp.ejecutar(entorno)

            #  evaluacion del tipo de operacion not
            if self.operador == TipoLogico.NOT:

                if nodoIzquierda.valor == 'false':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'true')
                

                elif nodoIzquierda.valor == 'true':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'false')



        elif self.leftExp != None and self.rightExp != None: 

            # ejecutamos los nodos de derecha y izquierda
            nodoIzquierda = self.leftExp.ejecutar(entorno)
            nodoDerecha = self.rightExp.ejecutar(entorno)

            # print(type(nodoIzquierda))
            # print(self.operador)
            # print(nodoDerecha)

            # evalucaion del tipo de operacion
            if self.operador == TipoLogico.OR:

                if nodoIzquierda.valor == 'false' and nodoDerecha.valor == 'false':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'false')
                

                elif nodoIzquierda.valor == 'false' and nodoDerecha.valor == 'true':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'true')


                elif nodoIzquierda.valor == 'true' and nodoDerecha.valor == 'false':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'true')


                elif nodoIzquierda.valor == 'true' and nodoDerecha.valor == 'true':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'true')



            #  evaluacion del tipo de operacion and
            elif self.operador == TipoLogico.AND:

                if nodoIzquierda.valor == 'false' and nodoDerecha.valor == 'false':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'false')
                

                elif nodoIzquierda.valor == 'false' and nodoDerecha.valor == 'true':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'false')

                elif nodoIzquierda.valor == 'true' and nodoDerecha.valor == 'false':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'false')

                elif nodoIzquierda.valor == 'true' and nodoDerecha.valor == 'true':
                    return Primitivo(self.fila, self.columna, TipoExpresion.BOOL, 'true')



        # no se cumple con ninguna condicion
        else: 
            return None








