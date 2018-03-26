# -*- coding: utf-8 -*-

import random
import copy
from heuristic import Heuristic
class Neighbor(object):


    def __init__(self, state):
        self.state = state
        self.bagState = state[0]
        self.itemState = state[1]

    def generateState2(self):

        newState = copy.deepcopy(self.state)
        nBagState = newState[0]
        nItemState = newState[1]


        for i in range(len(nBagState)):
            for j in range(len(nItemState)):
                index = random.randint(0,(len(nItemState) -1))

                if (len(nBagState)) == nItemState[index][1] and \
                        Heuristic(newState).bagWeight2(i, nItemState[index][0]):
                    nItemState[index][1] = i

        return newState





    def generateState(self):
        itemState = self.state[1]

        newState = copy.deepcopy(self.state)

        nChange = len(itemState) / random.randint(1, len(itemState)/2)

        itemChange = [] #itens que irão mudar

        for i in range(nChange):
            rn = random.randint(0, len(itemState) - 1)
            while rn in itemChange:
                rn = random.randint(0, len(itemState) - 1)

            itemChange.append(rn)

        for i in range(len(itemChange)):
            newState[1][itemChange[i]][1] = random.randint(0,len(self.state[0]))

        return newState
