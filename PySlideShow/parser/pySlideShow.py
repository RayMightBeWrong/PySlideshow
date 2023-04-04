#!/usr/bin/python3

import sys
from lark import Lark
from grammar import grammar
import transformer


frase = sys.stdin.read()
p = Lark(grammar)

parse_tree = p.parse(frase)
data = transformer.Transformer().transform(parse_tree)
print(data)
