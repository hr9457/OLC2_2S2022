# importacion de ply
from Compiler.Lexico import tokens

# ----------------------------------------------------------------
#                      Precedencia de Operadores
# ----------------------------------------------------------------
# precedencia de abajo hacia arriba
precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICAR', 'DIV')
    )



# ----------------------------------------------------------------
#                      Definicion de la Gramatica
# ----------------------------------------------------------------

def p_expresion(p):
    '''expresion : valor MAS valor'''
    if p[2] == '+':
        p[0] = p[1] + p[3]


def p_valor(p):
    '''valor : ENTERO'''
    p[0] = p[1]


def p_error(p):
    print(f'Error sintactico en -> {p.value}')



import Compiler.ply.yacc as yacc
parser = yacc.yacc()


def analizar(entrada):
    return parser.parse(entrada)



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
