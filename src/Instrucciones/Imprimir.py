from src.Interfaces.Instruccion import Instruccion
from src.environment.Environment import Environment
from src.Interfaces.TipoExpresion import TipoExpresion


# clase para manejar la instruccion println 
class Imprimir(Instruccion):

    def __init__(self, contenido):
        self.contenido = contenido

    # metodo para ejecutar el imprimir
    def ejecutar(self, entorno):

        # result = self.contenido.ejecutar().ejecutar()
        # primitivo
        
        result = self.contenido.ejecutar(entorno)
        # print(f' IMPRIMIR <type> ->> {type(result)}')
        # print(result.tipo)

        if result.tipo == TipoExpresion.ID:
            result_env = entorno.getVariable(result.valor)
            return result_env.valor
        else:
            return result.valor