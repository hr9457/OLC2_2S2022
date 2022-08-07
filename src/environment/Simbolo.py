from src.Interfaces.TipoExpresion import TipoExpresion


class Simbolo:

    
    def __init__(self, fila, columna, identificador, tipo, valor, mutabilidad):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.tipo = tipo
        self.valor = valor 
        self.mutabilidad = mutabilidad 




    def ejecutar(self):
        return Simbolo(
            self.fila,
            self.columna,
            self.identificador,
            self.tipo,
            self.valor,
            self.mutabilidad
        )