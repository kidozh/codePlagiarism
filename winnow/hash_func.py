# -*- coding: UTF-8 -*-
__author__ = 'kidozh'


def hash_md5(text):
    import hashlib

    hashText = hashlib.md5(text.encode('utf8'))
    hashHex = hashText.hexdigest()
    hashHex = int(hashHex,16)

    return hashHex