# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import logging
import ply.lex as lex
from ply.lex import TOKEN
# List of token names.   This is always required
tokens = (
    'NOTE',
    'INSN',
    'JUMPINSN',
    'CALLINSN',
    'CALL',
    'SYMBOLREF',
    'NIL',
    'PARALLEL',
    'CLOBBER',
    'SET',
    'USE',
    'IFTHENELSE',
    'CONSTINT',
    'BARRIER',
    'MEM',
    'REG',
    'PC',
    'LABELREF',
    'CODELABEL',
    'IFLAG',
    'VFLAG',
    'FFLAG',
    'CFLAG',
    'UFLAG',
    'SITYPE',
    'SFTYPE',
    'DITYPE',
    'QITYPE',
    'TITYPE',
    'CCZTYPE',
    'CCGCTYPE',
    'CCGOCTYPE',
    'CCTYPE',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'UDIV',
    'MOD',
    'UMOD',
    'ASHIFTRT',
    'LSHIFTRT',
    'ASHIFT',
    'LSHIFT',
    'SUBREG',
    'EXPRLIST',
    'SIEXTEND',
    'FLEXTEND',
    'ZEEXTEND',
    'COMPARE',
    'NEG',
    'LTU',
    'GTU',
    'LT',
    'GT',
    'LEU',
    'GEU',
    'LE',
    'GE',
    'EQ',
    'NE',
    'PUNCTUATION',
    'DECIMAL',
    'HEXADECIMAL',
    'INTEGER',
    'IDENTIFIER',
    'STRING',
    'BEGIG1',
    'ENDIG1',
    'BEGIG2',
    'ENDIG2',
    'BEGIG3',
    'ENDIG3',
    'COMM',
    'SKIP',
    'FUNC',
    'ENDPARA',
    'RARROW',
)

states = (
    ('IG1','exclusive'),
    ('IG2','exclusive'),
    ('IG3','exclusive'),
    ('EXPECT','exclusive'),
    ('CATCH','exclusive'),
    ('COMMENT','exclusive'),
)

# Regular expression rules for simple tokens
t_NOTE = r'note' 				
t_INSN=r'insn'				
t_JUMPINSN=r'jump\_insn'		
t_CALLINSN=r'call\_insn' 		
t_CALL=r'call'				
t_SYMBOLREF=r'symbol\_ref'		
t_NIL=r'nil' 				
t_PARALLEL=r'parallel \[' 			
t_CLOBBER=r'clobber' 			
t_SET=r'set' 				
t_USE=r'use' 				
t_IFTHENELSE=r'if\_then\_else' 	
t_CONSTINT=r'const\_int' 		
t_BARRIER=r'barrier'			
t_MEM=r'mem' 				
t_REG=r'reg' 				
t_PC=r'pc' 				
t_LABELREF=r'label\_ref'		
t_CODELABEL=r'code\_label'		
t_IFLAG=r'/i' 				
t_VFLAG=r'/v' 				
t_FFLAG=r'/f' 				
t_CFLAG=r'/c' 				
t_UFLAG=r'/u' 				
t_SITYPE=r'SI' 				
t_SFTYPE=r'SF' 				
t_DITYPE=r'DI' 				
t_QITYPE=r'QI' 				
t_TITYPE=r'TI'				
t_CCZTYPE=r'CCZ' 				
t_CCGCTYPE=r'CCGC' 				
t_CCGOCTYPE=r'CCGOC'				
t_CCTYPE=r'C'				
t_PLUS=r'plus:' 			
t_MINUS=r'minus:' 			
t_MULT=r'mult:'				
t_DIV=r'div:'				
t_UDIV=r'udiv:'				
t_MOD=r'mod:'				
t_UMOD=r'umod:'				
t_ASHIFTRT=r'ashiftrt:'			
t_LSHIFTRT=r'lshiftrt:'			
t_ASHIFT=r'ashift:'			
t_LSHIFT=r'lshift:'			
t_SUBREG=r'subreg:'			
t_EXPRLIST=r'expr_list:'		
t_SIEXTEND=r'sign_extend:'		
t_FLEXTEND=r'float_extend:'		
t_ZEEXTEND=r'zero_extend:'		
t_COMPARE=r'compare:'			
t_NEG=r'neg'				
t_LTU=r'ltu'				
t_GTU=r'gtu'				
t_LT=r'lt' 				
t_GT=r'gt' 				
t_LEU=r'leu'				
t_GEU=r'geu'				
t_LE=r'le' 				
t_GE=r'ge'				
t_EQ=r'eq'				
t_NE=r'ne'	

t_ANY_ignore = ' \t'
PUNCTUATION =  	r'([!:,.()*-])'
DECIMAL     =    r'([0-9]+)'
HEXADECIMAL =    r'(0[xX][0-9a-fA-F]+)'
INTEGER     =    r'('+DECIMAL + r'|' + HEXADECIMAL + r')'
IDENTIFIER  =    r'([a-zA-Z][a-zA-Z0-9_]*)'
STRING 		=	r'(\"[^"\n]*\")'
BEG_IGNORE 	=	r'("\[")'
END_IGNORE 	=	r'("\]")'
BEG_IGNORE2 =    r'("{")'
END_IGNORE2 =    r'("}")'
BEG_IGNORE3 =    r'("<")'
END_IGNORE3 =    r'(">")'
# A regular expression rule with some action code
@TOKEN(PUNCTUATION)
def t_PUNCTUATION(t):
    return t

@TOKEN(STRING)
def t_STRING(t):
    t.value = str(t.value)
    return t

@TOKEN(DECIMAL)
def t_DECIMAL(t):
    t.value = int(t.value)
    return t

@TOKEN(HEXADECIMAL)
def t_HEXADECIMAL(t):
    t.value = int(t.value,16)
    return t

def t_COMM(t):
    r';;'
    t.lexer.begin('EXPECT')
    return t

@TOKEN(BEG_IGNORE)
def t_BEGIG1(t):
    t.lexer.begin('IG1')
    return t

@TOKEN(END_IGNORE)
def t_IG1_ENDIG1(t):
    t.lexer.begin('INITIAL')
    return t

@TOKEN(BEG_IGNORE2)
def t_BEGIG2(t):
    t.lexer.begin('IG2')
    return t

@TOKEN(END_IGNORE2)
def t_IG1_ENDIG2(t):
    t.lexer.begin('INITIAL')
    return t

@TOKEN(BEG_IGNORE3)
def t_BEGIG3(t):
    t.lexer.begin('IG3')
    return t

@TOKEN(END_IGNORE3)
def t_IG1_ENDIG3(t):
    t.lexer.begin('INITIAL')
    return t

t_IG1_ignore_SKIP = r'.'
t_IG2_ignore_SKIP = r'.'
t_IG3_ignore_SKIP = r'.'


def t_EXPECT_FUNC(t):
    r'Function'
    t.lexer.begin('CATCH')
    return t

t_EXPECT_ignore_SKIP = r'.'

def t_EXPECT_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('INITIAL')
    return t

@TOKEN(IDENTIFIER)
def t_CATCH_IDENTIFIER(t):
    t.lexer.begin('COMMENT')
    return t

t_COMMENT_ignore_SKIP = r'.'

def t_COMMENT_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('INITIAL')
    return t
# Define a rule so we can track line numbers
def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ENDPARA=r'\]'
t_RARROW=r'->'
t_ignore_IDENTIFIER=IDENTIFIER
# Error handling rule
def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
# log=logging.getLogger()
lexer = lex.lex()

if __name__ == '__main__':
     lex.runmain()