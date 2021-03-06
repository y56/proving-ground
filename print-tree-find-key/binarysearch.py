#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:15:05 2019

Find target in a sorted list.

For hits, return index.
For misses, return -1

@author: Yu-Jen (Eugene) Wang, yjwang.y56@gmail.com
"""


def binarysearch(sortedlist, target):

    def binarysearchhelper(sortedlist, target, low, high):

        if low > high:
            return -1

        mid = (low + high) // 2

        if (target == sortedlist[mid]):
            return mid

        if (target > sortedlist[mid]):
            return binarysearchhelper(sortedlist, target, (mid + 1), high)
        else:
            return binarysearchhelper(sortedlist, target, low, (mid - 1))

    return binarysearchhelper(sortedlist, target, 0, len(sortedlist) - 1)


if __name__ == '__main__':

    sortedlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    result = binarysearch(sortedlist, 1)
    print("target index is", result)
