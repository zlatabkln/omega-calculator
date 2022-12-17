from node_classes import *

# parser will create a tree from token list, when the parent node is the operator, and leaves are operands
# tree is build from last priority(on top) to the highest(bottom)

'''exaple:
1+~2*3 =>  +
          / \
         1   *
            / \
           ~   3
            \
             2'''


class MyParser:
    def __init__(self, tokens):
        self.tokens = tokens  # list of tokens from the lexer
        self.curr_tok = None
        self.prev_tok = None
        self.curr_tok_index = -1
        self.get_next()

    # goes to the next token
    def get_next(self):
        self.curr_tok_index += 1
        if self.curr_tok_index < len(self.tokens):
            self.prev_tok = self.curr_tok
            self.curr_tok = self.tokens[self.curr_tok_index]
        return self.curr_tok

    # token is number or parentheses - converts to number node and deals with expression in parentheses
    def priority_zero(self):
        tok = self.curr_tok
        if tok.level == 0:
            '''parentheses - goes from left to right parentheses and runs over expression between from the lowest 
             priority - 1 '''
            if tok.type in LP.values():
                self.get_next()
                num = self.priority_one()
                if self.curr_tok.type in RP.values():
                    self.get_next()
                    return num
                else:
                    raise AbsentOperatorException("Absent right parentheses")
            else:
                self.get_next()
                return NumNode(tok)

    '''priority functions - start_priority calls for the lowest existing priority function, 
      and she calls for the one higher than her. It goes from 1 to 7,
       and the seventh calls to the zero priority - the highest, number or parentheses. 
       In the end, the created number node goes in reverse, like in recursion, and builds a tree by the way,
       from the highest to lowest priority (in case higher priority is after lower one). If there are still
       any tokens left, we start a new similar cycle with the next one, until we reach to the end'''

    def priority_one(self):
        return self.op_to_tree(self.priority_two, 1)

    def priority_two(self):
        return self.op_to_tree(self.priority_three, 2)

    def priority_three(self):
        return self.op_to_tree(self.priority_four, 3)

    def priority_four(self):
        return self.op_to_tree(self.priority_five, 4)

    def priority_five(self):
        return self.op_to_tree(self.priority_six, 5)

    def priority_six(self):
        return self.op_to_tree(self.priority_seven, 6)

    def priority_seven(self):
        return self.op_to_tree(self.priority_zero, 7)

    '''this function finds the lowest existing priority (so we won't go through priority level functions we don't have
    in expression), calls the matching function and starts the cycle. It also checks if there is any operators at all - 
    if there isn't any, it'll raise an exception'''

    def start_priority(self):
        list_of_priorities = []
        for tok in self.tokens:
            if tok.level not in [-1, -2]:
                list_of_priorities.append(tok.level)
        list_of_priorities.sort(reverse=True)
        max_priority = list_of_priorities[0]
        list_of_priorities = list(filter(lambda x: x != 0, list_of_priorities))
        list_of_priorities.sort()
        min_priority = list_of_priorities[0]
        if max_priority == 0:
            raise AbsentOperatorException(None)
        if min_priority == 1:
            return self.priority_one()
        elif min_priority == 2:
            return self.priority_two()
        elif min_priority == 3:
            return self.priority_three()
        elif min_priority == 4:
            return self.priority_four()
        elif min_priority == 5:
            return self.priority_five()
        elif min_priority == 6:
            return self.priority_six()
        else:
            return self.priority_seven()

    '''this function builds a tree - it's called by every priority function, and creates a tree when the parent node
    is the operator, and the sons are operands (another expression or a number)'''

    def op_to_tree(self, case_function, level):
        left = case_function()
        while self.curr_tok.level == level:
            op_tok = self.curr_tok
            self.get_next()
            right = case_function()
            left = OpNode(left, op_tok, right)
        return left

    # calls the function that builds a tree starting with the lowest priority
    def parse(self):
        tree = self.start_priority()
        return tree
