#!/usr/bin/python3

from lark import Lark
from lark.tree import pydot__tree_to_png
from lark import Transformer
from lark import Discard

def parser():
    stack = []
    def parse_slides(elem):
        if elem[0] == 'slide':
            diff = elem[1] != len(stack)
            for i in range(0, diff):
                stack.pop()
            print('stack: ', stack)
            pass

        else:
            stack.append(elem[0])
            for e in elem[2]:
                parse_slides(e)

    def make_tree(tree, level):
        if tree == 'slide':
            return (tree, level)
        else:
            new_tree = []
            for child in tree[1]:
                new_tree.append(make_tree(child, level + 1))
            return (tree[0], level, new_tree)




    class MyTransformer(Transformer):
        def __init__(self):
            self.variables = {}

        def start(self, items):
            print('\n\n\nVARIABLES:')
            print(self.variables)#, end='\n\n\n')

        def vars(self, items):
            pass

        def var(self, items):
            self.variables[items[0]] = items[1]

        def varcall(self, items):
            return items[0]

        def rgb(self, items):
            if len(items) == 3:
                # testar valor dos elementos
                return ('rgb', (items[0], items[1], items[2]))
            elif len(items) == 1:
                return ('hex', (items[0]))

        def slides(self, items):
            new_tree = []
            for item in items:
                new_tree.append(make_tree(item, 0))
            print(new_tree)
            print()
            for item in new_tree:
                parse_slides(item)

        def content(self, items):
            if items[0] == 'slide':
                return 'slide'
            
            children = []
            for i in range(1, len(items)):
                children.append(items[i])

            return (items[0], children)

        def endc(self, items):
            return Discard

        def slide(self, items):
            return 'slide'



        def INT(self, token):
            return int(token)

        def WORD(self, token):
            return str(token)

        def HEXWORD(self, token):
            return str(token)


    ## Primeiro precisamos da GIC
    grammar = '''
    start: vars? slides
    vars: var+ 
    slides: "start" content*  "end"

    varcall: "#" WORD
    var: varcall "=" rgb
        | "var até agora só contempla cores"
    rgb: "(" INT "," INT "," INT ")"
        | "0" "x" HEXWORD 

    content: WORD content+ endc 
            | slide
    slide: "slide"
    endc: "."




    HEXWORD: HEXDIGIT+

    %import common.WS
    %import common.INT
    %import common.WORD
    %import common.HEXDIGIT
    %ignore WS
    '''

    frase = '''
    #black = (10,30,40)
    #white = 0xFFFFFF

    start 
        bground
            text
                slide.
            slide
            text
                slide..
    end
    '''
    p = Lark(grammar)

    print('===========================   PRINT TREE   ===========================')
    parse_tree = p.parse(frase)
    print(parse_tree.pretty())

    print('\n')
    print('===========================   DEBUG PARSER PRINTS   ===========================')
    print()
    data = MyTransformer().transform(parse_tree)
    #print(data)
