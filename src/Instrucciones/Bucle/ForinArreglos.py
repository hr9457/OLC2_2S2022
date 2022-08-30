from src.Interfaces.Instruccion import Instruccion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoMutable import TipoMutable
from src.environment.Environment import Environment
from src.environment.Environment import Simbolo
from src.Expresiones.Primitivo import Primitivo




class ForinArreglos(Instruccion):

    def __init__(self,fila, columna, pivote, variable, instrucciones):
        self.fila = fila
        self.columna = columna
        self.pivote = pivote
        self.variable = variable
        self.instrucciones = instrucciones


    def ejecutar(self, entorno):

        retornoForinArreglos = ''



        # primer filtro verificacion del pivote
        if self.pivote is not None and self.pivote.tipo == TipoExpresion.ID:

            
            # agregro variable en el entorno afuera del for
            entorno.addVariable(self.pivote.valor,
                        Simbolo(
                            self.fila,
                            self.columna,
                            self.pivote.valor, # identificador
                            self.pivote.tipo,
                            '',
                            TipoMutable.MUTABLE
                            ))
            
            
            
            
            # creacion de un nuevo entorno para el for
            numeroEntorno = entorno.numero + 1
            envForIn = Environment('FOR',numeroEntorno,entorno)


            # ejecucion del la expresion para recorrer
            exp = self.variable.ejecutar(entorno)
            variablePivote = self.pivote.ejecutar(entorno)


            # si la expresion es un arreglo que poder recorrer
            if exp.tipo == TipoExpresion.ARREGLO:



                # for para recorrer el arreglo y su contenido
                for elementoArreglo in exp.listadoExpresiones:

                    

                    # listado del valor del arreglo
                    elemento = elementoArreglo.ejecutar(entorno)


                    # nueva asigancion a la variable pivote con el valor del arreglo
                    # actualizacon de la variable pivote con su nuevo valor
                    varPivote = entorno.getVariable(self.pivote.valor)
                    varPivote.valor = elemento.valor
                    varPivote.tipo = elemento.tipo
                    entorno.addVariable(self.pivote.valor,varPivote)

                    
                    
                    for instruccion in self.instrucciones:

                        result = instruccion.ejecutar(envForIn)

                        # menejo de instrucciones break y continue
                        if isinstance(result, Primitivo) and result.tipo == TipoExpresion.BREAK:
                            if result.valor is not None:
                                retornoForinArreglos += result.valor
                            return retornoForinArreglos

                        elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                            if result.valor is not None:
                                retornoForinArreglos += result.valor
                            break


                        # concatenacion del resultado del for
                        if result is not None:
                            retornoForinArreglos += result



                return retornoForinArreglos






        else:
            return f'var {self.pivote.valor} no es un ID'


        return None