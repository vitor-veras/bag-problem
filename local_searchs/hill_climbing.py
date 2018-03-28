# -*- coding: utf-8 -*-

# Algoritmo HillClimbing adaptado de : https://en.wikipedia.org/wiki/Hill_climbing

from local_searchs.heuristic import Heuristic
from local_searchs.neighbor import Neighbor
from local_searchs.bag_problem import BagProblem

import copy


class HillClimbing(object):
    def __init__(self, iterate=100, startState=None):
        self.iterate = iterate
        self.startState = startState

    def hill_comum(self):
        currentState = self.startState

        currentEval = Heuristic(currentState).count()

        currentWeight = Heuristic(currentState).getCurrentTotalWeight()
        totalWeight = Heuristic(currentState).getTotalWeight()
        i = 0
        while i < self.iterate and currentWeight != totalWeight:
            newState = Neighbor(BagProblem().desalloc(currentState)).generateState()
            nextEval = Heuristic(newState).count()

            if nextEval > currentEval :
                currentState = copy.deepcopy(newState)
                currentEval = nextEval
                currentWeight = Heuristic(currentState).getCurrentTotalWeight()

            i += 1

        return currentState