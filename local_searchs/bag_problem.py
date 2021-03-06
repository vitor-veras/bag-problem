# -*- coding: utf-8 -*-
# w = [1, 3, 5, 7, 11, 13, 17, 19]
# c = [23, 29, 31, 37, 41, 43, 47]

import random
import copy
import sys
from local_searchs.heuristic import Heuristic


class BagProblem(object):
    def __init__(self, vItem=[1, 3, 5, 7, 11, 13, 17, 19],
                 vBag=[23, 29, 31, 37, 41, 43, 47],
                 nBag=3,
                 nItem=30):
        self.vItem = vItem
        self.vBag = vBag
        self.nBag = nBag
        self.nItem = nItem

    def initState(self):
        items = []
        bags = []

        aux = list(self.vBag)
        for i in range(self.nBag):
            vol = aux[random.randint(0, len(aux) - 1)]
            bags.append(vol)
            aux.remove(vol)
        for i in range(self.nItem):
            items.append([self.vItem[random.randint(0, len(self.vItem) - 1)], self.nBag])

        return [bags, items]

    def desalloc(self, state):
        newState = copy.deepcopy(state)
        min_bag = sys.maxsize
        index = -1

        for i in range (len(newState[0])):
            a_weight = Heuristic(newState).countInBag(i)

            if a_weight < min_bag:
                index = i
                min_bag = a_weight

        for i in range(len(newState[1])):
            if newState[1][i][1] == index:
                newState[1][i][1] = len(newState[0])

        return newState
