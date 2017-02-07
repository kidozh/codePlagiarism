# -*- coding: UTF-8 -*-
__author__ = 'kidozh'
from cluster import *

class simArray:
    probFile={}
    simiMatrix = {}
    textMatrix = {}
    def __init__(self):
        self.probFile = {}
        self.simiMatrix = {}
        self.textMatrix = {}

    def get_simi_from_path(self,path,language='char'):
        from compare.checkSet import get_sim_by_set
        fileCluster = get_all_lang_files(path,language=language)
        for prob,fileList in fileCluster.items():
            # read all list
            self.textMatrix[prob] = []
            self.probFile[prob] = []
            totProbLen = len(fileList)
            self.simiMatrix[prob] = [[1.0]*totProbLen]*totProbLen
            # get all code
            for aimFile in fileList:
                with open(aimFile,'r') as file:
                    if language == C_CPP:
                        from cluster.filter import remove_for_c_parser,get_ast_from_c
                        # remove all the comments and include
                        # and gennerate AST
                        self.textMatrix[prob].append(get_ast_from_c(remove_for_c_parser(file.read())))
                        pass
                    else:
                        self.textMatrix[prob].append( file.read())
            # compare each other

            for indexA,textA in enumerate(self.textMatrix[prob]) :
                # self.simiMatrix[prob][indexA][indexA] = 1.0
                if (totProbLen - 1 == indexA):
                    break
                for indexB in xrange(indexA+1,totProbLen-1):
                    A2B,B2A = get_sim_by_set(textA,self.textMatrix[prob][indexB])
                    self.simiMatrix[prob][indexA][indexB] = A2B
                    self.simiMatrix[prob][indexB][indexA] = B2A
                    print fileCluster[prob][indexA],fileCluster[prob][indexB],A2B,B2A
                    if A2B > 0.75 or B2A > 0.75:
                        print fileCluster[prob][indexA],fileCluster[prob][indexB],A2B,B2A

help_text='''
you can refer to readme.MD for help
'''

if __name__ == '__main__':
    a = simArray()
    import getopt
    import sys
    opts, args = getopt.getopt(sys.argv[1:], "d:l:h", ["help"])
    help = False
    for opt,val in opts:
        if opt == '-d':
            dir = val
        elif opt == '-l':
            lan = val
        elif opt == '-h' or opt == '--help':
            print 'opt'
            help = True
    if not help:
        a.get_simi_from_path(val,language=lan)