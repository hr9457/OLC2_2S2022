from src.Expresiones.Primitivo import Primitivo
from src.environment.Simbolo import Simbolo

# clase para menejar los entornos
class Environment:
    
    # consturctor del entorno
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.variables = {}
        self.next = None
        self.prev = None




    #  metodo para agregar variables
    def addVariable(self, id ,nuevaVariable):


        self.variables.update({id: nuevaVariable})
        print('variable agregada')
        # si la lista no contiene elementos
        # if len(self.variables) == 0:
        #     self.variables.update({id: nuevaVariable})
        #     print('variable agregada')

        # else:
        #     for key in self.variables.keys():
        #         if key == id:
        #             print(f'variable --> {id} <--  existente')
        #             break
        #         else:
        #             print(' variable nuevas agregadas')
        #             self.variables.update({id: nuevaVariable})
        #             break





    # metodo para obtener valor de una variable
    def getVariable(self, id):

        # ciclo de busquede dentro del entorno
        for key in self.variables.keys():
            if key == id:
                # print(f'retornando variable  {self.variables[key].identificador}')
                # print(f'retornando variable  {self.variables[key].valor}')
                return Simbolo(
                    self.variables[key].fila,
                    self.variables[key].columna,
                    self.variables[key].identificador,
                    self.variables[key].tipo,
                    self.variables[key].valor,
                    self.variables[key].mutabilidad)
                





# if __name__ == '__main__':
#     print('entorno')
#     p = Primitivo(0, 0, 'integer', 3)
#     env = Environment('main', 1)

#     v = {}
#     v.update({'var1':p})
#     print(v['var1'].fila)
#     print(v['var1'].columna)
#     print(v['var1'].tipo)
#     print(v['var1'].valor)
#     print(len(v))