from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Error.Error import Error


# clase para manejar la instruccion println 
class Imprimir(Instruccion):

    def __init__(self, contenido):
        self.contenido = contenido

    # metodo para ejecutar el imprimir
    def ejecutar(self, entorno):

        # result = self.contenido.ejecutar().ejecutar()
        # primitivo

        # print(type(self.contenido))
        result = self.contenido.ejecutar(entorno)
        # print(f' IMPRIMIR <type> ->> {type(result)}')
        # print(f'IMPRIMIR: {result}')
        
        if isinstance(result, Error):
            print('es una clase error')
            return result.ejecutar()

        else:
            if result.tipo == TipoExpresion.ID:
                print(f'IMPRIMIR --> {result.valor}')
                result_env = entorno.getVariable(result.valor)
                print(f'IMPRIMIR: {result_env}')
                return result_env.valor
            else:
                print(result.tipo)
                return result.valor