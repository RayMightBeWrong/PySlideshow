grammar = '''
start: config? vars? slides
config: "config" "=" "{" config_content "}"
vars: var+ 
slides: "start" content*  "end"

config_content: config_attr ("," config_attr)*
config_attr: WORD ":" NR

varcall: "#" WORD
var: varcall "=" attr_content
rgb: "(" NR "," NR "," NR ")"
    | "0" "x" HEXWORD 

content: tag content+ endc 
    | slide
tag: tagname taginfo 
tagname: DURATION | TEXT | IMG 
taginfo: "(" attr ("," attr)* ")"
attr: WORD "=" attr_content
attr_content: varcall
    | type

type : rgb
    | ESCAPED_STRING
    | NR
    | BOOL

slide: "slide"
endc: "."



DURATION: "duration"
TEXT: "text"
IMG: "img"

HEXWORD: HEXDIGIT+
NR: ("+" | "-")? NUMBER 
BOOL: TRUE | FALSE
TRUE: "TRUE"
FALSE: "FALSE"

%import common.WS
%import common.NUMBER
%import common.WORD
%import common.HEXDIGIT
%import common.ESCAPED_STRING
%ignore WS
'''
