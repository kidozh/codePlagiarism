# -*- coding: UTF-8 -*-
__author__ = 'kidozh'
import os

fileExt = {
    'c/c++':["cpp", "CPP", "cxx", "CXX", "c", ".C", "h", "H"],
    'char':["TXT", "txt", "ASC", "asc", "TEX", "tex","cpp", "CPP", "cxx", "CXX", "c", ".C", "h", "H","PY","py"]
}

C_CPP = 'c/c++'
CHAR = 'char'

def get_all_lang_files(path,language='char'):
    '''
    get all listed files
    :param path:
    :param language:
    :return: key -- prob value -- file list
    '''

    # collect each dir
    fileSet = {}
    for root, dirs, files in os.walk(path) :
        # collect all the verified file
        print dirs
        for dirClass in dirs:
            for fileRoot,dirs,files in os.walk(os.path.join(root,dirClass)):
                print '# ',dirClass,files,os.path.join(root,dirClass)
                for file in files:
                    # if it's less than 2,just return null
                    if len(files) < 2 :
                        continue
                    # check every file extension
                    spiltedFilename = str(file).split('.')
                    # verify if it has proper extension
                    if len(spiltedFilename) > 1 and spiltedFilename[-1] in fileExt[language]:
                        if fileSet.has_key(dirClass):
                            fileSet[dirClass].append(os.path.join(fileRoot,file))
                        else:
                            fileSet[dirClass] = [os.path.join(fileRoot,file)]

        return fileSet


class ast_info_node:
    str = ''
    def __init__(self):
        self.str = ''
    def __str__(self):
        return self.str.decode('utf8')
    def write(self,string):
        self.str += string
    @property
    def ast_string(self):
        return self.str.decode('utf8')



# print os.path.dirname(os.path.dirname(__file__))
if __name__ == '__main__':
    print get_all_lang_files(os.path.dirname(os.path.dirname(__file__)),language='c/c++')


