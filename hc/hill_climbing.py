# -*- coding: utf-8 -*-

# Algoritmo HillClimbing adaptado de : https://en.wikipedia.org/wiki/Hill_climbing

from heuristic import Heuristic
from neighbor import Neighbor
from utils import Generate
import copy

class HillClimbing(object):
    def __init__(self, iterate=100, startState=None):
        self.iterate = iterate
        self.startState = startState


    def hill(self):
        currentState = self.startState

        currentEval = Heuristic(currentState).count()

        i = 0
        while i < self.iterate:
            newState = Neighbor(Generate().desalloc(currentState)).generateState2()
            nextEval = Heuristic(newState).count()
            print "CurrentEval : %s | NextEval : %s" % (currentEval, nextEval)
            #print "CurrentState : %s" % currentState[1]
            print "newState : %s" % newState[1]
            if nextEval > currentEval :
                currentState = copy.deepcopy(newState)
                currentEval = nextEval

            i += 1

        print "CurrentState ", currentState
        return currentState