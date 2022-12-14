
from turtle import right
from src.Expresiones.Primitivo import Primitivo
from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoOperador import TipoOperador
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Simbolo import Simbolo
from src.Error.Error import Error



from src.environment.Simbolo3d import Simbolo3d



# clase para manejar las sumas
class Aritmetica(Expresion):

    # constructor usando el constructor de la clase Nodo
    def __init__(self, fila, columna,lefExp, operador ,rigthExp):
        self.fila = fila 
        self.columna = columna
        self.leftExp = lefExp
        self.operador = operador
        self.rigthExp = rigthExp
        self.tipo = None
        # self.tablaErrores = tablaErrores

    def ejecutar(self, entorno):


        # ejecucion del nodod izquierda y derecha
        nodoIzquierda = self.leftExp.ejecutar(entorno)
        nodoDerecha = self.rigthExp.ejecutar(entorno)


        print(f'Aritmetica --> {nodoIzquierda.tipo}')
        print(f'Aritmetica --> {nodoDerecha}')

        

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
        
        
        
        
        
        # *************
        #  TIPOS DE ARREGLOS
        # ***********
        if nodoDerecha.tipo == TipoExpresion.ARREGLO:
            print('tipo de expresion arreglo')
            n = nodoDerecha.ejecutar(entorno)


        
        
        
        
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

                # mod
                elif self.operador == TipoOperador.DIV:
                    result = nodoIzquierda.valor % nodoDerecha.valor
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

                # mod
                elif self.operador == TipoOperador.DIV:
                    result = nodoIzquierda.valor % nodoDerecha.valor
                    self.tipo = TipoExpresion.FLOAT
                    return Primitivo(self.fila, self.columna, TipoExpresion.FLOAT, result)


            # evaluacion de tipo de valor --> FLOAT
            if nodoIzquierda.tipo == TipoExpresion.STRING:

                # suma
                if self.operador == TipoOperador.MAS:
                    result = nodoIzquierda.valor + nodoDerecha.valor
                    self.tipo = TipoExpresion.STRING
                    return Primitivo(self.fila, self.columna, TipoExpresion.STRING, result)





        # caso para tipos diferentes   
        else:
            # # para reportes
            # self.tablaErrores.append(['Aritmetica, Error operacion Aritmetica <-',entorno.nombre,self.fila,self.columna])
            # # --------------------------------
            return '--> Aritmetica, Error operacion Aritmetica <-'























    # traduccion en 3d
    def traducir(self, entorno, traductor3d):



        cadenaTraduccion3d = ''


        # ejecucion del nodod izquierda y derecha
        # OBTENER LOS VALORES
        # EJECUCION DEL NODO DERECHO Y DEL NODO IZQUIERDO
        nodoIzquierdo = self.leftExp.traducir(entorno, traductor3d)
        nodoDerecho = self.rigthExp.traducir(entorno, traductor3d)




        # VERIFICACION DE LOS NODOS SI SON TIPO ID Y HAY QUE BUSCARLOS EN EL STACK
        if nodoIzquierdo.tipo == TipoExpresion.ID and nodoDerecho.tipo == TipoExpresion.ID:

            nodoIzquierdo = entorno.getVariable3d(nodoIzquierdo.valor)
            nodoDerecho = entorno.getVariable3d(nodoDerecho.valor)


        # SI SOLO EL NODO IZQUIERDO ES UN ID
        elif nodoIzquierdo.tipo == TipoExpresion.ID and nodoDerecho.tipo != TipoExpresion.ID:

            nodoIzquierdo = entorno.getVariable3d(nodoIzquierdo.valor)


        # SI SOLO  EL NODO DERECHO ES UN ID
        elif nodoIzquierdo.tipo != TipoExpresion.ID and nodoDerecho.tipo == TipoExpresion.ID:

            nodoDerecho = entorno.getVariable3d(nodoDerecho.valor)





        
        
        # verificaion de tipo del nodo derecha y nodo izquierda
        if nodoIzquierdo.tipo == nodoDerecho.tipo:

            # evaluacion de tipo valor --> INTEGER o FLOAT
            if nodoIzquierdo.tipo == TipoExpresion.INTEGER:

                # suma
                if self.operador == TipoOperador.MAS:

                    
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} + {resultadoNodoDerecho} ;\n'
                    traductor3d.setContenidoMain(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.INTEGER,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************


                # resta
                if self.operador == TipoOperador.MENOS:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} - {resultadoNodoDerecho} ;\n'
                    traductor3d.setContenidoMain(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.INTEGER,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************



                # multiplicacion
                if self.operador == TipoOperador.POR:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} * {resultadoNodoDerecho} ;\n'
                    traductor3d.setContenidoMain(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.INTEGER,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************



                # division
                if self.operador == TipoOperador.DIV:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} / {resultadoNodoDerecho} ;\n'
                    traductor3d.setContenidoMain(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.INTEGER,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************





            # evaluacion de tipo valor --> FLOAT
            elif  nodoIzquierdo.tipo == TipoExpresion.FLOAT:

                # suma
                if self.operador == TipoOperador.MAS:

                    
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} + {resultadoNodoDerecho} ;\n'
                    traductor3d.setContenidoMain(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.FLOAT,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************


                # resta
                if self.operador == TipoOperador.MENOS:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} - {resultadoNodoDerecho} ;\n'
                    traductor3d.setContenidoMain(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.FLOAT,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************



                # multiplicacion
                if self.operador == TipoOperador.POR:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} * {resultadoNodoDerecho} ;\n'
                    traductor3d.setContenidoMain(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.FLOAT,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************



                # division
                if self.operador == TipoOperador.DIV:
                    # obteniendo valores de los nodos
                    resultadoNodoIzquierdo = nodoIzquierdo.valor
                    resultadoNodoDerecho = nodoDerecho.valor

                    # ********** traduccion **************
                    # obtengo el valor actual de los temporales
                    temporalActual = traductor3d.getTemporal()

                    cadenaTraduccion3d += f't{temporalActual} = {resultadoNodoIzquierdo} / {resultadoNodoDerecho} ;\n'
                    traductor3d.setContenidoMain(cadenaTraduccion3d)
                    traductor3d.aumentarTemporal()

                    return Simbolo3d(
                        self.fila,
                        self.columna,
                        None,
                        TipoExpresion.FLOAT,
                        f't{temporalActual}',
                        None,
                        0,
                        0
                    )
                    # *************************************