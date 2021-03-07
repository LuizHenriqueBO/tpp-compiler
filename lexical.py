import re
import sys
from ply.lex import lex

class Lexical:

  def __init__(self):
    self.lexer = lex(debug=False, module=self, optimize=False)


  keywords = {
    'inteiro'       : 'INTEIRO',
    'flutuante'     : 'FLUTUANTE',
    'cientifico'    : 'CIENTIFICO',
    'senão'         : 'SENAO',
    'se'            : 'SE',
    'fim'           : 'FIM',
    'repita'        : 'REPITA',
    'até'           : 'ATE',
    'então'         : 'ENTAO',
    'retorna'       : 'RETORNA',
    'leia'          : 'LEIA',
    'escreva'       : 'ESCREVA',
    'texto'         : 'TEXTO',
  }


  tokens = [
    'SOMA',
    'SUBTRACAO',
    'MULTIPLICACAO',
    'DIVISAO',
    'PARENTESES_ESQ',
    'PARENTESES_DIR',
    'ID',
    'DOIS_PONTOS',
    'IGUAL',
    'MAIOR',
    'MENOR',
    'DIFERENTE',
    'MAIOR_IGUAL',
    'MENOR_IGUAL',
    'COLCHETE_DIR',
    'COLCHETE_ESQ',
    'VIRGULA',
    'COMENTARIO',
    'ATRIBUICAO',
    'CARACTERES',
    'NEGACAO',
    'OU_LOGICO',
    'E_LOGICO',
    'NUMERO_INTEIRO',
    'NUMERO_FLOAT',
    'NUMERO_CIENTIFICO',
  ] + list(keywords.values())


  t_SOMA               =  r'\+'
  t_SUBTRACAO          =  r'-'
  t_MULTIPLICACAO      =  r'\*'
  t_DIVISAO            =  r'/'
  t_PARENTESES_ESQ     =  r'\('
  t_PARENTESES_DIR     =  r'\)'
  t_COLCHETE_DIR       =  r'\]'
  t_COLCHETE_ESQ       =  r'\['
  t_VIRGULA            =  r','
  t_DOIS_PONTOS        =  r':'
  t_IGUAL              =  r'='
  t_MAIOR              =  r'>'
  t_MENOR              =  r'<'
  t_DIFERENTE          =  r'<>'
  t_MAIOR_IGUAL        =  r'>='
  t_MENOR_IGUAL        =  r'<='
  t_ATRIBUICAO         =  r':='
  t_CARACTERES         =  r'\"[^\"]*\"'
  t_NEGACAO            =  r'\!'
  t_OU_LOGICO          =  r'\|\|'
  t_E_LOGICO           =  r'\&\&'
  t_NUMERO_INTEIRO     =  r'[+-]?\d+'
  t_NUMERO_FLOAT       =  r'[+-]?\d+\.\d+'
  t_NUMERO_CIENTIFICO  =  r'[+-]?\d+(\.\d+)?[eE][+-]?\d+'


  # get IDs
  def t_ID(self, t):
    r'[a-zA-Zá-ñÁ-Ñ][_a-zA-Zá-ñÁ-Ñ0-9]*'
    t.type = self.keywords.get(t.value, 'ID')
    return t

  # get comments
  def t_COMENTARIO(self, t):
    r'\{[^\}]*\}'


  # Define a rule so we can track line numbers
  def t_newline(self, t):
    r'\n+'
    t.lexer.lineno += len(t.value)


  # A string containing ignored characters (spaces and tabs)
  t_ignore  = ' \t'


  # Error handling rule
  def t_error(self, t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



lexical = Lexical()
File = open(sys.argv[1], encoding="utf-8")
lexical.lexer.input(File.read())


# Tokenize
print()
print("{:^20} {:^20} {:^10} {:^10}".format('type', 'value', 'line', 'position'))

while True:
  tok = lexical.lexer.token()
  if not tok:
    break      # No more input
  print("{:<20} {:^20} {:^10} {:^10}".format(tok.type, tok.value, tok.lineno, tok.lexpos))

print()
print()