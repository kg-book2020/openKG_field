# -*- encoding: utf-8 -*-
"""
@File    : testEs.py.py
@Time    : 2021/3/19 14:00
@Author  : Ryt_tech
@Email   : zhaohongyu2401@yeah.net
@Software: PyCharm
"""

# Set your own model path
MODELDIR="D:\\Python_Packages\\ltp_data"

import sys
import os
 
from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer
import jieba.posseg

# stopwordFile = open('stopWord.txt', 'r')
# wordMerg = 'wordMerge.txt'
# jieba.load_userdict(wordMerg)
print ("正在加载LTP模型... ...")

segmentor = Segmentor()
segmentor.load(os.path.join(MODELDIR, "cws.model"))

postagger = Postagger()
postagger.load(os.path.join(MODELDIR, "pos.model"))

parser = Parser()
parser.load(os.path.join(MODELDIR, "parser.model"))

recognizer = NamedEntityRecognizer()
recognizer.load(os.path.join(MODELDIR, "ner.model"))

#labeller = SementicRoleLabeller()
#labeller.load(os.path.join(MODELDIR, "srl/"))

print ("加载模型完毕。")

in_file_name = "inputold.txt"
out_file_name = "outputold.txt"
begin_line = 1
end_line = 0

if len(sys.argv) > 1:
    in_file_name = sys.argv[1]

if len(sys.argv) > 2:
    out_file_name = sys.argv[2]

if len(sys.argv) > 3:
    begin_line = int(sys.argv[3])

if len(sys.argv) > 4:
    end_line = int(sys.argv[4])

def extraction_start(in_file_name, out_file_name, begin_line, end_line):
    """
    事实三元组抽取的总控程序
    Args:
        in_file_name: 输入文件的名称
        #out_file_name: 输出文件的名称
        begin_line: 读文件的起始行
        end_line: 读文件的结束行
    """
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    
    line_index = 1
    sentence_number = 0
    text_line = in_file.readline()
    while text_line:

        if line_index < begin_line:
            text_line = in_file.readline()
            line_index += 1
            continue
        if end_line != 0 and line_index > end_line:
            break
        sentence = text_line.strip()
        if sentence == "" or len(sentence) > 1000:
            text_line = in_file.readline()
            line_index += 1
            continue
        try:
            fact_triple_extract(sentence, out_file)
            out_file.flush()
        except:
            pass
        sentence_number += 1

        if sentence_number % 50 == 0:
            print ("%d done" % (sentence_number))
        text_line = in_file.readline()
        line_index += 1

    in_file.close()
    out_file.close()

def checkRull(flag, word):
    if (flag[0] =='n' or flag == 'x' or flag == 'eng' or flag =='l' or flag =='b' or flag[0] =='v'):
        return True
    return False

