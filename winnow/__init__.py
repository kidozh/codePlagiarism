# -*- coding: UTF-8 -*-
__author__ = 'kidozh'

import winnowing

from hash_func import hash_md5

def winnow_text_by_default(text):
    """
    winnow text by SHA-1
    :param text: text
    :return:
    """
    return winnowing.winnow(text)

def winnow_text_by_md5(text):
    """
    winnow text by MD5
    :param text: text
    :return: a set which contains fingerpirnt
    """
    winnowing.hash_function = hash_md5
    return winnowing.winnow(text.decode('utf-8'))

if __name__ == '__main__':
    # just for test
    print winnow_text_by_default('A do run run run, a do run run')
    print winnow_text_by_md5('The cake was a lie')