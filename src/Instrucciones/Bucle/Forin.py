from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Expresiones.Primitivo import Primitivo
from src.environment.Simbolo import Simbolo
from src.Interfaces.TipoMutable import TipoMutable
from src.Interfaces.TipoExpresion import TipoExpresion


class Forin(Instruccion):

    def __init__(self, fila, columna, variable, inicio, final, instrucciones):
        self.fila = fila
        self.columna = columna
        self.variable = variable
        self.inicio = inicio
        self.final = final
        self.instrucciones = instrucciones
        self.retornoForin = ''


    def ejecutar(self, entorno):


        # crear un nuevo entorno para el for
        numeroEntorno = entorno.numero + 1
        envFor = Environment('FOR',numeroEntorno,entorno)

        # print(f'FOR IN --> variable: {self.variable.tipo}')


        if self.inicio.tipo == TipoExpresion.INTEGER and self.final.tipo == TipoExpresion.INTEGER and self.variable.tipo == TipoExpresion.ID:

            # tipo de ejecucion del ciclo for
            inicioFor = self.inicio.ejecutar(entorno)
            finalFor = self.final.ejecutar(entorno)

            # creacion variables para iteraciones
            entorno.addVariable(self.variable.valor,
                        Simbolo(
                            self.fila,
                            self.columna,
                            self.variable.valor,
                            inicioFor.tipo,
                            inicioFor.valor,
                            TipoMutable.MUTABLE
                            ))


            # ejecucion del ciclo for
            for i in range(inicioFor.valor, finalFor.valor):

                # ejecucion de las instrucciones que hay en el ciclo for
                for instruccion in self.instrucciones:

                    result = instruccion.ejecutar(envFor)

                    # menejo de instrucciones break y continue
                    if isinstance(result, Primitivo) and result.tipo == TipoExpresion.BREAK:
                        if result.valor is not None:
                            self.retornoForin += result.valor
                        return self.retornoForin

                    elif isinstance(result, Primitivo) and result.tipo == TipoExpresion.CONTINUE:
                        if result.valor is not None:
                            self.retornoForin += result.valor
                        break


                    # concatenacion del resultado del for
                    if result is not None:
                        self.retornoForin += result


                # actualizcion de la variable
                variableFor = envFor.getVariable(self.variable.valor)
                envFor.updateVariabe(self.variable.valor,
                    Simbolo(
                        self.fila,
                        self.columna,
                        self.variable.valor,
                        inicioFor.tipo,
                        variableFor.valor + 1,
                        TipoMutable.MUTABLE
                        ))



            return self.retornoForin

        else:
            return 'FORIN : error paramentros'


        

