# importacion de la herramienta ply para utilizarla
import ply.lex as lex
lexer = lex.lex()


# ----------------------------------------------------------------
#                            Reservadas 
# ----------------------------------------------------------------
tokens = (
    'MAS',
    'ENTERO'
)


# ----------------------------------------------------------------
#                              Tokens 
# ----------------------------------------------------------------
t_MAS = r'\+'



# ----------------------------------------------------------------
#                      Expresiones Regulares
# ----------------------------------------------------------------

# MANEJO DE NUMERO ENTEROS
def t_entero(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f'Error al convertir a un valor entero {t.value}')
        t.value = 0
    return t


# MANEJO DE ERRORES
def t_error(t):
    print(f'Error lexico {t.value[0]}')
    t.lexer.skip(1)







# ----------------------------------------------------------------
#                      Precedencia de Operadores
# ----------------------------------------------------------------
precedence = (
    ('left' , 'MAS')
)







# ----------------------------------------------------------------
#                      Definicion de la Gramatica
# ----------------------------------------------------------------

def p_expresion(t):
    '''expresion : expresion MAS expresion'''
    if t[2] == '+':
        t[0] = t[1] + t[2]


def p_valor(t):
    '''valor : ENTERO'''
    t[0] = t[1]


def p_error(t):
    print(f'Error sintactico en {t.value}')