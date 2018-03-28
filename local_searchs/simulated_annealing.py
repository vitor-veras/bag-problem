import random
import sys
from local_searchs.neighbor import Neighbor
from local_searchs.heuristic import Heuristic
from local_searchs.bag_problem import BagProblem
from math import exp

# Algoritmo Simulated Annealing adaptado de : https://pt.wikipedia.org/wiki/Simulated_annealing

class SimulatedAnnealing(object):

    # maxDisc -> Numero maximo de perturbacoes na temperatura
    # maxSuc -> Numero maximo de sucessos por iteracao
    # alpha -> fator de reducao da temperatura
    def __init__(self, iterate=500,
                 maxDis=100,
                 maxSuc=70,
                 alpha=0.9,
                 startTemp=300,
                 initialState= None):
        self.iterate = iterate
        self.maxDis = maxDis
        self.maxSuc = maxSuc
        self.alpha = alpha
        self.initialState = initialState
        self.startTemp = startTemp

    def simulate(self):
        i = 0
        success = sys.maxsize
        currentState = self.initialState
        t = self.startTemp
        currentWeight = Heuristic(currentState).getCurrentTotalWeight()
        totalWeight = Heuristic(currentState).getTotalWeight()

        solutions = []

        while not(success == 0) and i < self.iterate and currentWeight != totalWeight:
            j = 0
            success = 0
            while success <= self.maxSuc and j < self.maxDis:
                f1 = Heuristic(currentState).count()
                newState = Neighbor(BagProblem().desalloc(currentState)).generateState()

                f2 = Heuristic(newState).count()
                deltaF = f1 - f2
                if not t == 0.0:
                    if (deltaF <= 0) or (exp(-deltaF/t) > random.random()):
                        currentState = newState
                        success += 1

                j += 1
            t = self.alpha * t
            i += 1

        return currentState, solutions
