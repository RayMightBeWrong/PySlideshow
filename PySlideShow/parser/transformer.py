from lark import Transformer

from parserFunctions import *
from PIL import ImageColor

stack = []
slides = []
def parse_slides(elem):
    if elem == 'slide':
        slides.append(stack.copy())
    elif elem == '.':
        stack.pop()
    else:
        stack.append(elem[0])
        for e in elem[1]:
            parse_slides(e)


class Transformer(Transformer):
    def __init__(self):
        self.variables = {}
        self.valid = True
        self.configuration = []

    def start(self, items):
        for slide in slides:
            print('SLIDE: ')
            for e in slide:
                print(e)
            print()
        print()

        if self.valid:
            if self.configuration == []:
                self.configuration = {'width': 500, 'heigth': 500}
            return {
                'config': self.configurations,
                'slides': slides
            }
        else:
            return None

    def config_content(self, items):
        valid, items = validate_config(items)
        
        self.valid = valid
        self.configurations = items

    def config_attr(self, items):
        return (items[0], items[1])

    def var(self, items):
        self.variables[items[0][1]] = items[1]

    def varcall(self, items):
        return ('varcall', items[0])        

    def rgb(self, items):
        if len(items) == 3:
            return (items[0], items[1], items[2])
        elif len(items) == 1: 
            if len(str(items[0])) == 6:
                color = ImageColor.getcolor('#' + str(items[0]), "RGB")
                return color
            else:
                return None 

    def slides(self, items):
        for item in items:
            parse_slides(item)

    def content(self, items):
        if items[0] == 'slide':
            return 'slide'

        children = []
        for i in range(1, len(items)):
            children.append(items[i])

        tag_dict = {}
        for attr in items[0]['taginfo']:
            tag_dict[attr[0]] = attr[1]

        tag = (items[0]['tagname'], tag_dict)
        return (tag, children, '.')

    def tag(self, items):
        valid, items[1] = validate_tag(items[0], items[1])
        if self.valid:
            self.valid = valid

        return {
            'tagname': items[0],
            'taginfo': items[1]
        }

    def tagname(self, items):
        return items[0]

    def taginfo(self, items):
        return items

    def attr(self, items):
        if isinstance(items[1], tuple):
            if items[1][1] in self.variables:
                items[1] = self.variables[items[1][1]]
            else:
                items[1] = None

        return (items[0], items[1])

    def attr_content(self, items):
        return items[0]

    def type(self, items):
        return items[0]

    def endc(self, items):
        return '.'

    def slide(self, items):
        return 'slide'

    def DURATION(self, token):
        return 'duration'

    def TEXT(self, token):
        return 'text'

    def IMG(self, token):
        return 'img'

    def NR(self, token):
        return float(token)

    def WORD(self, token):
        return str(token)

    def ESCAPED_STRING(self, token):
        token = str(token)
        token = token[1:-1]
        return token

    def HEXWORD(self, token):
        return str(token)

    def BOOL(self, token):
        if token == 'FALSE':
            return False
        elif token == 'TRUE':
            return True
