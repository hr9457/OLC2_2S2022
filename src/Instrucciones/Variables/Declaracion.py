from src.Interfaces.Instruccion import Instruccion
from src.environment.Simbolo import Simbolo
from src.Error.Error import Error


class Declaracion(Instruccion):

    # constructor
    def __init__(self, fila, columna, identificador, tipo, valor, mutabilidad):
        self.fila = fila
        self.columna = columna
        self.identificador = identificador
        self.tipo = tipo
        self.valor = valor
        self.mutabilidad = mutabilidad


    # metodo ejecutar
    def ejecutar(self, entorno):


        # verificacion de tipos
        # con tipo y el tipo del primitivo        
        primitivo = self.valor.ejecutar(entorno)

        # print(primitivo.tipo)
        # TIPO == None  es una variable sin tipo
        if self.tipo == None:
            # print(f'DECLARACION: {primitivo.tipo}')
            # print(primitivo.valor)
            entorno.addVariable(self.identificador, Simbolo(primitivo.fila, primitivo.columna, self.identificador, 
            primitivo.tipo, primitivo.valor, self.mutabilidad) )
            # print('variable agregada sin tipo')
            return None

        
        elif self.tipo != None:
            # print(self.tipo)
            # print(primitivo.tipo)
            if self.tipo == primitivo.tipo:
                # print(f'DECLARCION: --> {self.identificador}')
                entorno.addVariable(self.identificador, Simbolo(primitivo.fila, primitivo.columna, self.identificador, 
                primitivo.tipo, primitivo.valor, self.mutabilidad) )
                # print('variable agregada con tipo')
                return None

            else: 
                return Error('DECLARACION: tipos para declaracion de variables')


        else:
            return Error('DECLARACION: tipos para declaracion de variables')




