# in this module is stored all the grammar of the calculator. for each operator we define priority level and operand
# sides
ADD = {"type": 'ADD', "level": 1}
DIV = {"type": 'DIV', "level": 2}
MUL = {"type": 'MUL', "level": 2}
POW = {"type": 'POW', "level": 3}
MODULO = {"type": 'MODUL', "level": 4}
MAX = {"type": 'MAX', "level": 5}
MIN = {"type": 'MIN', "level": 5}
AVG = {"type": 'AVG', "level": 5}
FACTORIAL = {"type": 'FACTORIAL', "level": 6}
SUM_DIGITS = {"type": 'SUM_DIGITS', "level": 6}
TILDA = {"type": 'TILDA', "level": 6}
RP = {"type": 'RP', "level": 0}
LP = {"type": 'LP', "level": 0}

DU_OPERATORS = {'+': ADD, '/': DIV, '*': MUL, '^': POW, '%': MODULO,
                '$': MAX, '&': MIN, '@': AVG}
R_UN_OPERATORS = {'!': FACTORIAL, '#': SUM_DIGITS}
L_UN_OPERATORS = {'~': TILDA}
UN_OPERATORS=[R_UN_OPERATORS,L_UN_OPERATORS]
MINUS = ['-']
PAR = {'(': LP, ')': RP}
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
TOKENS = [DU_OPERATORS, R_UN_OPERATORS, L_UN_OPERATORS, MINUS, PAR, DIGITS, '.']
