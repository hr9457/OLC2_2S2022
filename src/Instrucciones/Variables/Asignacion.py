from src.Interfaces.Instruccion import Instruccion
from src.Error.Error import Error
from src.Interfaces.TipoMutable import TipoMutable
from src.Interfaces.TipoExpresion import TipoExpresion
from src.environment.Simbolo import Simbolo




class Asignacion(Instruccion):



    def __init__(self, fila, columna, identificador, expresion, tablaErrores):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.expresion = expresion
        self.tablaErrores = tablaErrores



    
    def ejecutar(self,entorno): 
        print('ASIGNACION -->')    
        print(f'ASIGNACION --> {self.identificador}')
        print(f'ASIGNACION --> {self.expresion}')  


        # retorna un Simbolo o None
        result = entorno.getVariable(self.identificador)
        exp = self.expresion.ejecutar(entorno)


        print(f'ASIGNACION ==> {exp.valor}') 

        if isinstance(result, Error):
            print(f'ERROR ==> {result.mensaje}') 

        if result is not None:

            if result.mutabilidad == TipoMutable.MUTABLE:
                print(result.mutabilidad)
                # print('variable mutable')
                print(result.valor)
                print(result.tipo)

                if result.tipo == exp.tipo:
                    entorno.updateVariabe(self.identificador, 
                    Simbolo(
                        result.fila,
                        result.columna,
                        result.identificador,
                        result.tipo,
                        exp.valor,
                        result.mutabilidad
                    ))

                return None


            else:
                # para reportes
                self.tablaErrores.append(['ASIGNACION: Error asignar valor',entorno.nombre,self.fila,self.columna])
                # --------------------------------
                return 'ASIGNACION: Error asignar valor'


        else:
            # para reportes
            self.tablaErrores.append(['ASIGNACION: Error asignar valor',entorno.nombre,self.fila,self.columna])
            # --------------------------------
            return 'ASIGNACION: Error asignar valor'


