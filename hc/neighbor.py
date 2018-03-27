# -*- coding: utf-8 -*-

import random
import copy
from heuristic import Heuristic
class Neighbor(object):


    def __init__(self, state):
        self.state = state
        self.bagState = state[0]
        self.itemState = state[1]

    def generateState(self):

        newState = copy.deepcopy(self.state)
        nBagState = newState[0]
        nItemState = newState[1]


        for i in range(len(nBagState)):
            for j in range(len(nItemState)):
                index = random.randint(0,(len(nItemState) -1))

                if (len(nBagState)) == nItemState[index][1] and \
                        Heuristic(newState).bagWeight(i, nItemState[index][0]):
                    nItemState[index][1] = i

        return newState
