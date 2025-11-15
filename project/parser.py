import ply.yacc as yacc
from lexer import tokens

# Grammar (simplified & right-recursive so PLY can handle it)
# S -> UNIT S | ε
# UNIT -> a b | ( S )

def p_start(p):
    '''start : seq
             | empty'''
    print("✅ ACCEPTED: String fits grammar (balanced + matching a/b)")

def p_seq(p):
    '''seq : unit seq
           | unit'''
    pass

def p_unit_ab(p):
    'unit : A B'
    pass

def p_unit_paren(p):
    'unit : LPAREN seq RPAREN'
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("❌ REJECTED: Invalid string (fails CFG or PDA rules)")

parser = yacc.yacc(start='start')

if __name__ == "__main__":
    print("Comprehensive Automata Parser (PLY version)")
    print("Alphabet: a, b, (, )")
    print("Type 'quit' to exit.\n")

    while True:
        s = input("Enter string> ").strip()
        if s.lower() in ('quit', 'exit'):
            break
        parser.parse(s)
        print()
