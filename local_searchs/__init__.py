# -*- coding: utf-8 -*-
from local_searchs.heuristic import Heuristic
from local_searchs.neighbor import Neighbor
from local_searchs.utils import Utils
from local_searchs.hill_climbing import HillClimbing
from local_searchs.simulated_annealing import SimulatedAnnealing
from local_searchs.bag_problem import BagProblem
import time

from local_searchs.heuristic import Heuristic
from local_searchs.neighbor import Neighbor
from local_searchs.utils import Utils
from local_searchs.hill_climbing import HillClimbing
from local_searchs.simulated_annealing import SimulatedAnnealing
from local_searchs.bag_problem import BagProblem
import time

def main():
    bagProblem = BagProblem(nBag=2, nItem=6).initState()
    initialState = bagProblem

    Utils(initialState).printBags()

    print("-------Hill Climbing-------")
    hc = HillClimbing(500, initialState)
    init = time.time()
    final = hc.hill_comum()
    end = time.time() - init

    ut = Utils(final)
    ut.printBags()
    print("Timestamp : {}".format(end))
    print("----------------------------")

    print(final)

    print("-------Simulated Annealing-------")
    sa = SimulatedAnnealing(initialState=initialState)
    init = time.time()
    final = sa.simulate()
    end = time.time() - init

    ut = Utils(final)
    ut.printBags()
    print("Timestamp : {}".format(end))
    print("----------------------------")



if __name__ == '__main__':
    main()
