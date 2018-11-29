
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ADDASS ALIAS AND ANDLOG ASS BEGIN BOOLEAN BREAK CASE CLASS CLASSVAR COMA CONSTANTS DEF DEFINED DIV DIVASS DO DOBLEPOINT DOUBLESECUENCEPOINT ELSE ELSIF END ENSURE EQUAL ERROR EXP EXPASS FALSE FILE FLOAT FOR GLOBAL GREATHER GREATHEREQ IF IN INSTANCEVAR INT LBRACK LINE LOCAL LOWER LOWEREQ MOD MODASS MODULE MUL MULASS NEWLINE NEXT NIL NOT NOTEQ NOTLOG NUMBER OR ORLOG PSEUDO RBRACK REDO RESCUE RETRY RETURN SELF STRING SUB SUBASS SUPER THEN TRUE UNDEF UNLESS UNTIL WHEN WHILE YIELDwhile : WHILE logical code END\n             | WHILE logical DO salto code salto END\n             | WHILE logical DOBLEPOINT salto code salto END\n             | BEGIN code END WHILE logicalassign : variable ASS expr\n              | variable ASS sexpr\n              | variable ASS arraymath : term arith term\n            | term arith math\n            | variable asig termlogical : term comparison term\n               | term comparison logical\n               | variable comparison term\n               | variable comparison BOOLEAN\n               | logical logcompare logical\n               | BOOLEANvariable : LOCAL\n                | GLOBAL \n                | CONSTANTS \n                | INSTANCEVAR \n                | CLASSVARasig : ASS\n            | ADDASS\n            | SUBASS\n            | MULASS\n            | DIVASS\n            | MODASS\n            | EXPASSexpr :  math\n             | term\n             | variable\n             | assign\n             | array\n             | slice\n             | indexsexpr : sterm MUL term\n             | sterm ADD sexpr\n             | stermterm : NUMBERsterm : STRINGarith : EXP\n             | MUL\n             | DIV\n             | MOD\n             | ADD\n             | SUBcomparison : EQUAL\n                  | NOTEQ\n                  | GREATHER\n                  | LOWER\n                  | GREATHEREQ\n                  | LOWEREQlogcompare : ANDLOG\n                  | ORLOG\n                  | NOTLOG\n                  | AND\n                  | OR\n                  | NOTsalto : NEWLINE if : IF logical expr END\n          | IF logical THEN expr END\n          | IF logical\n          | IF logical THEN\n          | if else\n          | if elsif ENDelse : ELSE expr ENDelsif : ELSIF logical finalfinal : expr\n             | THEN expr\n             | expr else\n             | expr elsif code : expr\n            | if\n            | while\n            | expresiones\n            | for\n            | assign\n            | math\n            | code codeiterador : variable\n                | variable "," variableexpresiones : term DOUBLESECUENCEPOINT termfor : FOR iterador IN expresiones code END\n           | FOR iterador IN expresiones DO code END\n           | FOR iterador IN array code END\n           | FOR iterador IN array DO code ENDarray : LBRACK defarray RBRACKdefarray : NUMBER \n                | NUMBER COMA defarray\n                | STRING\n                | STRING COMA defarray\n                | INT\n                | INT COMA defarray\n                | FLOAT\n                | FLOAT COMA defarray\n                | BOOLEAN\n                | BOOLEAN COMA defarrayindex : variable LBRACK INT RBRACKslice : variable LBRACK defslice RBRACKdefslice : INT DOBLEPOINT INT\n                    | INT DOBLEPOINT\n                    | DOBLEPOINT INT'
    
