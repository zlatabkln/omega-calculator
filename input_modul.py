import grammar


# The input module - gets input from user, deletes the blank characters and passes to the lexer

def input_func() -> str:
    try:
        print("This is omega calculator. Please, enter the expression:\n")
        input_from_console = input()
        return clear_expression(input_from_console)
    except EOFError:
        print("EOF in input")
        exit("eof")


# deletes the blank chars from the entered string
def clear_expression(text: str) -> str:
    for c in text:
        if c in grammar.BLANKS:
            text = text.replace(c, '')
    return text
