from src.Interfaces.TipoExpresion import TipoExpresion	


class PrimateStruct:

    # lista de elementos y tipo 
    def __init__(self, elementos):
        self.elementos = elementos
        self.tipo = TipoExpresion.STRUCT



    def ejecutar(self, entorno):
        return self



        