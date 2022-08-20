# importacion de ply
from Compiler.Lexico import tokens, columnToken
from src.Instrucciones.Struct.BuildStruct import BuildStruct
input = ""

# importaciones de clases manejo de semantica

# importaciones para manejo de tipos
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoOperador import TipoOperador
from src.Interfaces.TipoRelacional import TipoRelacional
from src.Interfaces.TipoLogico import TipoLogico
from src.Interfaces.TipoMutable import TipoMutable
from src.Interfaces.TipoNativas import TipoNativas


# importaciones para manejo de Expresiones
from src.Expresiones.Primitivo import Primitivo
from src.Expresiones.Aritmetica import Aritmetica
from src.Expresiones.Negativo import Negativo
from src.Expresiones.Relacional import Relacional
from src.Expresiones.Logico import Logico
from src.Expresiones.Pow import Pow
from src.Expresiones.Nativas.Nativas import Nativas


# importacion de instrucciones
from src.Instrucciones.Imprimir import Imprimir
from src.Instrucciones.Variables.Declaracion import Declaracion
from src.Instrucciones.Variables.Asignacion import Asignacion
from src.Instrucciones.Casteo.Casteo import Casteo
from src.Instrucciones.Decision.InstruccionIf import InstruccionIf
from src.Instrucciones.Decision.instruccionElse import InstruccionElse
from src.Instrucciones.Bucle.While import While
from src.Instrucciones.Bucle.Loop import Loop
from src.Instrucciones.Bucle.Forin import Forin


# importaciones para funciones
from src.Instrucciones.Funciones.Funciones import Funciones
from src.Instrucciones.Funciones.GetFuncion import GetFuncion



# importaciones para structs
from src.Instrucciones.Struct.Struct import Struct
from src.Instrucciones.Struct.SimboloStruct import SimboloStruct



# menjo de entorno
from src.environment.Environment import Environment
from src.environment.Simbolo import Simbolo







# ----------------------------------------------------------------
#                      Precedencia de Operadores
# ----------------------------------------------------------------
# precedencia de abajo hacia arriba
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'UNOT'),
    ('left', 'IGUALDAD' ,'DIFERENTE'),
    ('left', 'MENOR', 'MAYOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICAR', 'DIV'),
    ('right', 'UMENOS')
    )








# ----------------------------------------------------------------
#                      Definicion de la Gramatica
# ----------------------------------------------------------------


# ***************************
# 
# ***************************

# ***************************
#   INICIO DE LA GRAMATICA
# ***************************
def p_inicio(p):
    ''' inicio : instrucciones '''
    p[0] = p[1]






# ***************************
#  GENERAR INSTRUCCIONES
# ***************************
def p_lista_instrucciones(p):
    ''' instrucciones : instrucciones instruccion '''
    p[1].append(p[2])
    p[0] = p[1]


def p_intrucciones(p):
    ''' instrucciones : instruccion '''
    p[0] = [p[1]]







# ***************************
#  INSTRUCCIONES DENTRO DEL LENGUAJE
# ***************************

def p_instruccion(p):
    ''' instruccion : imprimir  
                    | variable 
                    | asignacion
                    | instruccionif
                    | instruccionWhile 
                    | instruccionBreak
                    | instruccionContinue
                    | instruccionLoop
                    | instruccionFor
                    | funciones
                    | llamadofuncion
                    | funcionesParametros
                    | instruccionReturn
                    | instruccionStruct
                    | buildStruct '''
    p[0] = p[1]












# *************************************
#  RETORNOS PERMITIDOS EN EL LENGUAJE
# *************************************
def p_instruccion_break(p):
    ' instruccionBreak : BREAK PUNTOCOMA '
    p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.BREAK, None)







def p_instruccion_continue(p):
    ' instruccionContinue : CONTINUE PUNTOCOMA '
    p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.CONTINUE, None)





def p_instruccion_return(p):
    #       0              1     2     3
    ' instruccionReturn : RETURN exp PUNTOCOMA '
    p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.RETURN, p[2])















# ***************************
#   MANEJO DE FUNCIONES
# ***************************




# funciones void sin parametros
def p_funciones(p):
    #    0         1  2         3              4                   5             6            7
    ' funciones : FN ID PARENTESISIZQUIERDO PARENTESISDERECHO LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = Funciones(p.lineno(1), columnToken(input, p.slice[1]), p[2], None, p[6], None)









