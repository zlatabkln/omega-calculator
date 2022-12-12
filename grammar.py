# in this module is stored all the grammar of the calculator. for each operator we define priority level and operand
# sides
TT_ADD = {"type": 'TT_ADD', "level": 1, "side": "both"}
TT_DIV = {"type": 'TT_DIV', "level": 2, "side": "both"}
TT_MUL = {"type": 'TT_MUL', "level": 2, "side": "both"}
TT_POW = {"type": 'TT_POW', "level": 3, "side": "both"}
TT_MODUL = {"type": 'TT_MODUL', "level": 4, "side": "both"}
TT_MAX = {"type": 'TT_MAX', "level": 5, "side": "both"}
TT_MIN = {"type": 'TT_MIN', "level": 5, "side": "both"}
TT_AVG = {"type": 'TT_AVG', "level": 5, "side": "both"}
TT_FACTORIAL = {"type": 'TT_FACTORIAL', "level": 6, "side": "right"}
TT_COUNT_DIGITS = {"type": 'TT_COUNT_DIGITS', "level": 6, "side": "right"}
TT_TILDA = {"type": 'TT_TILDA', "level": 6, "side": "left"}
TT_RP = {"type": 'TT_RP', "level": -1, "side": "any"}
TT_LP = {"type": 'TT_LP', "level": -2, "side": "any"}

DU_OPERATORS = {'+': TT_ADD, '/': TT_DIV, '*': TT_MUL, '^': TT_POW, '%': TT_MODUL,
                '$': TT_MAX, '&': TT_MIN, '@': TT_AVG}
R_UN_OPERATORS = {'!': TT_FACTORIAL, '#': TT_COUNT_DIGITS}
L_UN_OPERATORS = {'~': TT_TILDA}
MINUS = ['-']
PAR = {'(': TT_RP, ')': TT_LP}
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
TOKENS = [DU_OPERATORS, R_UN_OPERATORS, L_UN_OPERATORS, MINUS, PAR, DIGITS, '.']
