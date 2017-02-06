# -*- coding: UTF-8 -*-
__author__ = 'kidozh'


import sys

sys.path.extend(['.', '..'])

from compare.checkSet import get_sim_by_set
from cluster import ast_info_node

with open('codeA.cpp','r') as fileA:
    with open('codeB.cpp','r') as fileB:
        get_sim_by_set(fileA.read(),fileB.read())

# test AST method
from pycparser import c_parser,parse_file

text = r"""
void func(void)
{
  x = 1;
}
"""


parser = c_parser.CParser()

_c_parser = c_parser.CParser()



with open('codeB.cpp','r') as file:
    text = file.read()
    from cluster.filter import comment_remover,remove_for_c_parser
    text = remove_for_c_parser(text)
    ast =  _c_parser.parse(text)
    print dir(ast)
    ast_info = ast_info_node()
    print ast.show(buf=ast_info)
    print ast_info.ast_string

