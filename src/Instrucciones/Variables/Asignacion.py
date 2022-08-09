from src.Interfaces.Instruccion import Instruccion
from src.Error.Error import Error
from src.Interfaces.TipoMutable import TipoMutable
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Simbolo import Simbolo




class Asignacion(Instruccion):



    def __init__(self, fila, columna, identificador, expresion):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.expresion = expresion



    
    def ejecutar(self,entorno): 
        print('ASIGNACION -->')    
        print(self.identificador)  


        # retorna un Simbolo o None
        result = entorno.getVariable(self.identificador)

        if result is not None:

            if result.mutabilidad == TipoMutable.MUTABLE:
                # print(result.mutabilidad)
                # print('variable mutable')
                # print(self.expresion.valor)
                if result.tipo == TipoExpresion.INTEGER:
                    entorno.addVariable(self.identificador, 
                    Simbolo(
                        result.fila,
                        result.columna,
                        result.identificador,
                        result.tipo,
                        self.expresion.valor,
                        result.mutabilidad
                    ))


            else:
                print('variable no mutable')
                return Error('ASIGNACION: Error asignar valor').ejecutar()


        else:
            print('ASIGNACION: Error asignar valor')
            return Error('ASIGNACION: Error asignar valor').ejecutar()


