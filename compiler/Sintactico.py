# importacion de ply
from Compiler.Lexico import tokens, columnToken
input = ""

# importaciones de clases manejo de semantica

# importaciones para manejo de tipos
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoOperador import TipoOperador
from src.Interfaces.TipoRelacional import TipoRelacional
from src.Interfaces.TipoLogico import TipoLogico
from src.Interfaces.TipoMutable import TipoMutable


# importaciones para manejo de Expresiones
from src.Expresiones.Primitivo import Primitivo
from src.Expresiones.Aritmetica import Aritmetica
from src.Expresiones.Negativo import Negativo
from src.Expresiones.Relacional import Relacional
from src.Expresiones.Logico import Logico
from src.Expresiones.Pow import Pow


# importacion de instrucciones
from src.Instrucciones.Imprimir import Imprimir
from src.Instrucciones.Variables.Declaracion import Declaracion
from src.Instrucciones.Variables.Asignacion import Asignacion
from src.Instrucciones.Casteo.Casteo import Casteo





# menjo de entorno
from src.environment.Environment import Environment







# ----------------------------------------------------------------
#                      Precedencia de Operadores
# ----------------------------------------------------------------
# precedencia de abajo hacia arriba
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'UNOT'),
    ('left', 'IGUALDAD'),
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
                    | asignacion '''
    p[0] = p[1]










# ***************************
#   IMPRESION PERMITIDAS
# ***************************
def p_imprimir(p):
    #  imprimir = println ( exp ) 
    ' imprimir : PRINTLN PARENTESISIZQUIERDO exp PARENTESISDERECHO PUNTOCOMA '
    p[0] = Imprimir(p[3])










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
































# ***************************
#   ACEPTACION DE TIPOS
# ***************************
def p_tipos(p):
    '''  tipo   :   I64
                |   F64 
                |   BOOL 
                |   STRING
                |   CARACTER  '''

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
    env = Environment('main', None)


    salida = ""
    for l in lista:
        # print(f'lista {l}')
        result = l.ejecutar(env)
        if result != None:
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
