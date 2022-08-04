from src.Interfaces.Expresion import Expresion
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Expresiones.Primitivo import Primitivo

class Negativo(Expresion):
    
    def __init__(self, nodo):
        self.nodo = nodo
        self.tipo = None

    def ejecutar(self):
        
        valor = self.nodo.ejecutar()

        if self.nodo.tipo == TipoExpresion.INTEGER:
            self.tipo = TipoExpresion.INTEGER
            return -1 * valor
            
    
        elif self.nodo.tipo == TipoExpresion.FLOAT:
            self.tipo = TipoExpresion.FLOAT
            return -1 * valor        

        else:
            return None