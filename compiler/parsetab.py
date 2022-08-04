
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftIGUALDADleftMENORMAYORMAYORIGUALMENORIGUALleftMASMENOSleftMULTIPLICARDIVrightUMENOSABS AMPERSAND AND AS BARRA BOOL BREAK CADENA CAPACITY CARACTER CHAR CLONE COMA COMENTARIO CONCATENARSTR CONTAINS CORCHETEDERECHO CORCHETEIZQUIERDO DECIMAL DIFERENTE DIV DOSPUNTOS ELSE ENTERO F64 FALSE FN I64 I64POW ID IF IGUAL IGUALDAD INSERT LEN LET LLAVEDERECHO LLAVEIZQUIERDO LOOP MAIN MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MULTIPLICAR MUT NEW NOT OR PARENTESISDERECHO PARENTESISIZQUIERDO PORCENTAJE PRINTLN PUNTO PUNTOCOMA PUSH REMOVE RETURN SQRT STRING STRUCT TIPORETURN TO_STRING TRUE USIZE WHAT WHILE WITH_CAPACITY inicio : instrucciones  instrucciones : instrucciones instruccion  instrucciones : instruccion  instruccion : imprimir  imprimir : PRINTLN PARENTESISIZQUIERDO exp PARENTESISDERECHO  exp : exp MAS exp \n            | exp MENOS exp \n            | exp MULTIPLICAR exp \n            | exp DIV exp\n            | exp MAYOR exp \n            | exp MENOR exp \n            | exp MAYORIGUAL exp \n            | exp MENORIGUAL exp \n            | exp IGUALDAD exp  exp : MENOS exp %prec UMENOS  exp : PARENTESISIZQUIERDO exp PARENTESISDERECHO  exp : primitivo  primitivo   : ENTERO \n                    | DECIMAL '
    
_lr_action_items = {'PRINTLN':([0,2,3,4,6,15,],[5,5,-3,-4,-2,-5,]),'$end':([1,2,3,4,6,15,],[0,-1,-3,-4,-2,-5,]),'PARENTESISIZQUIERDO':([5,7,8,10,16,17,18,19,20,21,22,23,24,],[7,8,8,8,8,8,8,8,8,8,8,8,8,]),'MENOS':([7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,],[10,10,17,10,-17,-18,-19,17,10,10,10,10,10,10,10,10,10,-15,-16,-6,-7,-8,-9,17,17,17,17,17,]),'ENTERO':([7,8,10,16,17,18,19,20,21,22,23,24,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'DECIMAL':([7,8,10,16,17,18,19,20,21,22,23,24,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'PARENTESISDERECHO':([9,11,12,13,14,25,26,27,28,29,30,31,32,33,34,35,],[15,-17,-18,-19,26,-15,-16,-6,-7,-8,-9,-10,-11,-12,-13,-14,]),'MAS':([9,11,12,13,14,25,26,27,28,29,30,31,32,33,34,35,],[16,-17,-18,-19,16,-15,-16,-6,-7,-8,-9,16,16,16,16,16,]),'MULTIPLICAR':([9,11,12,13,14,25,26,27,28,29,30,31,32,33,34,35,],[18,-17,-18,-19,18,-15,-16,18,18,-8,-9,18,18,18,18,18,]),'DIV':([9,11,12,13,14,25,26,27,28,29,30,31,32,33,34,35,],[19,-17,-18,-19,19,-15,-16,19,19,-8,-9,19,19,19,19,19,]),'MAYOR':([9,11,12,13,14,25,26,27,28,29,30,31,32,33,34,35,],[20,-17,-18,-19,20,-15,-16,-6,-7,-8,-9,-10,-11,-12,-13,20,]),'MENOR':([9,11,12,13,14,25,26,27,28,29,30,31,32,33,34,35,],[21,-17,-18,-19,21,-15,-16,-6,-7,-8,-9,-10,-11,-12,-13,21,]),'MAYORIGUAL':([9,11,12,13,14,25,26,27,28,29,30,31,32,33,34,35,],[22,-17,-18,-19,22,-15,-16,-6,-7,-8,-9,-10,-11,-12,-13,22,]),'MENORIGUAL':([9,11,12,13,14,25,26,27,28,29,30,31,32,33,34,35,],[23,-17,-18,-19,23,-15,-16,-6,-7,-8,-9,-10,-11,-12,-13,23,]),'IGUALDAD':([9,11,12,13,14,25,26,27,28,29,30,31,32,33,34,35,],[24,-17,-18,-19,24,-15,-16,-6,-7,-8,-9,-10,-11,-12,-13,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,6,]),'imprimir':([0,2,],[4,4,]),'exp':([7,8,10,16,17,18,19,20,21,22,23,24,],[9,14,25,27,28,29,30,31,32,33,34,35,]),'primitivo':([7,8,10,16,17,18,19,20,21,22,23,24,],[11,11,11,11,11,11,11,11,11,11,11,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> instrucciones','inicio',1,'p_inicio','Sintactico.py',64),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_lista_instrucciones','Sintactico.py',74),
  ('instrucciones -> instruccion','instrucciones',1,'p_intrucciones','Sintactico.py',80),
  ('instruccion -> imprimir','instruccion',1,'p_instruccion','Sintactico.py',91),
  ('imprimir -> PRINTLN PARENTESISIZQUIERDO exp PARENTESISDERECHO','imprimir',4,'p_imprimir','Sintactico.py',105),
  ('exp -> exp MAS exp','exp',3,'p_aritmetica','Sintactico.py',119),
  ('exp -> exp MENOS exp','exp',3,'p_aritmetica','Sintactico.py',120),
  ('exp -> exp MULTIPLICAR exp','exp',3,'p_aritmetica','Sintactico.py',121),
  ('exp -> exp DIV exp','exp',3,'p_aritmetica','Sintactico.py',122),
  ('exp -> exp MAYOR exp','exp',3,'p_aritmetica','Sintactico.py',123),
  ('exp -> exp MENOR exp','exp',3,'p_aritmetica','Sintactico.py',124),
  ('exp -> exp MAYORIGUAL exp','exp',3,'p_aritmetica','Sintactico.py',125),
  ('exp -> exp MENORIGUAL exp','exp',3,'p_aritmetica','Sintactico.py',126),
  ('exp -> exp IGUALDAD exp','exp',3,'p_aritmetica','Sintactico.py',127),
  ('exp -> MENOS exp','exp',2,'p_aritmetica_unaria','Sintactico.py',174),
  ('exp -> PARENTESISIZQUIERDO exp PARENTESISDERECHO','exp',3,'p_aritmetica_agrupacion','Sintactico.py',180),
  ('exp -> primitivo','exp',1,'p_expresion','Sintactico.py',187),
  ('primitivo -> ENTERO','primitivo',1,'p_valor','Sintactico.py',199),
  ('primitivo -> DECIMAL','primitivo',1,'p_valor','Sintactico.py',200),
]
