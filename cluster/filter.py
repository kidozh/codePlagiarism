# -*- coding: UTF-8 -*-

__author__ = 'kidozh'

import re

def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

def include_remover(text):
    include_regex = re.compile(r'(#include.+)|(#pragma.+)$',re.MULTILINE)
    return re.sub(include_regex,'',text)

def remove_for_c_parser(text):
    return include_remover(comment_remover(text))

from pycparser import c_parser
from cluster import ast_info_node
def get_ast_from_c(Ccode):
    '''
    get ast from C code without comments and include or pragma cmd
    :param Ccode:list or character
    :return: ast string
    '''
    ast_info = ast_info_node()
    parser = c_parser.CParser()
    if isinstance(Ccode,list):
        ast_list = []
        for eachCode in Ccode:

            ast = parser.parse(eachCode)
            ast.show(buf=ast_info)
            ast_list.append(ast_info.ast_string)

        return ast_list
    else:
        # we assume it's a character
        ast = parser.parse(Ccode)
        ast.show(buf=ast_info)
        return ast_info.ast_string
