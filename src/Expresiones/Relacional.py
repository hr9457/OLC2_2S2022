from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoRelacional import TipoRelacional

from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.TipoExpresion import TipoExpresion

from src.Error.Error import Error


class Relacional(Expresion):


    def __init__(self, fila, columna, leftExp, operador, rightExp):
        self.fila = fila
        self.columna = columna
        self.leftExp = leftExp
        self.operador = operador
        self.rightExp = rightExp
        self.tipo = None


    def ejecutar(self, entorno):

        # ejecutamos nodos derecha y izquierda
        nodoIzquierda = self.leftExp.ejecutar(entorno)
        nodoDerecha = self.rightExp.ejecutar(entorno)


        print(f'RELACIONAL --> {nodoIzquierda}')
        print(f'RELACIONAL --> {self.operador}')
        print(f'RELACIONAL --> {type(nodoDerecha)}')
        


        # verificacion si algun nodod que sube es una variable para buscar su valoe en el entorno
        if nodoIzquierda.tipo == TipoExpresion.ID and nodoDerecha.tipo == TipoExpresion.ID:

            nodoIzquierda = entorno.getVariable(nodoIzquierda.valor)
            nodoDerecha = entorno.getVariable(nodoDerecha.valor)

        elif nodoIzquierda.tipo == TipoExpresion.ID and nodoDerecha.tipo != TipoExpresion.ID:

            nodoIzquierda = entorno.getVariable(nodoIzquierda.valor)

        elif nodoIzquierda.tipo != TipoExpresion.ID and nodoDerecha.tipo == TipoExpresion.ID:

            nodoDerecha = entorno.getVariable(nodoDerecha.valor)



       

        # evalucacion de tipos de los primitivos
        if nodoIzquierda.tipo == nodoDerecha.tipo:

            
            # evalucaion de tipo valor --> INTEGER
            if nodoIzquierda.tipo == TipoExpresion.INTEGER:


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


                # evalucacion de la diferentes
                if self.operador == TipoRelacional.DIFERENTE:

                    if nodoIzquierda.valor != nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')


            
            # evalucaion de tipo valor --> FLOAT
            if nodoIzquierda.tipo == TipoExpresion.FLOAT:


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



                # evalucacion de la diferentes 
                if self.operador == TipoRelacional.DIFERENTE:

                    if nodoIzquierda.valor != nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')





            # evalucaion de tipo valor --> FLOAT
            if nodoIzquierda.tipo == TipoExpresion.STRING:
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



                # evalucacion de la diferentes
                if self.operador == TipoRelacional.DIFERENTE:

                    if nodoIzquierda.valor != nodoDerecha.valor:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'true')
                    else:
                        return Primitivo(0, 0, TipoExpresion.BOOL, 'false')

                


        else:
            return Error('RELACIONAL: Error operador relacional')




