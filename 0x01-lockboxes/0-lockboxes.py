#!/usr/bin/python3
'''returns true of locboxes can all be opened and false if not'''


def join(lst1, lst2):
    results = []
    for num in lst2:
        results += lst1[num]
    return results


def canUnlockAll(boxes):
    '''returns true of locboxes can all be opened and false if not'''
    index = 0
    total = list(set(boxes[0]) | {0})
    added = True
    while added:
        added = False
        for j in join(boxes, total[index:]):
            if j not in total:
                total.append(j)
                index += 1
                added = True
        return len(total) == len(boxes)