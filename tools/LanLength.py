# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 23:32:50 2022

@author: 81702
"""
# https://docs.python.org/ja/3/library/itertools.html
from itertools import groupby
# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "list[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res
# RUN LENGTH DECODING list(tuple()) -> str
# example) [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] -> "aabbbbaaca"
def runLengthDecode(L: "list[tuple]") -> str:
    res = ""
    for c, n in L:
        res += c * int(n)
    return res
# RUN LENGTH ENCODING str -> str
# example) "aabbbbaaca" -> "a2b4a2c1a1"
def runLengthEncodeToString(S: str) -> str:
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
    return res
