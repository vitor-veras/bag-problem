# -*- coding: utf-8 -*-

class Utils(object):
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
            print('Bag {} = {} | Max Vol. = {} , Allocated = {}'.format(i+1, bags[i], self.st[0][i], sum(bags[i])))
        print('Items out of bags: {}'.format(outBag))

    def BagsList(self, size):
        bags = list()
        for i in range(0, size):
            bags.append(list())
        return bags