def fact_triple_extract(sentence, out_file):
    """
    对于给定的句子进行事实三元组抽取
    Args:
        sentence: 要处理的语句
    """
    #print sentence
    tem = jieba.posseg.cut(sentence)
    words=[]
    for word, flag in tem:
        #
        # if checkRull(flag, word):
        #     word = word.decode('utf-8').encode('utf-8').replace('\r', '').replace('\n', '')
            words.append(' ' + word)
    print ('\t'.join(words))

    words = list(words)

    # print("ssss"+"\t".join(words))
    # print('---------\n')
    words1 = segmentor.segment(sentence)
    words = list(words1)
    # print ("\t".join(words))
    postags = postagger.postag(words)
    netags = recognizer.recognize(words, postags)
    arcs = parser.parse(words, postags)
    #print "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)

    child_dict_list = build_parse_child_dict(words, postags, arcs)
    for index in range(len(postags)):
        # 抽取以谓词为中心的事实三元组
        if postags[index] == 'v':
            child_dict = child_dict_list[index]
            # 主谓宾
            if child_dict.has_key('SBV') and child_dict.has_key('VOB'):
                e1 = complete_e(words, postags, child_dict_list, child_dict['SBV'][0])
                r = words[index]
                e2 = complete_e(words, postags, child_dict_list, child_dict['VOB'][0])
                out_file.write("主语谓语宾语关系\t(%s, %s, %s)\n" % (e1, r, e2))
                out_file.flush()
            # 定语后置，动宾关系
            if arcs[index].relation == 'ATT':
                if child_dict.has_key('VOB'):
                    e1 = complete_e(words, postags, child_dict_list, arcs[index].head - 1)
                    r = words[index]
                    e2 = complete_e(words, postags, child_dict_list, child_dict['VOB'][0])
                    temp_string = r+e2
                    if temp_string == e1[:len(temp_string)]:
                        e1 = e1[len(temp_string):]
                    if temp_string not in e1:
                        out_file.write("定语后置动宾关系\t(%s, %s, %s)\n" % (e1, r, e2))
                        out_file.flush()
            # 含有介宾关系的主谓动补关系
            if child_dict.has_key('SBV') and child_dict.has_key('CMP'):
                #e1 = words[child_dict['SBV'][0]]
                e1 = complete_e(words, postags, child_dict_list, child_dict['SBV'][0])
                cmp_index = child_dict['CMP'][0]
                r = words[index] + words[cmp_index]
                if child_dict_list[cmp_index].has_key('POB'):
                    e2 = complete_e(words, postags, child_dict_list, child_dict_list[cmp_index]['POB'][0])
                    out_file.write("介宾关系主谓动补\t(%s, %s, %s)\n" % (e1, r, e2))
                    out_file.flush()

        # 尝试抽取命名实体有关的三元组
        if netags[index][0] == 'S' or netags[index][0] == 'B':
            ni = index
            if netags[ni][0] == 'B':
                while netags[ni][0] != 'E':
                    ni += 1
                e1 = ''.join(words[index:ni+1])
            else:
                e1 = words[ni]
            if arcs[ni].relation == 'ATT' and postags[arcs[ni].head-1] == 'n' and netags[arcs[ni].head-1] == 'O':
                r = complete_e(words, postags, child_dict_list, arcs[ni].head-1)
                if e1 in r:
                    r = r[(r.index(e1)+len(e1)):]
                if arcs[arcs[ni].head-1].relation == 'ATT' and netags[arcs[arcs[ni].head-1].head-1] != 'O':
                    e2 = complete_e(words, postags, child_dict_list, arcs[arcs[ni].head-1].head-1)
                    mi = arcs[arcs[ni].head-1].head-1
                    li = mi
                    if netags[mi][0] == 'B':
                        while netags[mi][0] != 'E':
                            mi += 1
                        e = ''.join(words[li+1:mi+1])
                        e2 += e
                    if r in e2:
                        e2 = e2[(e2.index(r)+len(r)):]
                    if r+e2 in sentence:
                        out_file.write("人名//地名//机构\t(%s, %s, %s)\n" % (e1, r, e2))
                        out_file.flush()

def build_parse_child_dict(words, postags, arcs):
    """
    为句子中的每个词语维护一个保存句法依存子节点的字典
    Args:
        words: 分词列表
        postags: 词性列表
        arcs: 句法依存列表
    """
    child_dict_list = []
    for index in range(len(words)):
        child_dict = dict()
        for arc_index in range(len(arcs)):
            if arcs[arc_index].head == index + 1:
                if child_dict.has_key(arcs[arc_index].relation):
                    child_dict[arcs[arc_index].relation].append(arc_index)
                else:
                    child_dict[arcs[arc_index].relation] = []
                    child_dict[arcs[arc_index].relation].append(arc_index)
        #if child_dict.has_key('SBV'):
        #    print words[index],child_dict['SBV']
        child_dict_list.append(child_dict)
    return child_dict_list

def complete_e(words, postags, child_dict_list, word_index):
    """
    完善识别的部分实体
    """
    child_dict = child_dict_list[word_index]
    prefix = ''
    if child_dict.has_key('ATT'):
        for i in range(len(child_dict['ATT'])):
            prefix += complete_e(words, postags, child_dict_list, child_dict['ATT'][i])
    
    postfix = ''
    if postags[word_index] == 'v':
        if child_dict.has_key('VOB'):
            postfix += complete_e(words, postags, child_dict_list, child_dict['VOB'][0])
        if child_dict.has_key('SBV'):
            prefix = complete_e(words, postags, child_dict_list, child_dict['SBV'][0]) + prefix

    return prefix + words[word_index] + postfix

if __name__ == "__main__":
    #extraction_start(in_file_name, out_file_name, begin_line, end_line)
    in_file_name = 'title.txt'
    out_file_name = 'result.txt'
    extraction_start(in_file_name, out_file_name, begin_line, end_line)
