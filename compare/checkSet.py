__author__ = 'kidozh'
# -*- coding: UTF-8 -*-
from winnow import winnow_text_by_default,winnow_text_by_md5

def get_fingerPrint_cnt(winnowSet):
    """
    count all the fingerPrint
    :param winnowSet:
    :return:
    """
    cntDict = {}
    for pos,hash in winnowSet:
        if cntDict.has_key(hash):
            cntDict[hash] += 1
        else:
            cntDict[hash] = 1

    return cntDict

def get_sim_by_set(textA,textB):
    '''
    it will caculate two fingerPrint then check its & and | set
    :param textA:
    :param textB:
    :return: simiA_2_B,simiB_2_A
    '''
    winnowA = winnow_text_by_default(textA)
    winnowB = winnow_text_by_default(textB)

    # check its common
    cntDictA = get_fingerPrint_cnt(winnowA)
    cntDictB = get_fingerPrint_cnt(winnowB)

    intersectionFingerprint = len(winnowA) + len(winnowB)
    unionFingerprint = 0
    # merge dict
    for hash,cnt in cntDictA.items():
        if cntDictB.has_key(hash):
            # common set
            unionFingerprint += min(cntDictB[hash],cnt)

    # print intersectionFingerprint,unionFingerprint,2*float(unionFingerprint)/intersectionFingerprint
    # print len(winnowA),len(winnowB),float(unionFingerprint)/len(winnowA),float(unionFingerprint)/len(winnowB)
    return float(unionFingerprint)/len(winnowA),float(unionFingerprint)/len(winnowB)
