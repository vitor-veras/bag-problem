from local_searchs.utils import Utils
from local_searchs.hill_climbing import HillClimbing
from local_searchs.simulated_annealing import SimulatedAnnealing
from local_searchs.bag_problem import BagProblem
from ga.bag_problem import BagProblem
from ga.genetic_algorithm import GeneticAlgorithm
import time


def main():
    # BAG PROBLEM PARAMS
    n_items = 5
    n_bags = 3
    w = [1, 3, 5, 7, 11, 13, 17, 19]
    c = [23, 29, 31, 37, 41, 43, 47]
    # GENETIC ALGORITHM PARAMS
    n_ind = 5
    n_generations = 300

    # bagProblem = BagProblem(vBag = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83],nBag=15, nItem=80).initState()
    # initialState = bagProblem
    #
    # Utils(initialState).printBags()
    #
    # print("-------Hill Climbing-------")
    # hc = HillClimbing(500, initialState)
    # init = time.time()
    # final = hc.hill_comum()
    # end = time.time() - init
    #
    # ut = Utils(final)
    # ut.printBags()
    # print("Timestamp : {}".format(end))
    # print("----------------------------")
    #
    # print("-------Simulated Annealing-------")
    # finalSa = []
    # sa = SimulatedAnnealing(initialState=initialState)
    # init = time.time()
    # final = sa.simulate()
    # end = time.time() - init
    #
    # ut = Utils(final)
    # ut.printBags()
    # print("Timestamp : {}".format(end))
    # print("----------------------------")


    bp = BagProblem(n_items, n_bags, w, c)
    ga = GeneticAlgorithm(bp, n_ind)
    # ga.print_population()

    a = [0, 1, 1, -1, 2]
    b = [1, 2, 2, -1, 2]
    pop = [a,b]
    fit=lambda x: bp.get_bags_w(x)
    m=[]
    print(len(pop))
    print(bp.get_weights())
    m = (list(map(fit, pop)))

    # for i in range(len(pop)):
    #     m.append(list(map(fit,pop[i])))
    # m = list(map(fit,a))
    print(m)


if __name__ == '__main__':
    main()
