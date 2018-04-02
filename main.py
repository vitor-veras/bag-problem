# -*- coding: utf-8 -*-

from local_searchs.utils import Utils
from local_searchs.hill_climbing import HillClimbing
from local_searchs.simulated_annealing import SimulatedAnnealing
from local_searchs.bag_problem import BagProblem as bpLS
from ga.bag_problem import BagProblem as bpGA
from ga.genetic_algorithm import GeneticAlgorithm
import time
import random


def main():

    """LOCAL SEARCHS TESTS(HC - SA)"""
    bagProblem = bpLS(nBag=3, nItem=30).initState()
    initialState = bagProblem

    Utils(initialState).printBags()
    values = [random.randint(100, 1000) for i in range(10)]

    for v in values:
        hc = HillClimbing(v, initialState)
        init = time.time()
        final = hc.hill_comum()
        end = time.time() - init

        ut = Utils(final)
        print("\n-------Hill Climbing (%s)-------" % (v))
        ut.printBags()
        print("Timestamp : {}".format(end))
        print("----------------------------\n")


    print("-------Simulated Annealing-------")
    sa = SimulatedAnnealing(initialState=initialState)
    init = time.time()
    final = sa.simulate()
    end = time.time() - init

    ut = Utils(final)
    ut.printBags()
    print("Timestamp : {}".format(end))
    print("----------------------------")


    """GENETIC ALGORITHM TESTS"""

    # BAG PROBLEM PARAMS
    n_items = 30
    n_bags = 3
    w = [1, 3, 5, 7, 11, 13, 17, 19]
    c = [23, 29, 31, 37, 41, 43, 47]
    # GENETIC ALGORITHM PARAMS
    n_ind = 100
    n_generations = 500
    p_mut = 0.2
    p_sel = 0.1

    bp = bpGA(n_items, n_bags, w, c)
    ga = GeneticAlgorithm(bp, n_ind)
    print("GENETIC ALGORITHM: ")
    for i in range(10):
        ga.genetic_algorithm(ga.get_population(), n_generations, p_sel)
        ga.genetic_algorithm(ga.get_population(),n_generations,0.2,p_sel)


if __name__ == '__main__':
    main()
