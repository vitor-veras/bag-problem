#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Heuristic(object):
    # state = [[bagW0, bagW1, bagW2], [(itemW0, inBagX), ...]]
    def __init__(self, state):
        self.state = state
        self.bagState = state[0]
        self.itemState = state[1]

    def bagWeight(self, indexBag, plusWeight):
        count = plusWeight
        for i in range(len(self.itemState)):
            if self.itemState[i][1] == indexBag:
                count += self.itemState[i][0]
        if self.bagState[indexBag] < count:
            return False

        return True

    def count(self):
        total = 0
        for i in range(len(self.bagState)):
            total += self.countInBag(i)

        return total

    def countInBag(self, bagIndex):
        eval = 0
        for i in range(len(self.itemState)):
            if self.itemState[i][1] == bagIndex:
                eval += self.itemState[i][0]
                # eval += 1
        return eval

    def getTotalWeight(self):
        total = 0
        for i in range(len(self.bagState)):
            total += self.bagState[i]

        return total

    def getCurrentTotalWeight(self):
        total = 0
        for i in range(len(self.itemState)):
            if not self.itemState[i][1] == len(self.bagState):
                total += self.itemState[i][0]

        return total