# funciones con tipo sin parametros
def p_funciones_tipo(p):
    #    0         1  2         3              4                   5      6          7           8            9
    ' funciones : FN ID PARENTESISIZQUIERDO PARENTESISDERECHO TIPORETURN tipo LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = Funciones(p.lineno(1), columnToken(input, p.slice[1]), p[2], None, p[8], p[6])










# llamado a funciones sin parametros
def p_llamado_funcion(p):
    #       0          1            2                3            4
    ' llamadofuncion : ID PARENTESISIZQUIERDO PARENTESISDERECHO PUNTOCOMA '
    p[0] = GetFuncion(0, 0, None, p[1])











# funciones con parametros
def p_funciones_parametros(p):
    #          0             1  2         3              4                   5             6            7           8
    ' funcionesParametros : FN ID PARENTESISIZQUIERDO parametros PARENTESISDERECHO LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = Funciones(p.lineno(1), columnToken(input, p.slice[1]), p[2], p[4], p[7], None)








# funciones con tipo y con parametros
def p_funciones_parametros_tipo(p):
    #          0             1  2         3              4                5             6       7           8            9           10
    ' funcionesParametros : FN ID PARENTESISIZQUIERDO parametros PARENTESISDERECHO  TIPORETURN tipo  LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = Funciones(p.lineno(1), columnToken(input, p.slice[1]), p[2], p[4], p[9], p[7])






# listado de parametros
def p_lista_parametros(p):
    #        0           1        2           3 
    ''' parametros : parametros COMA instruccionParametro '''
    p[1].append(p[3])
    p[0] = p[1]


def p_parametros(p):
    ''' parametros : instruccionParametro '''
    p[0] = [p[1]]



def p_instruccion_parametro(p):
    #       0                 1    2       3
    ' instruccionParametro : ID DOSPUNTOS tipo '
    p[0] = Simbolo(0, 0, p[1], p[3], None, TipoMutable.MUTABLE) 














# llamado a funciones con parametros
def p_llamado_funcion_parametros(p):
    #       0          1            2                3            4                   5
    ' llamadofuncion : ID PARENTESISIZQUIERDO parametrosllamado PARENTESISDERECHO PUNTOCOMA '
    p[0] = GetFuncion(0, 0, p[3], p[1])





# listado de parametros llamado a funcion(parametos)
def p_lista_parametros_llamado_funcion(p):
    #        0                 1               2           3 
    ''' parametrosllamado : parametrosllamado COMA instruccionLlamado '''
    p[1].append(p[3])
    p[0] = p[1]


def p_parametros_llamado_funcion(p):
    ''' parametrosllamado : instruccionLlamado '''
    p[0] = [p[1]]



def p_instruccion_parametro_llamado_funcion(p):
    #       0                 1 
    ' instruccionLlamado : exp '
    p[0] = p[1] 




















# ***************************
#   MANEJO DE STRUCTS
# ***************************

# menejo de struct simple
def p_struct(p):
    #         0              1   2         3              4         5
    ' instruccionStruct : STRUCT ID LLAVEIZQUIERDO listadoStruct LLAVEDERECHO '
    p[0] = Struct(p.lineno(2), columnToken(input, p.slice[2]), p[2], p[4])








def p_struct_listado(p):
    ' listadoStruct : listadoStruct COMA elementoStruct '
    p[1].append(p[3])
    p[0] = p[1]






def p_parametros_struct(p):
    ' listadoStruct : elementoStruct  '
    p[0] = [p[1]]






def p_elemento_struct(p):
    #        0          1   2         3  
    ' elementoStruct : ID DOSPUNTOS tipo '
    p[0] = Simbolo(
        p.lineno(1), 
        columnToken(input, p.slice[1]),
        p[1],
        p[3],
        None,
        TipoMutable.MUTABLE
        )










# build de structs
def p_build_struct(p):
    #    0           1         2            3          4            5
    ' buildStruct : ID LLAVEIZQUIERDO listadoBuild LLAVEDERECHO PUNTOCOMA '
    p[0] = BuildStruct(
        p.lineno(1),
        columnToken(input, p.slice[1]),
        p[1],
        p[3]
    )





def p_build_struct_listado(p):
    ' listadoBuild : listadoBuild COMA elementoBuild '
    p[1].append(p[3])
    p[0] = p[1]






def p_build_parametros_struct(p):
    ' listadoBuild : elementoBuild  '
    p[0] = [p[1]]
    # p[0] = [None]






def p_elemento_struct_build(p):
    #        0           1     2        3 
    ' elementoBuild :   ID  DOSPUNTOS   exp '    
    p[0] = SimboloStruct(p[1],p[3])
























