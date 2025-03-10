# -*- encoding: utf-8 -*-
"""
@File    : user_json.py
@Time    : 2021/3/19 10:19
@Author  : Ryt_tech
@Email   : zhaohongyu2401@yeah.net
@Software: PyCharm
"""
import json
import random

def load_data(path):
    w1 = [u'\u76f8\u5bf9\u8fd0\u52a8', u'\u8fde\u7eed\u79fb\u52a8', u'\u65cb\u8f6c', u'\u4f4d\u7f6e', u'\u52a8\u6cbf',
     u'\u56fa\u5b9a\u79fb\u52a8', u'\u914d\u5408\u79fb\u52a8', u'\u52a8\u659c\u6258\u5757', u'\u6746\u671d',
     u'\u52a8\u540e', u'\u9488\u79fb\u52a8', u'\u9500\u6cbf', u'\u65bd\u52a0\u529b', u'\u79fb\u52a8\u72b6\u6001',
     u'\u53cd\u5411\u8fd0\u52a8', u'\u8fdc\u79bb', u'\u62c9\u52a8', u'\u7f29\u56de', u'\u8f6c\u52a8',
     u'\u79fb\u52a8\u7a7a\u95f4', u'\u6258\u67b6\u79fb\u52a8', u'\u624b\u79fb\u52a8', u'\u5de5\u4ef6\u79fb\u52a8',
     u'\u79fb\u52a8\u8f68\u8ff9', u'\u4e8c\u4f4d\u7f6e', u'\u79fb\u52a8\u5230\u4f4d', u'\u4f4d\u79fb\u65f6',
     u'\u79fb\u52a8\u884c\u7a0b', u'\u53ef\u524d\u540e\u5de6\u53f3', u'\u6ed1\u5757\u5de6\u53f3',
     u'\u5f84\u5411\u79fb\u52a8', u'\u4f4d\u79fb', u'\u4f38\u7f29\u79fb\u52a8', u'\u79fb\u52a8\u540c\u6b65',
     u'\u7528\u6237\u79fb\u52a8', u'\u79fb\u52a8\u8f6c\u6362', u'\u81ea\u52a8\u79fb\u52a8', u'\u524d\u79fb',
     u'\u4efb\u610f\u79fb\u52a8', u'\u540e\u9000', u'\u79fb\u52a8\u63a8\u52a8', u'\u5355\u5143\u79fb\u52a8',
     u'\u79fb\u5411', u'\u52a8\u4f7f', u'\u79fb\u52a8\u8fc7\u7a0b', u'\u79fb\u52a8\u91cf', u'\u90e8\u4ef6\u79fb\u52a8',
     u'\u6eda\u8f6e\u79fb\u52a8', u'\u79fb\u4f4d', u'\u53ef\u76f4\u7ebf']
    w2 = [u'\u667a\u80fdSD', u'\u79fb\u52a8\u7535\u5b50\u652f\u4ed8', u'\u81ea\u52a9\u5145\u503c',
     u'\u7535\u5b50\u8d26\u6237\u4fdd\u5bc6', u'\u91d1\u878d\u4ea4\u6613', u'\u7535\u5b50\u5145\u503c',
     u'\u79fb\u52a8\u9500\u552e\u70b9', u'\u786e\u8ba4\u652f\u4ed8', u'\u591a\u5361\u5408\u4e00', u'\u94f6\u8054\u5361',
     u'\u63a5\u89e6\u5f0f\u5237\u5361', u'\u9632\u76d7\u5237', u'\u4ea4\u6613\u7cfb\u7edf',
     u'\u667a\u80fd\u652f\u4ed8\u7ec8\u7aef', u'\u5feb\u9012\u8d39', u'\u901a\u4fe1\u652f\u4ed8',
     u'\u79bb\u7ebf\u4ea4\u6613', u'\u79fb\u52a8\u91d1\u878d', u'\u8fdc\u7a0b\u652f\u4ed8', u'\u7a7a\u4e2d\u53d1\u5361',
     u'\u652f\u4ed8\u5b9d', u'NFC', u'\u667a\u80fd\u79fb\u52a8\u652f\u4ed8', u'\u7f51\u4e0a\u4ea4\u6613',
     u'\u7535\u5b50\u4ea4\u6613', u'\u7535\u5b50\u7968\u52a1', u'\u652f\u4ed8\u624b\u6bb5', u'\u7f51\u4e0a\u94f6\u884c',
     u'\u94f6\u884c\u5361', u'\u652f\u4ed8\u670d\u52a1', u'POS', u'\u652f\u4ed8\u4ea4\u6613', u'\u667a\u80fd\u5361',
     u'\u8131\u673a\u6d88\u8d39', u'\u624b\u673a\u94f6\u884c', u'\u652f\u4ed8\u64cd\u4f5c', u'\u52a0\u6cb9\u6536\u94f6',
     u'\u6536\u94f6\u7cfb\u7edf', u'\u667a\u80fdPOS', u'\u91d1\u878d', u'\u6307\u7eb9\u652f\u4ed8',
     u'\u5b89\u5168\u8ba4\u8bc1', u'\u94f6\u884c\u8f6c\u8d26', u'\u652f\u4ed8\u5361', u'\u667a\u80fd\u652f\u4ed8',
     u'\u94f6\u8054\u95ea\u4ed8', u'\u79fb\u52a8\u4ea4\u6613', u'\u5c0f\u989d', u'\u8d22\u4ed8',
     u'\u79fb\u52a8\u5145\u503c']
    w3 = [u'\u4ea4\u6613\u8bbe\u5907', u'\u5168\u6b3e', u'\u4ee3\u6536\u8d39', u'\u667a\u80fd\u652f\u4ed8',
     u'\u8d27\u5230\u4ed8\u6b3e', u'\u652f\u4ed8\u6e20\u9053', u'\u652f\u4ed8\u73af\u5883', u'\u4ea4\u6613\u7cfb\u7edf',
     u'\u4fe1\u7528\u5361', u'\u4e91\u652f\u4ed8', u'\u91d1\u878d\u673a\u6784', u'\u94f6\u884c\u7ec8\u7aef',
     u'\u975e\u73b0\u91d1', u'\u94f6\u884c\u8d26', u'\u6536\u8d39', u'\u652f\u4ed8\u6a21\u5f0f',
     u'\u5728\u7ebf\u4ea4\u6613', u'\u8ba2\u5355\u652f\u4ed8', u'\u91d1\u989d', u'\u5361\u7ed3\u7b97',
     u'\u5361\u652f\u4ed8', u'\u9884\u4ed8\u91d1', u'\u652f\u4ed8\u7801', u'\u8d26\u6237', u'\u52a0\u6cb9\u6536\u94f6',
     u'\u94f6\u884c\u5e10\u6237', u'\u5546\u6237', u'\u5546\u5bb6\u7cfb\u7edf', u'\u5b9a\u91d1', u'\u652f\u4ed8\u5b9d',
     u'\u5237\u5361\u6d88\u8d39', u'\u652f\u4ed8\u65b9', u'\u81ea\u52a8\u9009\u62e9\u6536\u6b3e',
     u'\u8f66\u8f7d\u652f\u4ed8', u'\u65e0\u7ebf\u652f\u4ed8', u'\u5916\u90e8\u652f\u4ed8', u'\u652f\u4ed8\u6a21\u5757',
     u'\u652f\u4ed8\u7ba1\u7406', u'\u652f\u4ed8\u9a8c\u8bc1', u'\u626b\u7801\u652f\u4ed8', u'\u7535\u5b50\u4ea4\u6613',
     u'\u652f\u4ed8\u7ec8\u7aef', u'\u79fb\u52a8\u7535\u5b50\u652f\u4ed8', u'\u652f\u4ed8\u5b89\u5168', u'\u5c0f\u989d',
     u'\u652f\u4ed8\u6307\u4ee4', u'\u91d1\u878d\u4ea4\u6613', u'\u8fdc\u7a0b\u652f\u4ed8', u'\u8ba2\u91d1',
     u'\u8ba4\u8bc1\u652f\u4ed8']

    w1r = [u'\u6eda\u8f6e\u79fb\u52a8', u'\u5355\u5143\u79fb\u52a8', u'\u540e\u9000', u'\u524d\u79fb',
     u'\u79fb\u52a8\u8fc7\u7a0b', u'\u79fb\u52a8\u8f6c\u6362', u'\u79fb\u5411', u'\u53ef\u76f4\u7ebf', u'\u52a8\u4f7f',
     u'\u7528\u6237\u79fb\u52a8', u'\u5f84\u5411\u79fb\u52a8', u'\u81ea\u52a8\u79fb\u52a8', u'\u4efb\u610f\u79fb\u52a8',
     u'\u4f4d\u79fb', u'\u90e8\u4ef6\u79fb\u52a8', u'\u4f38\u7f29\u79fb\u52a8', u'\u79fb\u52a8\u91cf',
     u'\u79fb\u52a8\u540c\u6b65', u'\u79fb\u52a8\u63a8\u52a8', u'\u79fb\u4f4d', u'\u79fb\u52a8\u5e76',
     u'\u79fb\u52a8\u540e', u'\u56de\u79fb\u52a8', u'\u6765\u56de\u79fb\u52a8', u'\u76f8\u5bf9\u79fb\u52a8',
     u'\u8fd0\u52a8', u'\u6c34\u5e73\u79fb\u52a8', u'\u76f4\u7ebf\u79fb\u52a8', u'\u81ea\u7531\u79fb\u52a8',
     u'\u79fb\u52a8\u5e76\u4e14', u'\u5f80\u590d\u79fb\u52a8', u'\u79fb\u52a8\u800c\u79fb\u52a8', u'\u52a8\u65f6',
     u'\u524d\u540e\u79fb\u52a8', u'\u79fb\u52a8\u65b9\u5411', u'\u53ef\u4ee5\u79fb\u52a8', u'\u53ef\u79fb\u52a8',
     u'\u65cb\u8f6c\u79fb\u52a8', u'\u6ed1\u52a8', u'\u79fb\u52a8\u8def\u5f84', u'\u884c\u8fdb',
     u'\u8f74\u5411\u79fb\u52a8', u'\u79fb\u52a8\u4f4d\u7f6e', u'\u79bb\u5f00', u'\u80fd\u79fb\u52a8',
     u'\u7ec4\u4ef6\u79fb\u52a8', u'\u79fb\u52a8\u64cd\u4f5c', u'\u6a2a\u5411\u79fb\u52a8', u'\u80fd\u591f\u79fb\u52a8',
     u'\u4e0a\u4e0b\u79fb\u52a8']
    w2r = [u'\u94f6\u8054\u95ea\u4ed8', u'\u652f\u4ed8\u5361', u'\u79fb\u52a8\u4ea4\u6613', u'\u624b\u673a\u94f6\u884c',
     u'\u94f6\u884c\u8f6c\u8d26', u'\u8d22\u4ed8', u'\u6536\u94f6\u7cfb\u7edf', u'\u6307\u7eb9\u652f\u4ed8',
     u'\u5c0f\u989d', u'\u52a0\u6cb9\u6536\u94f6', u'\u667a\u80fd\u652f\u4ed8', u'\u91d1\u878d',
     u'\u652f\u4ed8\u64cd\u4f5c', u'\u8131\u673a\u6d88\u8d39', u'\u5b89\u5168\u8ba4\u8bc1', u'\u667a\u80fd\u5361',
     u'\u667a\u80fdPOS', u'POS', u'\u652f\u4ed8\u4ea4\u6613', u'\u79fb\u52a8\u5145\u503c', u'\u652f\u4ed8\u529f\u80fd',
     u'\u5b89\u5168\u652f\u4ed8', u'\u5b89\u5168\u79fb\u52a8\u652f\u4ed8', u'\u8fd1\u573a\u652f\u4ed8',
     u'\u652f\u4ed8\u7ec8\u7aef', u'\u624b\u673a\u652f\u4ed8', u'\u652f\u4ed8', u'\u7535\u5b50\u652f\u4ed8',
     u'\u5feb\u6377\u652f\u4ed8', u'\u8d85\u8584\u9759\u8109', u'\u5728\u7ebf\u652f\u4ed8',
     u'\u4e8c\u7ef4\u7801\u652f\u4ed8', u'\u652f\u4ed8\u5b89\u5168', u'\u7ebf\u4e0b\u652f\u4ed8',
     u'\u652f\u4ed8\u8bbe\u5907', u'\u95ea\u4ed8', u'\u65e0\u7ebf\u652f\u4ed8', u'\u514d\u5bc6',
     u'\u652f\u4ed8\u4e1a\u52a1', u'\u5361\u652f\u4ed8', u'\u65e0\u5361\u652f\u4ed8', u'POS\u7ec8\u7aef',
     u'\u7f51\u7edc\u652f\u4ed8', u'\u626b\u7801\u652f\u4ed8', u'\u84dd\u7259\u7ed3\u5408', u'\u6d88\u8d39\u652f\u4ed8',
     u'\u652f\u4ed8\u5e73\u53f0', u'\u79bb\u7ebf\u652f\u4ed8', u'\u5fae\u4fe1\u652f\u4ed8', u'\u5237\u5361\u529f\u80fd']
    w3r = [u'\u91d1\u878d\u4ea4\u6613', u'\u5c0f\u989d', u'\u5916\u90e8\u652f\u4ed8', u'\u626b\u7801\u652f\u4ed8',
     u'\u8fdc\u7a0b\u652f\u4ed8', u'\u652f\u4ed8\u6a21\u5757', u'\u8ba2\u91d1', u'\u7535\u5b50\u4ea4\u6613',
     u'\u8f66\u8f7d\u652f\u4ed8', u'\u79fb\u52a8\u7535\u5b50\u652f\u4ed8', u'\u652f\u4ed8\u65b9',
     u'\u652f\u4ed8\u6307\u4ee4', u'\u652f\u4ed8\u7ba1\u7406', u'\u65e0\u7ebf\u652f\u4ed8', u'\u652f\u4ed8\u9a8c\u8bc1',
     u'\u652f\u4ed8\u5b89\u5168', u'\u5237\u5361\u6d88\u8d39', u'\u652f\u4ed8\u7ec8\u7aef', u'\u8ba4\u8bc1\u652f\u4ed8',
     u'\u81ea\u52a8\u9009\u62e9\u6536\u6b3e', u'\u4ed8\u6b3e', u'\u5728\u7ebf\u652f\u4ed8', u'\u7535\u5b50\u652f\u4ed8',
     u'\u652f\u4ed8\u8fc7\u7a0b', u'\u7f51\u7edc\u652f\u4ed8', u'\u652f\u4ed8\u670d\u52a1', u'\u652f\u4ed8\u4fe1\u606f',
     u'\u7ed3\u7b97', u'\u4ea4\u6613', u'\u652f\u4ed8\u4ea4\u6613', u'\u73b0\u91d1\u652f\u4ed8',
     u'\u652f\u4ed8\u5904\u7406', u'\u7f51\u4e0a\u652f\u4ed8', u'\u652f\u4ed8\u8bf7\u6c42', u'\u7ebf\u4e0b\u652f\u4ed8',
     u'\u8d26\u6237\u652f\u4ed8', u'\u652f\u4ed8\u6388\u6743', u'\u652f\u4ed8\u5e73\u53f0', u'\u6536\u6b3e',
     u'\u786e\u8ba4\u652f\u4ed8', u'\u4e8c\u7ef4\u7801\u652f\u4ed8', u'\u6d88\u8d39\u652f\u4ed8', u'\u4ed8\u8d39',
     u'\u652f\u4ed8\u529f\u80fd', u'\u5fae\u4fe1\u652f\u4ed8', u'\u514d\u5bc6', u'\u652f\u4ed8\u64cd\u4f5c',
     u'\u652f\u4ed8\u624b\u6bb5', u'\u65e0\u5361\u652f\u4ed8', u'\u652f\u4ed8\u4e1a\u52a1']

    print(u'移动')
    print(','.join(w1))
    print(','.join(w1r))

    print(u'移动支付')
    print(','.join(w2))
    print(','.join(w2r))

    print(u'支付')
    print(','.join(w3))
    print(','.join(w3r))
    return 0

    userid = 'admin'

    his_words =[u'移动',u'移动支付',u'支付',u'什么']
    data = {}
    data[userid] = {}
    tem = {}
    for i in w1 :
        tem[i] = random.randint(1,10)
    data[userid][his_words[0]] = tem

    tem = {}
    for i in w2:
        tem[i] = random.randint(1,10)
    data[userid][his_words[1]] = tem

    tem = {}
    for i in w3:
        tem[i] = random.randint(1,10)
    data[userid][his_words[2]] = tem

    json.dump(data, open('user_history_click.json', 'w'))

path =' '
load_data(path)
