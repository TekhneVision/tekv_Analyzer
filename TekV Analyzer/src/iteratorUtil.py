'''
Created on Jan 14, 2018

@author: Jerime
'''

def unwrapListOfLists(_list):
    unwrapedList = []
    for item in _list:
        for value in item:
            unwrapedList.append(value)
    return unwrapedList

def unwrapList(_list):
    unwrapedList = []
    for item in _list:
        unwrapedList.append(item)
    return unwrapedList