# ***************************
#   IMPRESION PERMITIDAS
# ***************************
def p_imprimir(p):
    #  imprimir = println ( exp ) 
    #    0         1      2            3          4           5          6
    ' imprimir : PRINTLN NOT PARENTESISIZQUIERDO exp PARENTESISDERECHO PUNTOCOMA '
    p[0] = Imprimir(p[4], None)







def p_imprimir_elementos(p):
    #  imprimir = println ( exp ) 
    #    0         1      2            3          4    5        6          7                8
    ' imprimir : PRINTLN NOT PARENTESISIZQUIERDO exp COMA listadoprint PARENTESISDERECHO PUNTOCOMA '
    p[0] = Imprimir(p[4], p[6])






def p_lista_imprimir(p):
    ' listadoprint : listadoprint COMA exp '
    p[1].append(p[3])
    p[0] = p[1]






def p_print(p):
    ' listadoprint : exp '
    p[0] = [p[1]]





















# ***************************
#  DECLARACION DE VARIABLES
# ***************************

#  no mutable constates
def p_variables_mut_tipo(p):
    #     0              1   2   3   4        5    6      7    8
    '''  variable   :   LET MUT ID DOSPUNTOS tipo IGUAL exp PUNTOCOMA  '''

    # print(p[7])
    p[0] = Declaracion(0, 0, p[3], p[5], p[7], TipoMutable.MUTABLE)




def p_variables_mut(p):
    #     0              1   2   3   4    5      6    
    '''  variable   :   LET MUT ID IGUAL exp PUNTOCOMA  '''
    p[0] = Declaracion(0, 0, p[3], None, p[5], TipoMutable.MUTABLE)





# ---------------------- ** -------------------------
# mutables
def p_variables_tipo(p):
    #     0              1   2   3        4     5    6    7 
    '''  variable   :   LET ID DOSPUNTOS tipo IGUAL exp PUNTOCOMA  '''
    p[0] = Declaracion(0, 0, p[2], p[4], p[6], TipoMutable.NOMUTABLE)






def p_variables(p):
    #     0              1  2  3      4     5       
    '''  variable   :   LET ID IGUAL exp PUNTOCOMA  '''
    p[0] = Declaracion(0, 0, p[2], None, p[4], TipoMutable.NOMUTABLE)



















# ****************************************
#  ASIGNACION DE VALORES A UNA VARIABLE
# ****************************************
def p_asignacion_variables(p):
    #    0         1   2     3    4
    ' asignacion : ID IGUAL exp PUNTOCOMA '
    p[0] = Asignacion(0,0, p[1], p[3])



















# ****************************************
#  INSTRUCCIONE PARA MANEJO DEL IF
# ****************************************
def p_instruccion_if(p):
    #   0              1   2        3             4                5             6
    ' instruccionif : IF exp LLAVEIZQUIERDO   instrucciones   LLAVEDERECHO  instruccionElse'
    p[0] = InstruccionIf(0, 0, p[2], p[4], p[6])






def p_instruccion_else(p):
    #    0                 1        2           3              4        
    ''' instruccionElse : ELSE LLAVEIZQUIERDO instrucciones LLAVEDERECHO '''    
    p[0] = InstruccionElse(0, 0, p[3])






def p_instruccion_else_if(p):
    #    0                 1         2                  
    ''' instruccionElse : ELSE instruccionif
                        | '''
    # print(len(p))
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = None















# ****************************************
#  INSTRUCCIONE PARA MANEJO DEL WHILE
# ****************************************
def p_instruccion_while(p):
    #    0                1     2        3             4          5
    ' instruccionWhile : WHILE exp LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = While(p.lineno(1), columnToken(input, p.slice[1]), p[2], p[4])















# ****************************************
#  INSTRUCCIONE PARA MANEJO DEL LOOP
# ****************************************
def p_instruccion_loop(p):
    #    0                1          2              3          4
    ' instruccionLoop : LOOP LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = Loop(p.lineno(1), columnToken(input, p.slice[1]), p[3])













# ****************************************
#  INSTRUCCIONE PARA MANEJO DEL FOR IN
# ****************************************
def p_instruccion_forin(p):
    #    0              1   2  3   4   5     6     7       8             9             10 
    ' instruccionFor : FOR exp IN exp PUNTO PUNTO exp LLAVEIZQUIERDO instrucciones LLAVEDERECHO '
    p[0] = Forin(0, 0, p[2], p[4], p[7], p[9])













