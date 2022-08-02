from abc import ABC, abstractmethod

class Nodo(ABC):
    # def __init__(self,fila,columna):
    #     self.fila = fila
    #     self.columna = columna

    # abstractclassmethod para todas la clases hijas
    @abstractmethod
    def ejecutar(self):
        pass