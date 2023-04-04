#!/usr/bin/python3

from lark import Lark
from parser.grammar import grammar
import parser.transformer as transformer
def parsePSS(file):
    p = Lark(grammar)
    parse_tree = p.parse(file)
    data = transformer.Transformer().transform(parse_tree)
    return data