# ***************************
#   ACEPTACION DE TIPOS
# ***************************
def p_tipos(p):
    '''  tipo   :   I64
                |   F64 
                |   BOOL 
                |   STRING
                |   CARACTER
                |   ID  '''

    # print(p.slice[1].type)

    if p.slice[1].type == 'I64':
        p[0] = TipoExpresion.INTEGER


    elif p.slice[1].type == 'F64':
        p[0] = TipoExpresion.FLOAT


    elif p.slice[1].type == 'BOOL':
        p[0] = TipoExpresion.BOOL


    elif p.slice[1].type == 'STRING':
        p[0] = TipoExpresion.STRING


    elif p.slice[1].type == 'CARACTER':
        p[0] = TipoExpresion.CHAR



    elif p.slice[1].type == 'ID':
        p[0] = TipoExpresion.STRUCT












# **************************************
#   OPERACIONES ACPETADAS - EXPRESIONES
# **************************************

def p_aritmetica(p):
    # aritmetica + prim
    ''' exp : exp MAS exp 
            | exp MENOS exp 
            | exp MULTIPLICAR exp 
            | exp DIV exp
            | exp MAYOR exp 
            | exp MENOR exp 
            | exp MAYORIGUAL exp 
            | exp MENORIGUAL exp 
            | exp IGUALDAD exp
            | exp DIFERENTE exp
            | exp OR exp
            | exp AND exp '''

    if p[2] == '+':
        # p[0] = p[1] + p[3]
        p[0] = Aritmetica(0, 0, p[1], TipoOperador.MAS ,p[3])

    elif p[2] == '-':
        # p[0] = p[1] - p[3]
        p[0] = Aritmetica(0, 0, p[1], TipoOperador.MENOS ,p[3])

    elif p[2] == '*':
        # p[0] = p[1] * p[3]
        p[0] = Aritmetica(0, 0, p[1], TipoOperador.POR, p[3])
        
    elif p[2] == '/':
        # p[0] = p[1] / p[3]
        p[0] = Aritmetica(0, 0, p[1], TipoOperador.DIV, p[3])

    elif p[2] == '>':
        # p[0] = p[1] > p[3]
        p[0] = Relacional(0, 0, p[1], TipoRelacional.MAYORQUE, p[3])

    elif p[2] == '<':
        # p[0] = p[1] < p[3]
        p[0] = Relacional(0, 0, p[1], TipoRelacional.MENORQUE, p[3])


    elif p[2] == '>=':
        # p[0] = p[1] >= p[3]
        p[0] = Relacional(0, 0, p[1], TipoRelacional.MAYORIGUALQUE, p[3])


    elif p[2] == '<=':
        # p[0] = p[1] <= p[3]
        p[0] = Relacional(0, 0, p[1], TipoRelacional.MENORIGUALQUE, p[3])


    elif p[2] == '==':
        # p[0] = p[1] == p[3]
        p[0] = Relacional(0, 0, p[1], TipoRelacional.IGUALDAD, p[3])


    elif p[2] == '!=':
        # p[0] = p[1] == p[3]
        p[0] = Relacional(0, 0, p[1], TipoRelacional.DIFERENTE, p[3])


    elif p[2] == '||':
        # p[0] = p[1] || p[3]
        p[0] = Logico(0, 0, p[1], TipoLogico.OR, p[3])


    
    elif p[2] == '&&':
        # p[0] = p[1] || p[3]
        p[0] = Logico(0, 0, p[1], TipoLogico.AND, p[3])


    

# manejo de casteos para expresiones
def p_casteos(p):
    ''' exp :   exp AS I64 
        exp :   exp AS F64   '''

    if p.slice[3].type == 'I64':
        p[0] = Casteo(0,0, p[1], TipoExpresion.INTEGER)

    
    if p.slice[3].type == 'F64':
        p[0] = Casteo(0,0, p[1], TipoExpresion.FLOAT)




# manejo para funciones nativas
def p_funcion_nativa_tostring(p):
    ' exp : exp PUNTO TO_STRING PARENTESISIZQUIERDO PARENTESISDERECHO'
    p[0] = Nativas(0, 0, p[1], TipoNativas.TOSTRING)




def p_funcion_nativa_abs(p):
    ' exp : exp PUNTO ABS PARENTESISIZQUIERDO PARENTESISDERECHO '
    p[0] = Nativas(0, 0, p[1], TipoNativas.ABS)




def p_funcion_nativa_sqrt(p):
    ' exp : exp PUNTO SQRT PARENTESISIZQUIERDO PARENTESISDERECHO '
    p[0] = Nativas(0, 0, p[1], TipoNativas.SQRT)



