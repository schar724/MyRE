import ply.yacc as yacc
import sys
from pathlib import Path
import ply.lex as lex
import widget as ws
import nfa as ns

# file = open(Path(__file__).parent/sys.argv[1])


def match(instr, reg):

    
    regex = reg
    input_string = instr

    # Build the lexer
    lexer = lex.lex()

    lexer.input(input_string)
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
    
    # Build the parser
    parser = yacc.yacc()
    
    result = parser.parse(regex)
    success = ws.State(True, [])
    ws.glue(result, success)
    
    nfa = result.start
    
    
    currentState = [nfa]
    
    currentState = ns.epsilonClosure(currentState)
    for char in input_string:
        nextState = []
        for state in currentState:
            for transition in state.transitions:
                if(transition[0] == char):
                    nextState.append(transition[1])
    
        
        nextState = ns.epsilonClosure(nextState)
    
        currentState = nextState


    for state in currentState:
        if(state.success):
            return True
        
    return False

# List of token names.   This is always required
tokens = (
    'LETTER',
    'EPS',
    'OR',
    'STAR',
    'LPAREN',
    'RPAREN',
)

# Regular expression rules for simple tokens
t_OR = r'\|'
t_STAR = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EPS = r'eps'
t_LETTER = r'[abc]'

# A string containing ignored characters (spaces, tabs, newlines)
t_ignore = ' \t\n'



#Even with including this 
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position '{t.lexpos}'")
    exit()








print("Starting yacc...")


def p_E(p):
    'E : E OR T'
    p[0] = ws.or_widget(p[1], p[3])
    # p[0] = Node("E", "E|T", [p[1], Node("OR", "|", []), p[3]] )


def p_E1(p):
    'E : T'
    p[0] = p[1]
    # p[0] = Node("E", "T", [p[1]])


def p_T(p):
    'T : T F'
    p[0] = ws.concat_widget(p[1], p[2])
    # p[0] = Node("T", "TF", [p[1], p[2]])


def p_T1(p):
    'T : F '
    p[0] = p[1]
    # p[0] = Node("T", "F", [p[1]])


def p_F(p):
    'F : LPAREN E RPAREN'
    p[0] = p[2]
#     # p[0] = Node("F", "'(E)'", [Node("LPAREN", "(", []), p[2], Node("RPAREN", ")", [])] )


def p_F1(p):
    'F : F STAR'
    p[0] = ws.star_widget(p[1])
    # p[0] = Node("F", "F*", [p[1], Node("STAR", "*", [])])


def p_F2(p):
    'F : LETTER'
    p[0] = ws.char_widget(p[1])
    # p[0] = Node("F", "LETTER", [Node("LETTER", p[1], [])])


def p_F3(p):
    'F : EPS'
    p[0] = ws.char_widget(p[1])
    # p[0] = Node("F", "EPS", [Node("EPS", "eps", [])])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    exit()