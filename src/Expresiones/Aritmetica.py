
from turtle import right
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoOperador import TipoOperador
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Simbolo import Simbolo
from src.Error.Error import Error




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

    def ejecutar(self, entorno):


        # ejecucion del nodod izquierda y derecha
        nodoIzquierda = self.leftExp.ejecutar(entorno)
        nodoDerecha = self.rigthExp.ejecutar(entorno)


        print(f'Aritmetica --> {nodoIzquierda.tipo}')
        print(f'Aritmetica --> {nodoDerecha.tipo}')

        

        # verificacion si algun nodod que sube es una variable para buscar su valoe en el entorno
        if nodoIzquierda.tipo == TipoExpresion.ID and nodoDerecha.tipo == TipoExpresion.ID:

            nodoIzquierda = entorno.getVariable(nodoIzquierda.valor)
            nodoDerecha = entorno.getVariable(nodoDerecha.valor)

        elif nodoIzquierda.tipo == TipoExpresion.ID and nodoDerecha.tipo != TipoExpresion.ID:

            nodoIzquierda = entorno.getVariable(nodoIzquierda.valor)

        elif nodoIzquierda.tipo != TipoExpresion.ID and nodoDerecha.tipo == TipoExpresion.ID:

            nodoDerecha = entorno.getVariable(nodoDerecha.valor)



        print(f'Aritmetica --> {nodoIzquierda.valor}')
        print(f'Aritmetica --> {nodoDerecha.tipo}')        
        
        # ****************************************************************
        #  OPERACIONES ARITMECAS SOBRE LOS VALORES DE LOS NODOS     
        #  ****************************************************************

        # evalucacion de tipos de los primitivos
        if nodoIzquierda.tipo == nodoDerecha.tipo:


            # evaluacion de tipo valor --> INTEGER
            if nodoIzquierda.tipo == TipoExpresion.INTEGER:

                # suma
                if self.operador == TipoOperador.MAS:
                    result = nodoIzquierda.valor + nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, int(result))

                # resta
                elif self.operador == TipoOperador.MENOS:
                    result = nodoIzquierda.valor - nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, int(result))

                
                # multiplacion
                elif self.operador == TipoOperador.POR:
                    result = nodoIzquierda.valor * nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, int(result))

                # division
                elif self.operador == TipoOperador.DIV:
                    result = nodoIzquierda.valor / nodoDerecha.valor
                    self.tipo = TipoExpresion.INTEGER
                    return Primitivo(self.fila, self.columna, TipoExpresion.INTEGER, int(result))


            # evaluacion de tipo de valor --> FLOAT
            if nodoIzquierda.tipo == TipoExpresion.FLOAT:

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


            # evaluacion de tipo de valor --> FLOAT
            if nodoIzquierda.tipo == TipoExpresion.STRING:

                # suma
                if self.operador == TipoOperador.MAS:
                    result = nodoIzquierda.valor + nodoDerecha.valor
                    self.tipo = TipoExpresion.FLOAT
                    return Primitivo(self.fila, self.columna, TipoExpresion.FLOAT, result)





        # caso para tipos diferentes   
        else:
            # return Error('--> Aritmetica, Error operacion Aritmetica <-')
            # print('--> Aritmetica, Error operacion Aritmetica <-')
            return '--> Aritmetica, Error operacion Aritmetica <-'