def p_funcion_nativa_clone(p):
    ' exp : exp PUNTO CLONE PARENTESISIZQUIERDO PARENTESISDERECHO '
    p[0] = Nativas(0, 0, p[1], TipoNativas.CLONE)





# operaciones unitarias con precedencia
def p_logica_unitaria(p):
    ' exp : NOT exp %prec UNOT '
    p[0] = Logico(0, 0, p[2], TipoLogico.NOT, None) 


def p_aritmetica_unaria(p):
    ' exp : MENOS exp %prec UMENOS '
    p[0] = Negativo(0, 0, p[2])




# exp en una agrupacion
def p_aritmetica_agrupacion(p):
    ' exp : PARENTESISIZQUIERDO exp PARENTESISDERECHO '
    # ( exp )
    p[0] = p[2] 



# exp retornoa una potencia
def p_aritmetica_potencia(p):
    ''' exp : I64 DOSPUNTOS DOSPUNTOS POW PARENTESISIZQUIERDO exp COMA exp PARENTESISDERECHO 
            | F64 DOSPUNTOS DOSPUNTOS POW PARENTESISIZQUIERDO exp COMA exp PARENTESISDERECHO '''
    if p[1] == 'i64':
        p[0] = Pow(0, 0, TipoExpresion.INTEGER, p[6], p[8])	

    elif p[1] == 'f64':
        p[0] = Pow(0, 0, TipoExpresion.FLOAT, p[6], p[8])	



# exp retorno un primitivo
def p_expresion(p):
    ' exp : primitivo '
    p[0] = p[1]








# exp tipo espcial
# exp para funciones
def p_expresion_llamada_funcion(p):
    ' exp : ID PARENTESISIZQUIERDO PARENTESISDERECHO '
    p[0] = GetFuncion(0, 0, None, p[1])



def p_expresion_llamada_funcion_parametros(p):
    ' exp : ID PARENTESISIZQUIERDO parametrosllamado PARENTESISDERECHO '
    p[0] = GetFuncion(0, 0, p[3], p[1])




# ESTA DA  COMFLICTO


# expo para manejo de struct
# def p_expresion_tipo_struct(p):
#     ' exp : ID LLAVEIZQUIERDO listadoBuild LLAVEDERECHO '
#     p[0] = BuildStruct(
#         p.lineno(1),
#         columnToken(input, p.slice[1]),
#         p[1],
#         p[3]
#     )



def p_expresion_tipo_struct_elemento(p):
    ' exp : ID PUNTO ID '
    p[0] = Simbolo(
            p.lineno(1), 
            columnToken(input, p.slice[1]), 
            p[1],
            TipoExpresion.STRUCT, 
            p[2],
            TipoMutable.MUTABLE
            )









# ***************************
#   VALORES ACPETADOS
# ***************************

def p_valor(p):
    ''' primitivo   : ENTERO 
                    | DECIMAL
                    | TRUE
                    | FALSE
                    | CADENA
                    | CARACTER 
                    | ID '''

    if p.slice[1].type == 'ENTERO': 
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.INTEGER, p[1])
    
    elif p.slice[1].type == 'DECIMAL':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.FLOAT, p[1])
    
    elif p.slice[1].type == 'TRUE':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.BOOL, p[1])

    elif p.slice[1].type == 'FALSE':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.BOOL, p[1])

    elif p.slice[1].type == 'CADENA':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.STRING, p[1])


    elif p.slice[1].type == 'CARACTER':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.CHAR, p[1])


    elif p.slice[1].type == 'ID':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.ID, p[1])

















# ***************************
#   ERRORES CAPTURADOS
# ***************************

def p_error(p):
    print(f'Error sintactico en -> {p.value}')



















# ***************************
#   ARRANQUE DE LA GRAMATICA 
# ***************************

import Compiler.ply.yacc as yacc
parser = yacc.yacc()


def analizar(entrada):
    input = entrada
    lista = parser.parse(entrada)
    # print(lista)

    # entorno principal declarado
    env = Environment('main', 0, None)


    salida = ""
    for l in lista:
        # print(f'lista {l}')
        result = l.ejecutar(env)
        if result != None and isinstance(result, str):
            salida += str(result) + "\n"

    return salida



# if __name__ == '__main__':
#     # Build the parser
#     # import ply.yacc as yacc
#     # parser = yacc.yacc()
#
#     f = open('./entrada.txt')
#     contenido = f.read()
#
#     # result = parser.parse(contenido)
#     print(analizar(contenido))
