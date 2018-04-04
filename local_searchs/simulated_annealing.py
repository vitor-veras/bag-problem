# -*- coding: utf-8 -*-
import random
import sys
from local_searchs.neighbor import Neighbor
from local_searchs.heuristic import Heuristic
from local_searchs.bag_problem import BagProblem
from math import exp


# Algoritmo Simulated Annealing adaptado de : http://conteudo.icmc.usp.br/pessoas/sandra/G9_t2/annealing.htm

class SimulatedAnnealing(object):
    # maxDisc -> Numero maximo de perturbacoes na temperatura
    # maxSuc -> Numero maximo de sucessos por iteracao
    # alpha -> fator de reducao da temperatura
    def __init__(self, iterate=500,
                 maxDis=200,
                 maxSuc=100,
                 alpha=0.73,
                 startTemp=500,
                 initialState=None,
                 finalTemp=0.000005):
        self.iterate = iterate
        self.maxDis = maxDis
        self.maxSuc = maxSuc
        self.alpha = alpha
        self.initialState = initialState
        self.startTemp = startTemp
        self.finalTemp = finalTemp

    def simulate(self):
        currentState = self.initialState
        T0 = self.startTemp
        while T0 > self.finalTemp:
            newState = Neighbor(BagProblem().desalloc(currentState)).generateState()
            deltaF = Heuristic(currentState).count() - Heuristic(newState).count()
            if deltaF <= 0:
                currentState = newState
            else:
                if exp(-deltaF / T0) > random.random():
                    currentState = newState

            T0 = T0 * self.alpha
        return currentState
