import ply.lex as lex

# List of token names
tokens = [
    'A', 'B', 'LPAREN', 'RPAREN'
]

# Regular expression rules for each token
t_A = r'a'
t_B = r'b'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignore spaces, tabs, and newlines
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Optional: test lexer
if __name__ == "__main__":
    while True:
        data = input("Enter string (or 'quit'): ")
        if data.lower() == 'quit':
            break
        lexer.input(data)
        for tok in lexer:
            print(tok)