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
        # print(f'IMPRIMIR --> {result.tipo}')
        
        if isinstance(result, Error):
            # print('es una clase error')
            return result.ejecutar()

        else:
            if result.tipo == TipoExpresion.ID:
                result_env = entorno.getVariable(result.valor)
                return str(result_env.valor)
            else:
                print(f'IMPRIMIR --> {result.tipo}')
                print(f'IMPRIMIR --> {result.valor}')
                return str(result.valor)