from validation import *

# in this module is stored all the grammar of the calculator. for each operator we define priority level and operand
# sides
ADD = {"type": 'ADD', "level": 1, "func": valid_add}
DIV = {"type": 'DIV', "level": 2, "func": valid_div}
MUL = {"type": 'MUL', "level": 2, "func": valid_mul}
POW = {"type": 'POW', "level": 3, "func": valid_pow}
MODULO = {"type": 'MODUL', "level": 4, "func": valid_modulo}
MAX = {"type": 'MAX', "level": 5, "func": valid_max}
MIN = {"type": 'MIN', "level": 5, "func": valid_min}
AVG = {"type": 'AVG', "level": 5, "func": valid_avg}
FACTORIAL = {"type": 'FACTORIAL', "level": 6, "func": valid_factorial}
SUM_DIGITS = {"type": 'SUM_DIGITS', "level": 6, "func": valid_sum_digits}
TILDA = {"type": 'TILDA', "level": 6, "func": valid_tilda}
RP = {"type": 'RP', "level": 0, "func": None}
LP = {"type": 'LP', "level": 0, "func": None}
BLANKS = [" ", '\v', '\t', '\r']
DU_OPERATORS = {'+': ADD, '/': DIV, '*': MUL, '^': POW, '%': MODULO,
                '$': MAX, '&': MIN, '@': AVG}
R_UN_OPERATORS = {'!': FACTORIAL, '#': SUM_DIGITS}
L_UN_OPERATORS = {'~': TILDA}
UN_OPERATORS = [R_UN_OPERATORS, L_UN_OPERATORS]
MINUS = ['-']
PAR = {'(': LP, ')': RP}
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
TOKENS = [DU_OPERATORS, R_UN_OPERATORS, L_UN_OPERATORS, MINUS, PAR, DIGITS]
