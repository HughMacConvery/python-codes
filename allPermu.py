# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:48:44 2019
@author: jacy
"""
def permutation(string):
    if len(string) <= 1:
        return [string]
    else:
        wordList = []
        for word in permutation(string [: - 1]):
            for i in range (len(word) + 1):
                perWord = word [: i] + string[-1] + word[i:]
                wordList.append(perWord)
        return sorted(wordList)