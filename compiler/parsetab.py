
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightUNOTleftIGUALDADDIFERENTEleftMENORMAYORMAYORIGUALMENORIGUALleftMASMENOSleftMULTIPLICARDIVrightUMENOSABS AMPERSAND AND AS BARRA BOOL BREAK CADENA CAPACITY CARACTER CHAR CLONE COMA COMENTARIO CONTAINS CORCHETEDERECHO CORCHETEIZQUIERDO DECIMAL DIFERENTE DIV DOSPUNTOS ELSE ENTERO F64 FALSE FN I64 ID IF IGUAL IGUALDAD INSERT LEN LET LLAVEDERECHO LLAVEIZQUIERDO LOOP MAIN MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MULTIPLICAR MUT NEW NOT OR PARENTESISDERECHO PARENTESISIZQUIERDO PORCENTAJE POW PRINTLN PUNTO PUNTOCOMA PUSH REMOVE RETURN SQRT STRING TIPORETURN TRUE USIZE WHAT WHILE WITH_CAPACITY inicio : instrucciones  instrucciones : instrucciones instruccion  instrucciones : instruccion  instruccion : imprimir  \n                    | variable \n                    | asignacion\n                    | instruccionif\n                    | instruccionWhile   imprimir : PRINTLN PARENTESISIZQUIERDO exp PARENTESISDERECHO PUNTOCOMA   variable   :   LET MUT ID DOSPUNTOS tipo IGUAL exp PUNTOCOMA    variable   :   LET MUT ID IGUAL exp PUNTOCOMA    variable   :   LET ID DOSPUNTOS tipo IGUAL exp PUNTOCOMA    variable   :   LET ID IGUAL exp PUNTOCOMA   asignacion : ID IGUAL exp PUNTOCOMA  instruccionif : IF exp LLAVEIZQUIERDO   instrucciones   LLAVEDERECHO  instruccionElse instruccionElse : ELSE LLAVEIZQUIERDO instrucciones LLAVEDERECHO  instruccionElse : ELSE instruccionif\n                        |  instruccionWhile : WHILE exp LLAVEIZQUIERDO instrucciones LLAVEDERECHO   tipo   :   I64\n                |   F64 \n                |   BOOL \n                |   STRING\n                |   CARACTER   exp : exp MAS exp \n            | exp MENOS exp \n            | exp MULTIPLICAR exp \n            | exp DIV exp\n            | exp MAYOR exp \n            | exp MENOR exp \n            | exp MAYORIGUAL exp \n            | exp MENORIGUAL exp \n            | exp IGUALDAD exp\n            | exp DIFERENTE exp\n            | exp OR exp\n            | exp AND exp  exp :   exp AS I64 \n        exp :   exp AS F64    exp : NOT exp %prec UNOT  exp : MENOS exp %prec UMENOS  exp : PARENTESISIZQUIERDO exp PARENTESISDERECHO  exp : I64 DOSPUNTOS DOSPUNTOS POW PARENTESISIZQUIERDO exp COMA exp PARENTESISDERECHO \n            | F64 DOSPUNTOS DOSPUNTOS POW PARENTESISIZQUIERDO exp COMA exp PARENTESISDERECHO  exp : primitivo  primitivo   : ENTERO \n                    | DECIMAL\n                    | TRUE\n                    | FALSE\n                    | CADENA\n                    | CARACTER \n                    | ID '
    
