# -*- coding: utf-8 -*-
#w = [1, 3, 5, 7, 11, 13, 17, 19]
#c = [23, 29, 31, 37, 41, 43, 47]

import random
import copy


class Generate(object):
    def __init__(self, vItem=(1, 3, 5, 7, 11, 13, 17, 19),
                 vBag = (23, 29, 31, 37, 41, 43, 47),
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
            vol = aux[random.randint(0, len(self.vBag) - 1)]
            bags.append(vol)
            aux.remove(vol)
        for i in range(self.nItem):
            items.append([self.vItem[random.randint(0, len(self.vItem) - 1)], self.nBag])

        return [bags, items]

    def desalloc(self, state):
        newState = copy.deepcopy(state)

        for i in range(len(newState[1])):
            newState[1][i][1] = len(newState[0])

        return newState


class Utils(object):
    st = []

    def __init__(self, state):
        self.st = state

    def printBags(self):
        bags = self.BagsList(len(self.st[0]))
        outBag = []

        for i in self.st[1]:
            bag_index = i[1]
            if bag_index != len(self.st[0]):
                item = i[0]
                bags[bag_index].append(item)
                continue
            outBag.append(i[0])

        for i in range(len(bags)):
            print 'Bag {} = {} | Max Vol. = {} , Allocated = {}'.format(i, bags[i], self.st[0][i], sum(bags[i]))
        print 'Items out of bags: {}'.format(outBag)

    def BagsList(self, size):
        bags = list()
        for i in range(0, size):
            bags.append(list())
        return bags