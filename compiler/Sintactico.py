# importacion de ply
from Compiler.Lexico import tokens, columnToken
input = ""

# importaciones de clases manejo de semantica

# importaciones para manejo de tipos
from src.Interfaces.TipoExpresion import TipoExpresion
from src.Interfaces.TipoOperador import TipoOperador
from src.Interfaces.TipoRelacional import TipoRelacional
from src.Interfaces.TipoLogico import TipoLogico


# importaciones para manejo de Expresiones
from src.Expresiones.Primitivo import Primitivo
from src.Expresiones.Aritmetica import Aritmetica
from src.Expresiones.Negativo import Negativo
from src.Expresiones.Relacional import Relacional
from src.Expresiones.Logico import Logico


# importacion de instrucciones
from src.Instrucciones.Imprimir import Imprimir



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
    ' instruccion : imprimir '
    p[0] = p[1]
    # print(type(p[0]))







# ***************************
#   IMPRESION PERMITIDAS
# ***************************
def p_imprimir(p):
    #  imprimir = println ( exp ) 
    ' imprimir : PRINTLN PARENTESISIZQUIERDO exp PARENTESISDERECHO '
    p[0] = Imprimir(p[3])






# ***************************
#   OPERACIONES ACPETADAS
# ***************************

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




def p_logica_unitaria(p):
    ' exp : NOT exp %prec UNOT '
    p[0] = Logico(0, 0, p[2], TipoLogico.NOT, None) 


def p_aritmetica_unaria(p):
    ' exp : MENOS exp %prec UMENOS '
    p[0] = Negativo(0, 0, p[2])



def p_aritmetica_agrupacion(p):
    ' exp : PARENTESISIZQUIERDO exp PARENTESISDERECHO '
    # ( exp )
    p[0] = p[2] 



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
                    | FALSE '''

    if p.slice[1].type == 'ENTERO': 
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.INTEGER, p[1])
    
    elif p.slice[1].type == 'DECIMAL':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.FLOAT, p[1])
    
    elif p.slice[1].type == 'TRUE':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.BOOL, p[1])

    elif p.slice[1].type == 'FALSE':
        p[0] = Primitivo(p.lineno(1), columnToken(input, p.slice[1]), TipoExpresion.BOOL, p[1])





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
    salida = ""
    for l in lista:
        # print(f'lista {l}')
        result = l.ejecutar()        
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