_lr_action_items = {'PRINTLN':([0,2,3,4,5,6,7,8,14,39,58,69,70,88,89,93,94,97,99,101,106,107,108,111,112,115,],[9,9,-3,-4,-5,-6,-7,-8,-2,9,9,-14,9,9,-9,-13,-18,-19,-11,-15,-12,9,-17,-10,9,-16,]),'LET':([0,2,3,4,5,6,7,8,14,39,58,69,70,88,89,93,94,97,99,101,106,107,108,111,112,115,],[10,10,-3,-4,-5,-6,-7,-8,-2,10,10,-14,10,10,-9,-13,-18,-19,-11,-15,-12,10,-17,-10,10,-16,]),'ID':([0,2,3,4,5,6,7,8,10,12,13,14,15,16,18,20,23,24,37,39,40,41,42,43,44,45,46,47,48,49,50,51,58,61,69,70,88,89,92,93,94,97,98,99,101,103,104,106,107,108,111,112,113,114,115,],[11,11,-3,-4,-5,-6,-7,-8,17,32,32,-2,32,35,32,32,32,32,32,11,32,32,32,32,32,32,32,32,32,32,32,32,11,32,-14,11,11,-9,32,-13,-18,-19,32,-11,-15,32,32,-12,11,-17,-10,11,32,32,-16,]),'IF':([0,2,3,4,5,6,7,8,14,39,58,69,70,88,89,93,94,97,99,101,102,106,107,108,111,112,115,],[12,12,-3,-4,-5,-6,-7,-8,-2,12,12,-14,12,12,-9,-13,-18,-19,-11,-15,12,-12,12,-17,-10,12,-16,]),'WHILE':([0,2,3,4,5,6,7,8,14,39,58,69,70,88,89,93,94,97,99,101,106,107,108,111,112,115,],[13,13,-3,-4,-5,-6,-7,-8,-2,13,13,-14,13,13,-9,-13,-18,-19,-11,-15,-12,13,-17,-10,13,-16,]),'$end':([1,2,3,4,5,6,7,8,14,69,89,93,94,97,99,101,106,108,111,115,],[0,-1,-3,-4,-5,-6,-7,-8,-2,-14,-9,-13,-18,-19,-11,-15,-12,-17,-10,-16,]),'LLAVEDERECHO':([3,4,5,6,7,8,14,69,70,88,89,93,94,97,99,101,106,108,111,112,115,],[-3,-4,-5,-6,-7,-8,-2,-14,94,97,-9,-13,-18,-19,-11,-15,-12,-17,-10,115,-16,]),'PARENTESISIZQUIERDO':([9,12,13,15,18,20,23,24,37,40,41,42,43,44,45,46,47,48,49,50,51,61,92,95,96,98,103,104,113,114,],[15,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,103,104,24,24,24,24,24,]),'MUT':([10,],[16,]),'IGUAL':([11,17,35,62,63,64,65,66,67,90,],[18,37,61,92,-20,-21,-22,-23,-24,98,]),'NOT':([12,13,15,18,20,23,24,37,40,41,42,43,44,45,46,47,48,49,50,51,61,92,98,103,104,113,114,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'MENOS':([12,13,15,18,19,20,23,24,25,26,27,28,29,30,31,32,33,34,37,38,40,41,42,43,44,45,46,47,48,49,50,51,53,56,57,61,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,92,98,100,103,104,105,109,110,113,114,116,117,118,119,],[20,20,20,20,41,20,20,20,-44,-45,-46,-47,-48,-49,-50,-51,41,41,20,41,20,20,20,20,20,20,20,20,20,20,20,20,-40,41,41,20,41,-25,-26,-27,-28,41,41,41,41,41,41,41,41,-37,-38,-41,41,20,20,41,20,20,41,41,41,20,20,41,41,-42,-43,]),'I64':([12,13,15,18,20,23,24,36,37,40,41,42,43,44,45,46,47,48,49,50,51,52,60,61,92,98,103,104,113,114,],[21,21,21,21,21,21,21,63,21,21,21,21,21,21,21,21,21,21,21,21,21,83,63,21,21,21,21,21,21,21,]),'F64':([12,13,15,18,20,23,24,36,37,40,41,42,43,44,45,46,47,48,49,50,51,52,60,61,92,98,103,104,113,114,],[22,22,22,22,22,22,22,64,22,22,22,22,22,22,22,22,22,22,22,22,22,84,64,22,22,22,22,22,22,22,]),'ENTERO':([12,13,15,18,20,23,24,37,40,41,42,43,44,45,46,47,48,49,50,51,61,92,98,103,104,113,114,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'DECIMAL':([12,13,15,18,20,23,24,37,40,41,42,43,44,45,46,47,48,49,50,51,61,92,98,103,104,113,114,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'TRUE':([12,13,15,18,20,23,24,37,40,41,42,43,44,45,46,47,48,49,50,51,61,92,98,103,104,113,114,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'FALSE':([12,13,15,18,20,23,24,37,40,41,42,43,44,45,46,47,48,49,50,51,61,92,98,103,104,113,114,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'CADENA':([12,13,15,18,20,23,24,37,40,41,42,43,44,45,46,47,48,49,50,51,61,92,98,103,104,113,114,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'CARACTER':([12,13,15,18,20,23,24,36,37,40,41,42,43,44,45,46,47,48,49,50,51,60,61,92,98,103,104,113,114,],[31,31,31,31,31,31,31,67,31,31,31,31,31,31,31,31,31,31,31,31,31,67,31,31,31,31,31,31,31,]),'DOSPUNTOS':([17,21,22,35,54,55,],[36,54,55,60,85,86,]),'LLAVEIZQUIERDO':([19,25,26,27,28,29,30,31,32,33,53,56,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,102,118,119,],[39,-44,-45,-46,-47,-48,-49,-50,-51,58,-40,-39,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-41,107,-42,-43,]),'MAS':([19,25,26,27,28,29,30,31,32,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,109,110,116,117,118,119,],[40,-44,-45,-46,-47,-48,-49,-50,-51,40,40,40,-40,40,40,40,-25,-26,-27,-28,40,40,40,40,40,40,40,40,-37,-38,-41,40,40,40,40,40,40,40,-42,-43,]),'MULTIPLICAR':([19,25,26,27,28,29,30,31,32,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,109,110,116,117,118,119,],[42,-44,-45,-46,-47,-48,-49,-50,-51,42,42,42,-40,42,42,42,42,42,-27,-28,42,42,42,42,42,42,42,42,-37,-38,-41,42,42,42,42,42,42,42,-42,-43,]),'DIV':([19,25,26,27,28,29,30,31,32,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,109,110,116,117,118,119,],[43,-44,-45,-46,-47,-48,-49,-50,-51,43,43,43,-40,43,43,43,43,43,-27,-28,43,43,43,43,43,43,43,43,-37,-38,-41,43,43,43,43,43,43,43,-42,-43,]),'MAYOR':([19,25,26,27,28,29,30,31,32,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,109,110,116,117,118,119,],[44,-44,-45,-46,-47,-48,-49,-50,-51,44,44,44,-40,44,44,44,-25,-26,-27,-28,-29,-30,-31,-32,44,44,44,44,-37,-38,-41,44,44,44,44,44,44,44,-42,-43,]),'MENOR':([19,25,26,27,28,29,30,31,32,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,109,110,116,117,118,119,],[45,-44,-45,-46,-47,-48,-49,-50,-51,45,45,45,-40,45,45,45,-25,-26,-27,-28,-29,-30,-31,-32,45,45,45,45,-37,-38,-41,45,45,45,45,45,45,45,-42,-43,]),'MAYORIGUAL':([19,25,26,27,28,29,30,31,32,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,109,110,116,117,118,119,],[46,-44,-45,-46,-47,-48,-49,-50,-51,46,46,46,-40,46,46,46,-25,-26,-27,-28,-29,-30,-31,-32,46,46,46,46,-37,-38,-41,46,46,46,46,46,46,46,-42,-43,]),'MENORIGUAL':([19,25,26,27,28,29,30,31,32,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,109,110,116,117,118,119,],[47,-44,-45,-46,-47,-48,-49,-50,-51,47,47,47,-40,47,47,47,-25,-26,-27,-28,-29,-30,-31,-32,47,47,47,47,-37,-38,-41,47,47,47,47,47,47,47,-42,-43,]),'IGUALDAD':([19,25,26,27,28,29,30,31,32,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,109,110,116,117,118,119,],[48,-44,-45,-46,-47,-48,-49,-50,-51,48,48,48,-40,48,48,48,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,48,48,-37,-38,-41,48,48,48,48,48,48,48,-42,-43,]),'DIFERENTE':([19,25,26,27,28,29,30,31,32,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,109,110,116,117,118,119,],[49,-44,-45,-46,-47,-48,-49,-50,-51,49,49,49,-40,49,49,49,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,49,49,-37,-38,-41,49,49,49,49,49,49,49,-42,-43,]),'OR':([19,25,26,27,28,29,30,31,32,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,109,110,116,117,118,119,],[50,-44,-45,-46,-47,-48,-49,-50,-51,50,50,50,-40,-39,50,50,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-41,50,50,50,50,50,50,50,-42,-43,]),'AND':([19,25,26,27,28,29,30,31,32,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,109,110,116,117,118,119,],[51,-44,-45,-46,-47,-48,-49,-50,-51,51,51,51,-40,-39,51,51,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,51,-36,-37,-38,-41,51,51,51,51,51,51,51,-42,-43,]),'AS':([19,25,26,27,28,29,30,31,32,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,109,110,116,117,118,119,],[52,-44,-45,-46,-47,-48,-49,-50,-51,52,52,52,-40,-39,52,52,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-41,52,52,52,52,52,52,52,-42,-43,]),'PARENTESISDERECHO':([25,26,27,28,29,30,31,32,34,53,56,57,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,116,117,118,119,],[-44,-45,-46,-47,-48,-49,-50,-51,59,-40,-39,87,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-41,118,119,-42,-43,]),'PUNTOCOMA':([25,26,27,28,29,30,31,32,38,53,56,59,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,91,100,105,118,119,],[-44,-45,-46,-47,-48,-49,-50,-51,69,-40,-39,89,93,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-41,99,106,111,-42,-43,]),'COMA':([25,26,27,28,29,30,31,32,53,56,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,109,110,118,119,],[-44,-45,-46,-47,-48,-49,-50,-51,-40,-39,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-41,113,114,-42,-43,]),'BOOL':([36,60,],[65,65,]),'STRING':([36,60,],[66,66,]),'POW':([85,86,],[95,96,]),'ELSE':([94,],[102,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'instrucciones':([0,39,58,107,],[2,70,88,112,]),'instruccion':([0,2,39,58,70,88,107,112,],[3,14,3,3,14,14,3,14,]),'imprimir':([0,2,39,58,70,88,107,112,],[4,4,4,4,4,4,4,4,]),'variable':([0,2,39,58,70,88,107,112,],[5,5,5,5,5,5,5,5,]),'asignacion':([0,2,39,58,70,88,107,112,],[6,6,6,6,6,6,6,6,]),'instruccionif':([0,2,39,58,70,88,102,107,112,],[7,7,7,7,7,7,108,7,7,]),'instruccionWhile':([0,2,39,58,70,88,107,112,],[8,8,8,8,8,8,8,8,]),'exp':([12,13,15,18,20,23,24,37,40,41,42,43,44,45,46,47,48,49,50,51,61,92,98,103,104,113,114,],[19,33,34,38,53,56,57,68,71,72,73,74,75,76,77,78,79,80,81,82,91,100,105,109,110,116,117,]),'primitivo':([12,13,15,18,20,23,24,37,40,41,42,43,44,45,46,47,48,49,50,51,61,92,98,103,104,113,114,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'tipo':([36,60,],[62,90,]),'instruccionElse':([94,],[101,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> instrucciones','inicio',1,'p_inicio','Sintactico.py',81),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_lista_instrucciones','Sintactico.py',93),
  ('instrucciones -> instruccion','instrucciones',1,'p_intrucciones','Sintactico.py',99),
  ('instruccion -> imprimir','instruccion',1,'p_instruccion','Sintactico.py',113),
  ('instruccion -> variable','instruccion',1,'p_instruccion','Sintactico.py',114),
  ('instruccion -> asignacion','instruccion',1,'p_instruccion','Sintactico.py',115),
  ('instruccion -> instruccionif','instruccion',1,'p_instruccion','Sintactico.py',116),
  ('instruccion -> instruccionWhile','instruccion',1,'p_instruccion','Sintactico.py',117),
  ('imprimir -> PRINTLN PARENTESISIZQUIERDO exp PARENTESISDERECHO PUNTOCOMA','imprimir',5,'p_imprimir','Sintactico.py',133),
  ('variable -> LET MUT ID DOSPUNTOS tipo IGUAL exp PUNTOCOMA','variable',8,'p_variables_mut_tipo','Sintactico.py',153),
  ('variable -> LET MUT ID IGUAL exp PUNTOCOMA','variable',6,'p_variables_mut','Sintactico.py',163),
  ('variable -> LET ID DOSPUNTOS tipo IGUAL exp PUNTOCOMA','variable',7,'p_variables_tipo','Sintactico.py',174),
  ('variable -> LET ID IGUAL exp PUNTOCOMA','variable',5,'p_variables','Sintactico.py',184),
  ('asignacion -> ID IGUAL exp PUNTOCOMA','asignacion',4,'p_asignacion_variables','Sintactico.py',206),
  ('instruccionif -> IF exp LLAVEIZQUIERDO instrucciones LLAVEDERECHO instruccionElse','instruccionif',6,'p_instruccion_if','Sintactico.py',229),
  ('instruccionElse -> ELSE LLAVEIZQUIERDO instrucciones LLAVEDERECHO','instruccionElse',4,'p_instruccion_else','Sintactico.py',239),
  ('instruccionElse -> ELSE instruccionif','instruccionElse',2,'p_instruccion_else_if','Sintactico.py',249),
  ('instruccionElse -> <empty>','instruccionElse',0,'p_instruccion_else_if','Sintactico.py',250),
  ('instruccionWhile -> WHILE exp LLAVEIZQUIERDO instrucciones LLAVEDERECHO','instruccionWhile',5,'p_instruccion_while','Sintactico.py',272),
  ('tipo -> I64','tipo',1,'p_tipos','Sintactico.py',292),
  ('tipo -> F64','tipo',1,'p_tipos','Sintactico.py',293),
  ('tipo -> BOOL','tipo',1,'p_tipos','Sintactico.py',294),
  ('tipo -> STRING','tipo',1,'p_tipos','Sintactico.py',295),
  ('tipo -> CARACTER','tipo',1,'p_tipos','Sintactico.py',296),
  ('exp -> exp MAS exp','exp',3,'p_aritmetica','Sintactico.py',330),
  ('exp -> exp MENOS exp','exp',3,'p_aritmetica','Sintactico.py',331),
  ('exp -> exp MULTIPLICAR exp','exp',3,'p_aritmetica','Sintactico.py',332),
  ('exp -> exp DIV exp','exp',3,'p_aritmetica','Sintactico.py',333),
  ('exp -> exp MAYOR exp','exp',3,'p_aritmetica','Sintactico.py',334),
  ('exp -> exp MENOR exp','exp',3,'p_aritmetica','Sintactico.py',335),
  ('exp -> exp MAYORIGUAL exp','exp',3,'p_aritmetica','Sintactico.py',336),
  ('exp -> exp MENORIGUAL exp','exp',3,'p_aritmetica','Sintactico.py',337),
  ('exp -> exp IGUALDAD exp','exp',3,'p_aritmetica','Sintactico.py',338),
  ('exp -> exp DIFERENTE exp','exp',3,'p_aritmetica','Sintactico.py',339),
  ('exp -> exp OR exp','exp',3,'p_aritmetica','Sintactico.py',340),
  ('exp -> exp AND exp','exp',3,'p_aritmetica','Sintactico.py',341),
  ('exp -> exp AS I64','exp',3,'p_casteos','Sintactico.py',404),
  ('exp -> exp AS F64','exp',3,'p_casteos','Sintactico.py',405),
  ('exp -> NOT exp','exp',2,'p_logica_unitaria','Sintactico.py',420),
  ('exp -> MENOS exp','exp',2,'p_aritmetica_unaria','Sintactico.py',425),
  ('exp -> PARENTESISIZQUIERDO exp PARENTESISDERECHO','exp',3,'p_aritmetica_agrupacion','Sintactico.py',433),
  ('exp -> I64 DOSPUNTOS DOSPUNTOS POW PARENTESISIZQUIERDO exp COMA exp PARENTESISDERECHO','exp',9,'p_aritmetica_potencia','Sintactico.py',441),
  ('exp -> F64 DOSPUNTOS DOSPUNTOS POW PARENTESISIZQUIERDO exp COMA exp PARENTESISDERECHO','exp',9,'p_aritmetica_potencia','Sintactico.py',442),
  ('exp -> primitivo','exp',1,'p_expresion','Sintactico.py',453),
  ('primitivo -> ENTERO','primitivo',1,'p_valor','Sintactico.py',473),
  ('primitivo -> DECIMAL','primitivo',1,'p_valor','Sintactico.py',474),
  ('primitivo -> TRUE','primitivo',1,'p_valor','Sintactico.py',475),
  ('primitivo -> FALSE','primitivo',1,'p_valor','Sintactico.py',476),
  ('primitivo -> CADENA','primitivo',1,'p_valor','Sintactico.py',477),
  ('primitivo -> CARACTER','primitivo',1,'p_valor','Sintactico.py',478),
  ('primitivo -> ID','primitivo',1,'p_valor','Sintactico.py',479),
]