_lr_action_items = {'WHILE':([0,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,30,48,49,50,71,80,81,82,83,84,85,86,87,88,90,92,93,94,95,97,98,99,101,102,103,104,105,106,111,114,120,121,122,123,130,131,134,136,137,150,151,153,154,155,156,157,158,159,160,161,162,163,164,165,],[2,2,2,-16,-39,-17,-18,-19,-20,-21,2,-72,-73,-74,-75,-76,-32,-29,-30,-31,-33,-34,-35,2,2,89,-64,-62,-1,2,-59,2,-15,-11,-12,-13,-14,-65,-29,-30,-31,-32,-82,-8,-9,-5,-6,-7,-38,-40,-10,-63,-87,2,2,-4,-66,-99,-98,-60,2,2,-36,-37,-61,2,2,2,2,-2,-3,-83,2,-85,2,-84,-86,]),'BEGIN':([0,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,30,48,50,71,80,81,82,83,84,85,86,87,88,90,92,93,94,95,97,98,99,101,102,103,104,105,106,111,114,120,121,122,123,130,131,134,136,137,150,151,153,154,155,156,157,158,159,160,161,162,163,164,165,],[3,3,3,-16,-39,-17,-18,-19,-20,-21,3,-72,-73,-74,-75,-76,-32,-29,-30,-31,-33,-34,-35,3,3,-64,-62,-1,3,-59,3,-15,-11,-12,-13,-14,-65,-29,-30,-31,-32,-82,-8,-9,-5,-6,-7,-38,-40,-10,-63,-87,3,3,-4,-66,-99,-98,-60,3,3,-36,-37,-61,3,3,3,3,-2,-3,-83,3,-85,3,-84,-86,]),'$end':([1,7,8,80,84,85,86,87,88,122,158,159,],[0,-16,-39,-1,-15,-11,-12,-13,-14,-4,-2,-3,]),'BOOLEAN':([2,27,29,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,89,115,116,117,118,119,],[7,7,79,7,-53,-54,-55,-56,-57,-58,7,-47,-48,-49,-50,-51,-52,88,7,7,79,79,79,79,79,]),'NUMBER':([2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,68,69,70,71,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99,101,102,103,104,105,106,111,112,114,115,116,117,118,119,120,121,122,123,126,127,128,130,131,134,136,137,150,151,153,154,155,156,157,158,159,160,161,162,163,164,165,],[8,8,8,-16,-39,-17,-18,-19,-20,-21,8,-72,-73,-74,-75,-76,-32,-29,-30,-31,-33,-34,-35,8,75,8,8,-53,-54,-55,-56,-57,-58,8,-47,-48,-49,-50,-51,-52,8,8,-64,8,8,8,8,-41,-42,-43,-44,-45,-46,8,8,-23,-24,-25,-26,-27,-28,8,-1,8,-59,8,-15,-11,-12,-13,-14,8,-65,-29,-30,-31,-32,8,-82,-8,-9,-5,-6,-7,-38,-40,-10,8,8,-87,75,75,75,75,75,8,8,-4,-66,8,-22,8,-99,-98,-60,8,8,-36,-37,-61,8,8,8,8,-2,-3,-83,8,-85,8,-84,-86,]),'LOCAL':([2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,50,52,53,55,56,57,58,59,60,61,62,71,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99,101,102,103,104,105,106,111,113,114,120,121,122,123,126,130,131,134,136,137,150,151,153,154,155,156,157,158,159,160,161,162,163,164,165,],[9,9,9,-16,-39,-17,-18,-19,-20,-21,9,-72,-73,-74,-75,-76,-32,-29,-30,-31,-33,-34,-35,9,9,9,9,-53,-54,-55,-56,-57,-58,9,-47,-48,-49,-50,-51,-52,9,-64,9,9,9,-41,-42,-43,-44,-45,-46,9,9,-1,9,-59,9,-15,-11,-12,-13,-14,9,-65,-29,-30,-31,-32,9,-82,-8,-9,-5,-6,-7,-38,-40,-10,9,9,-87,9,9,-4,-66,9,-99,-98,-60,9,9,-36,-37,-61,9,9,9,9,-2,-3,-83,9,-85,9,-84,-86,]),'GLOBAL':([2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,50,52,53,55,56,57,58,59,60,61,62,71,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99,101,102,103,104,105,106,111,113,114,120,121,122,123,126,130,131,134,136,137,150,151,153,154,155,156,157,158,159,160,161,162,163,164,165,],[10,10,10,-16,-39,-17,-18,-19,-20,-21,10,-72,-73,-74,-75,-76,-32,-29,-30,-31,-33,-34,-35,10,10,10,10,-53,-54,-55,-56,-57,-58,10,-47,-48,-49,-50,-51,-52,10,-64,10,10,10,-41,-42,-43,-44,-45,-46,10,10,-1,10,-59,10,-15,-11,-12,-13,-14,10,-65,-29,-30,-31,-32,10,-82,-8,-9,-5,-6,-7,-38,-40,-10,10,10,-87,10,10,-4,-66,10,-99,-98,-60,10,10,-36,-37,-61,10,10,10,10,-2,-3,-83,10,-85,10,-84,-86,]),'CONSTANTS':([2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,50,52,53,55,56,57,58,59,60,61,62,71,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99,101,102,103,104,105,106,111,113,114,120,121,122,123,126,130,131,134,136,137,150,151,153,154,155,156,157,158,159,160,161,162,163,164,165,],[11,11,11,-16,-39,-17,-18,-19,-20,-21,11,-72,-73,-74,-75,-76,-32,-29,-30,-31,-33,-34,-35,11,11,11,11,-53,-54,-55,-56,-57,-58,11,-47,-48,-49,-50,-51,-52,11,-64,11,11,11,-41,-42,-43,-44,-45,-46,11,11,-1,11,-59,11,-15,-11,-12,-13,-14,11,-65,-29,-30,-31,-32,11,-82,-8,-9,-5,-6,-7,-38,-40,-10,11,11,-87,11,11,-4,-66,11,-99,-98,-60,11,11,-36,-37,-61,11,11,11,11,-2,-3,-83,11,-85,11,-84,-86,]),'INSTANCEVAR':([2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,50,52,53,55,56,57,58,59,60,61,62,71,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99,101,102,103,104,105,106,111,113,114,120,121,122,123,126,130,131,134,136,137,150,151,153,154,155,156,157,158,159,160,161,162,163,164,165,],[12,12,12,-16,-39,-17,-18,-19,-20,-21,12,-72,-73,-74,-75,-76,-32,-29,-30,-31,-33,-34,-35,12,12,12,12,-53,-54,-55,-56,-57,-58,12,-47,-48,-49,-50,-51,-52,12,-64,12,12,12,-41,-42,-43,-44,-45,-46,12,12,-1,12,-59,12,-15,-11,-12,-13,-14,12,-65,-29,-30,-31,-32,12,-82,-8,-9,-5,-6,-7,-38,-40,-10,12,12,-87,12,12,-4,-66,12,-99,-98,-60,12,12,-36,-37,-61,12,12,12,12,-2,-3,-83,12,-85,12,-84,-86,]),'CLASSVAR':([2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,50,52,53,55,56,57,58,59,60,61,62,71,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99,101,102,103,104,105,106,111,113,114,120,121,122,123,126,130,131,134,136,137,150,151,153,154,155,156,157,158,159,160,161,162,163,164,165,],[13,13,13,-16,-39,-17,-18,-19,-20,-21,13,-72,-73,-74,-75,-76,-32,-29,-30,-31,-33,-34,-35,13,13,13,13,-53,-54,-55,-56,-57,-58,13,-47,-48,-49,-50,-51,-52,13,-64,13,13,13,-41,-42,-43,-44,-45,-46,13,13,-1,13,-59,13,-15,-11,-12,-13,-14,13,-65,-29,-30,-31,-32,13,-82,-8,-9,-5,-6,-7,-38,-40,-10,13,13,-87,13,13,-4,-66,13,-99,-98,-60,13,13,-36,-37,-61,13,13,13,13,-2,-3,-83,13,-85,13,-84,-86,]),'IF':([3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,30,48,50,71,80,81,82,83,84,85,86,87,88,90,92,93,94,95,97,98,99,101,102,103,104,105,106,111,114,120,121,122,123,130,131,134,136,137,150,151,153,154,155,156,157,158,159,160,161,162,163,164,165,],[27,27,-16,-39,-17,-18,-19,-20,-21,27,-72,-73,-74,-75,-76,-32,-29,-30,-31,-33,-34,-35,27,27,-64,-62,-1,27,-59,27,-15,-11,-12,-13,-14,-65,-29,-30,-31,-32,-82,-8,-9,-5,-6,-7,-38,-40,-10,-63,-87,27,27,-4,-66,-99,-98,-60,27,27,-36,-37,-61,27,27,27,27,-2,-3,-83,27,-85,27,-84,-86,]),'FOR':([3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,30,48,50,71,80,81,82,83,84,85,86,87,88,90,92,93,94,95,97,98,99,101,102,103,104,105,106,111,114,120,121,122,123,130,131,134,136,137,150,151,153,154,155,156,157,158,159,160,161,162,163,164,165,],[28,28,-16,-39,-17,-18,-19,-20,-21,28,-72,-73,-74,-75,-76,-32,-29,-30,-31,-33,-34,-35,28,28,-64,-62,-1,28,-59,28,-15,-11,-12,-13,-14,-65,-29,-30,-31,-32,-82,-8,-9,-5,-6,-7,-38,-40,-10,-63,-87,28,28,-4,-66,-99,-98,-60,28,28,-36,-37,-61,28,28,28,28,-2,-3,-83,28,-85,28,-84,-86,]),'LBRACK':([3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,30,48,50,52,62,71,80,81,82,83,84,85,86,87,88,90,92,93,94,95,96,97,98,99,101,102,103,104,105,106,111,112,114,120,121,122,123,126,130,131,134,136,137,150,151,153,154,155,156,157,158,159,160,161,162,163,164,165,],[29,29,-16,-39,-17,-18,-19,-20,-21,29,-72,-73,-74,-75,-76,-32,-29,-30,64,-33,-34,-35,29,29,-64,29,29,29,-1,29,-59,29,-15,-11,-12,-13,-14,-65,-29,-30,64,-32,29,-82,-8,-9,-5,-6,-7,-38,-40,-10,29,29,-87,29,29,-4,-66,29,-99,-98,-60,29,29,-36,-37,-61,29,29,29,29,-2,-3,-83,29,-85,29,-84,-86,]),'DO':([4,7,8,84,85,86,87,88,97,114,136,137,],[31,-16,-39,-15,-11,-12,-13,-14,-82,-87,155,157,]),'DOBLEPOINT':([4,7,8,64,84,85,86,87,88,108,],[32,-16,-39,109,-15,-11,-12,-13,-14,132,]),'ANDLOG':([4,7,8,71,84,85,86,87,88,96,122,],[34,-16,-39,34,34,-11,34,-13,-14,34,34,]),'ORLOG':([4,7,8,71,84,85,86,87,88,96,122,],[35,-16,-39,35,35,-11,35,-13,-14,35,35,]),'NOTLOG':([4,7,8,71,84,85,86,87,88,96,122,],[36,-16,-39,36,36,-11,36,-13,-14,36,36,]),'AND':([4,7,8,71,84,85,86,87,88,96,122,],[37,-16,-39,37,37,-11,37,-13,-14,37,37,]),'OR':([4,7,8,71,84,85,86,87,88,96,122,],[38,-16,-39,38,38,-11,38,-13,-14,38,38,]),'NOT':([4,7,8,71,84,85,86,87,88,96,122,],[39,-16,-39,39,39,-11,39,-13,-14,39,39,]),'EQUAL':([5,6,8,9,10,11,12,13,85,],[41,41,-39,-17,-18,-19,-20,-21,41,]),'NOTEQ':([5,6,8,9,10,11,12,13,85,],[42,42,-39,-17,-18,-19,-20,-21,42,]),'GREATHER':([5,6,8,9,10,11,12,13,85,],[43,43,-39,-17,-18,-19,-20,-21,43,]),'LOWER':([5,6,8,9,10,11,12,13,85,],[44,44,-39,-17,-18,-19,-20,-21,44,]),'GREATHEREQ':([5,6,8,9,10,11,12,13,85,],[45,45,-39,-17,-18,-19,-20,-21,45,]),'LOWEREQ':([5,6,8,9,10,11,12,13,85,],[46,46,-39,-17,-18,-19,-20,-21,46,]),'THEN':([7,8,71,84,85,86,87,88,96,],[-16,-39,111,-15,-11,-12,-13,-14,126,]),'ELSE':([7,8,9,10,11,12,13,16,24,25,26,50,71,84,85,86,87,88,90,92,93,94,95,98,99,101,102,103,104,105,106,111,114,123,125,130,131,134,150,151,153,],[-16,-39,-17,-18,-19,-20,-21,52,-33,-34,-35,-64,-62,-15,-11,-12,-13,-14,-65,-29,-30,-31,-32,-8,-9,-5,-6,-7,-38,-40,-10,-63,-87,-66,52,-99,-98,-60,-36,-37,-61,]),'ELSIF':([7,8,9,10,11,12,13,16,24,25,26,50,71,84,85,86,87,88,90,92,93,94,95,98,99,101,102,103,104,105,106,111,114,123,125,130,131,134,150,151,153,],[-16,-39,-17,-18,-19,-20,-21,53,-33,-34,-35,-64,-62,-15,-11,-12,-13,-14,-65,-29,-30,-31,-32,-8,-9,-5,-6,-7,-38,-40,-10,-63,-87,-66,53,-99,-98,-60,-36,-37,-61,]),'END':([7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,30,48,50,51,71,80,82,84,85,86,87,88,90,91,92,93,94,95,97,98,99,101,102,103,104,105,106,110,111,114,122,123,124,125,130,131,134,135,145,146,147,148,149,150,151,153,154,156,158,159,160,161,162,163,164,165,],[-16,-39,-17,-18,-19,-20,-21,49,-72,-73,-74,-75,-76,-32,-29,-30,-31,-33,-34,-35,80,-79,-64,90,-62,-1,-59,-15,-11,-12,-13,-14,-65,123,-29,-30,-31,-32,-82,-8,-9,-5,-6,-7,-38,-40,-10,134,-63,-87,-4,-66,-67,-68,-99,-98,-60,153,158,159,-70,-71,-69,-36,-37,-61,160,162,-2,-3,-83,164,-85,165,-84,-86,]),'NEWLINE':([7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,31,32,48,50,71,80,84,85,86,87,88,90,92,93,94,95,97,98,99,101,102,103,104,105,106,111,114,120,121,122,123,130,131,134,150,151,153,158,159,160,162,164,165,],[-16,-39,-17,-18,-19,-20,-21,-72,-73,-74,-75,-76,-32,-29,-30,-31,-33,-34,-35,82,82,-79,-64,-62,-1,-15,-11,-12,-13,-14,-65,-29,-30,-31,-32,-82,-8,-9,-5,-6,-7,-38,-40,-10,-63,-87,82,82,-4,-66,-99,-98,-60,-36,-37,-61,-2,-3,-83,-85,-84,-86,]),'DOUBLESECUENCEPOINT':([8,22,138,],[-39,54,54,]),'EXP':([8,22,93,98,],[-39,56,56,56,]),'MUL':([8,22,93,98,104,105,],[-39,57,57,57,128,-40,]),'DIV':([8,22,93,98,],[-39,58,58,58,]),'MOD':([8,22,93,98,],[-39,59,59,59,]),'ADD':([8,22,93,98,104,105,],[-39,60,60,60,129,-40,]),'SUB':([8,22,93,98,],[-39,61,61,61,]),'ASS':([9,10,11,12,13,23,94,100,],[-17,-18,-19,-20,-21,62,62,127,]),'ADDASS':([9,10,11,12,13,23,94,100,],[-17,-18,-19,-20,-21,65,65,65,]),'SUBASS':([9,10,11,12,13,23,94,100,],[-17,-18,-19,-20,-21,66,66,66,]),'MULASS':([9,10,11,12,13,23,94,100,],[-17,-18,-19,-20,-21,67,67,67,]),'DIVASS':([9,10,11,12,13,23,94,100,],[-17,-18,-19,-20,-21,68,68,68,]),'MODASS':([9,10,11,12,13,23,94,100,],[-17,-18,-19,-20,-21,69,69,69,]),'EXPASS':([9,10,11,12,13,23,94,100,],[-17,-18,-19,-20,-21,70,70,70,]),',':([9,10,11,12,13,73,],[-17,-18,-19,-20,-21,113,]),'IN':([9,10,11,12,13,72,73,139,],[-17,-18,-19,-20,-21,112,-80,-81,]),'STRING':([29,62,115,116,117,118,119,129,],[76,105,76,76,76,76,76,105,]),'INT':([29,64,109,115,116,117,118,119,132,],[77,108,133,77,77,77,77,77,152,]),'FLOAT':([29,115,116,117,118,119,],[78,78,78,78,78,78,]),'RBRACK':([74,75,76,77,78,79,107,108,132,133,140,141,142,143,144,152,],[114,-88,-90,-92,-94,-96,130,131,-101,-102,-89,-91,-93,-95,-97,-100,]),'COMA':([75,76,77,78,79,],[115,116,117,118,119,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'while':([0,3,4,14,30,48,81,83,120,121,136,137,154,155,156,157,161,163,],[1,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'logical':([2,27,33,40,53,89,],[4,71,84,86,96,122,]),'term':([2,3,4,14,27,30,33,40,47,48,52,53,54,55,62,63,71,81,83,89,96,111,112,120,121,126,128,136,137,154,155,156,157,161,163,],[5,22,22,22,5,22,5,85,87,22,93,5,97,98,93,106,93,22,22,5,93,93,138,22,22,93,150,22,22,22,22,22,22,22,22,]),'variable':([2,3,4,14,27,28,30,33,40,48,52,53,55,62,71,81,83,89,96,111,113,120,121,126,136,137,154,155,156,157,161,163,],[6,23,23,23,6,73,23,6,6,23,94,6,100,94,94,23,23,6,94,94,139,23,23,94,23,23,23,23,23,23,23,23,]),'code':([3,4,14,30,48,81,83,120,121,136,137,154,155,156,157,161,163,],[14,30,48,48,48,120,121,48,48,154,156,48,161,48,163,48,48,]),'expr':([3,4,14,30,48,52,62,71,81,83,96,111,120,121,126,136,137,154,155,156,157,161,163,],[15,15,15,15,15,91,101,110,15,15,125,135,15,15,149,15,15,15,15,15,15,15,15,]),'if':([3,4,14,30,48,81,83,120,121,136,137,154,155,156,157,161,163,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'expresiones':([3,4,14,30,48,81,83,112,120,121,136,137,154,155,156,157,161,163,],[18,18,18,18,18,18,18,136,18,18,18,18,18,18,18,18,18,18,]),'for':([3,4,14,30,48,81,83,120,121,136,137,154,155,156,157,161,163,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'assign':([3,4,14,30,48,52,62,71,81,83,96,111,120,121,126,136,137,154,155,156,157,161,163,],[20,20,20,20,20,95,95,95,20,20,95,95,20,20,95,20,20,20,20,20,20,20,20,]),'math':([3,4,14,30,48,52,55,62,71,81,83,96,111,120,121,126,136,137,154,155,156,157,161,163,],[21,21,21,21,21,92,99,92,92,21,21,92,92,21,21,92,21,21,21,21,21,21,21,21,]),'array':([3,4,14,30,48,52,62,71,81,83,96,111,112,120,121,126,136,137,154,155,156,157,161,163,],[24,24,24,24,24,24,103,24,24,24,24,24,137,24,24,24,24,24,24,24,24,24,24,24,]),'slice':([3,4,14,30,48,52,62,71,81,83,96,111,120,121,126,136,137,154,155,156,157,161,163,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'index':([3,4,14,30,48,52,62,71,81,83,96,111,120,121,126,136,137,154,155,156,157,161,163,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'logcompare':([4,71,84,86,96,122,],[33,33,33,33,33,33,]),'comparison':([5,6,85,],[40,47,40,]),'else':([16,125,],[50,147,]),'elsif':([16,125,],[51,148,]),'arith':([22,93,98,],[55,55,55,]),'asig':([23,94,100,],[63,63,63,]),'iterador':([28,],[72,]),'defarray':([29,115,116,117,118,119,],[74,140,141,142,143,144,]),'salto':([31,32,120,121,],[81,83,145,146,]),'sexpr':([62,129,],[102,151,]),'sterm':([62,129,],[104,104,]),'defslice':([64,],[107,]),'final':([96,],[124,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> while","S'",1,None,None,None),
  ('while -> WHILE logical code END','while',4,'p_while','gramarRuby.py',8),
  ('while -> WHILE logical DO salto code salto END','while',7,'p_while','gramarRuby.py',9),
  ('while -> WHILE logical DOBLEPOINT salto code salto END','while',7,'p_while','gramarRuby.py',10),
  ('while -> BEGIN code END WHILE logical','while',5,'p_while','gramarRuby.py',11),
  ('assign -> variable ASS expr','assign',3,'p_assign','gramarRuby.py',20),
  ('assign -> variable ASS sexpr','assign',3,'p_assign','gramarRuby.py',21),
  ('assign -> variable ASS array','assign',3,'p_assign','gramarRuby.py',22),
  ('math -> term arith term','math',3,'p_math','gramarRuby.py',27),
  ('math -> term arith math','math',3,'p_math','gramarRuby.py',28),
  ('math -> variable asig term','math',3,'p_math','gramarRuby.py',29),
  ('logical -> term comparison term','logical',3,'p_logical','gramarRuby.py',33),
  ('logical -> term comparison logical','logical',3,'p_logical','gramarRuby.py',34),
  ('logical -> variable comparison term','logical',3,'p_logical','gramarRuby.py',35),
  ('logical -> variable comparison BOOLEAN','logical',3,'p_logical','gramarRuby.py',36),
  ('logical -> logical logcompare logical','logical',3,'p_logical','gramarRuby.py',37),
  ('logical -> BOOLEAN','logical',1,'p_logical','gramarRuby.py',38),
  ('variable -> LOCAL','variable',1,'p_variable','gramarRuby.py',41),
  ('variable -> GLOBAL','variable',1,'p_variable','gramarRuby.py',42),
  ('variable -> CONSTANTS','variable',1,'p_variable','gramarRuby.py',43),
  ('variable -> INSTANCEVAR','variable',1,'p_variable','gramarRuby.py',44),
  ('variable -> CLASSVAR','variable',1,'p_variable','gramarRuby.py',45),
  ('asig -> ASS','asig',1,'p_asig','gramarRuby.py',49),
  ('asig -> ADDASS','asig',1,'p_asig','gramarRuby.py',50),
  ('asig -> SUBASS','asig',1,'p_asig','gramarRuby.py',51),
  ('asig -> MULASS','asig',1,'p_asig','gramarRuby.py',52),
  ('asig -> DIVASS','asig',1,'p_asig','gramarRuby.py',53),
  ('asig -> MODASS','asig',1,'p_asig','gramarRuby.py',54),
  ('asig -> EXPASS','asig',1,'p_asig','gramarRuby.py',55),
  ('expr -> math','expr',1,'p_expr','gramarRuby.py',59),
  ('expr -> term','expr',1,'p_expr','gramarRuby.py',60),
  ('expr -> variable','expr',1,'p_expr','gramarRuby.py',61),
  ('expr -> assign','expr',1,'p_expr','gramarRuby.py',62),
  ('expr -> array','expr',1,'p_expr','gramarRuby.py',63),
  ('expr -> slice','expr',1,'p_expr','gramarRuby.py',64),
  ('expr -> index','expr',1,'p_expr','gramarRuby.py',65),
  ('sexpr -> sterm MUL term','sexpr',3,'p_sexpr','gramarRuby.py',70),
  ('sexpr -> sterm ADD sexpr','sexpr',3,'p_sexpr','gramarRuby.py',71),
  ('sexpr -> sterm','sexpr',1,'p_sexpr','gramarRuby.py',72),
  ('term -> NUMBER','term',1,'p_term','gramarRuby.py',79),
  ('sterm -> STRING','sterm',1,'p_sterm','gramarRuby.py',83),
  ('arith -> EXP','arith',1,'p_arith','gramarRuby.py',87),
  ('arith -> MUL','arith',1,'p_arith','gramarRuby.py',88),
  ('arith -> DIV','arith',1,'p_arith','gramarRuby.py',89),
  ('arith -> MOD','arith',1,'p_arith','gramarRuby.py',90),
  ('arith -> ADD','arith',1,'p_arith','gramarRuby.py',91),
  ('arith -> SUB','arith',1,'p_arith','gramarRuby.py',92),
  ('comparison -> EQUAL','comparison',1,'p_comparison','gramarRuby.py',97),
  ('comparison -> NOTEQ','comparison',1,'p_comparison','gramarRuby.py',98),
  ('comparison -> GREATHER','comparison',1,'p_comparison','gramarRuby.py',99),
  ('comparison -> LOWER','comparison',1,'p_comparison','gramarRuby.py',100),
  ('comparison -> GREATHEREQ','comparison',1,'p_comparison','gramarRuby.py',101),
  ('comparison -> LOWEREQ','comparison',1,'p_comparison','gramarRuby.py',102),
  ('logcompare -> ANDLOG','logcompare',1,'p_logcompare','gramarRuby.py',106),
  ('logcompare -> ORLOG','logcompare',1,'p_logcompare','gramarRuby.py',107),
  ('logcompare -> NOTLOG','logcompare',1,'p_logcompare','gramarRuby.py',108),
  ('logcompare -> AND','logcompare',1,'p_logcompare','gramarRuby.py',109),
  ('logcompare -> OR','logcompare',1,'p_logcompare','gramarRuby.py',110),
  ('logcompare -> NOT','logcompare',1,'p_logcompare','gramarRuby.py',111),
  ('salto -> NEWLINE','salto',1,'p_salto','gramarRuby.py',118),
  ('if -> IF logical expr END','if',4,'p_if','gramarRuby.py',122),
  ('if -> IF logical THEN expr END','if',5,'p_if','gramarRuby.py',123),
  ('if -> IF logical','if',2,'p_if','gramarRuby.py',124),
  ('if -> IF logical THEN','if',3,'p_if','gramarRuby.py',125),
  ('if -> if else','if',2,'p_if','gramarRuby.py',126),
  ('if -> if elsif END','if',3,'p_if','gramarRuby.py',127),
  ('else -> ELSE expr END','else',3,'p_else','gramarRuby.py',138),
  ('elsif -> ELSIF logical final','elsif',3,'p_elsif','gramarRuby.py',142),
  ('final -> expr','final',1,'p_final','gramarRuby.py',149),
  ('final -> THEN expr','final',2,'p_final','gramarRuby.py',150),
  ('final -> expr else','final',2,'p_final','gramarRuby.py',151),
  ('final -> expr elsif','final',2,'p_final','gramarRuby.py',152),
  ('code -> expr','code',1,'p_code','gramarRuby.py',155),
  ('code -> if','code',1,'p_code','gramarRuby.py',156),
  ('code -> while','code',1,'p_code','gramarRuby.py',157),
  ('code -> expresiones','code',1,'p_code','gramarRuby.py',158),
  ('code -> for','code',1,'p_code','gramarRuby.py',159),
  ('code -> assign','code',1,'p_code','gramarRuby.py',160),
  ('code -> math','code',1,'p_code','gramarRuby.py',161),
  ('code -> code code','code',2,'p_code','gramarRuby.py',162),
  ('iterador -> variable','iterador',1,'p_iterador','gramarRuby.py',168),
  ('iterador -> variable , variable','iterador',3,'p_iterador','gramarRuby.py',169),
  ('expresiones -> term DOUBLESECUENCEPOINT term','expresiones',3,'p_expresiones','gramarRuby.py',173),
  ('for -> FOR iterador IN expresiones code END','for',6,'p_for','gramarRuby.py',177),
  ('for -> FOR iterador IN expresiones DO code END','for',7,'p_for','gramarRuby.py',178),
  ('for -> FOR iterador IN array code END','for',6,'p_for','gramarRuby.py',179),
  ('for -> FOR iterador IN array DO code END','for',7,'p_for','gramarRuby.py',180),
  ('array -> LBRACK defarray RBRACK','array',3,'p_array','gramarRuby.py',185),
  ('defarray -> NUMBER','defarray',1,'p_defarray','gramarRuby.py',189),
  ('defarray -> NUMBER COMA defarray','defarray',3,'p_defarray','gramarRuby.py',190),
  ('defarray -> STRING','defarray',1,'p_defarray','gramarRuby.py',191),
  ('defarray -> STRING COMA defarray','defarray',3,'p_defarray','gramarRuby.py',192),
  ('defarray -> INT','defarray',1,'p_defarray','gramarRuby.py',193),
  ('defarray -> INT COMA defarray','defarray',3,'p_defarray','gramarRuby.py',194),
  ('defarray -> FLOAT','defarray',1,'p_defarray','gramarRuby.py',195),
  ('defarray -> FLOAT COMA defarray','defarray',3,'p_defarray','gramarRuby.py',196),
  ('defarray -> BOOLEAN','defarray',1,'p_defarray','gramarRuby.py',197),
  ('defarray -> BOOLEAN COMA defarray','defarray',3,'p_defarray','gramarRuby.py',198),
  ('index -> variable LBRACK INT RBRACK','index',4,'p_index','gramarRuby.py',203),
  ('slice -> variable LBRACK defslice RBRACK','slice',4,'p_slice','gramarRuby.py',207),
  ('defslice -> INT DOBLEPOINT INT','defslice',3,'p_defslice','gramarRuby.py',211),
  ('defslice -> INT DOBLEPOINT','defslice',2,'p_defslice','gramarRuby.py',212),
  ('defslice -> DOBLEPOINT INT','defslice',2,'p_defslice','gramarRuby.py',213),
]
