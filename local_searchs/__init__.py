
from local_searchs.heuristic import Heuristic
from local_searchs.neighbor import Neighbor
from local_searchs.utils import Utils
from local_searchs.hill_climbing import HillClimbing
from local_searchs.simulated_annealing import SimulatedAnnealing
from local_searchs.bag_problem import BagProblem


def main():
    bagProblem = BagProblem(nBag=3, nItem=30).initState()
    initialState = bagProblem

    Utils(initialState).printBags()

    print("-------Hill Climbing-------")
    hc = HillClimbing(500, initialState)
    final = hc.hill_comum()

    ut = Utils(final)
    ut.printBags()
    print("----------------------------")

    print("-------Simulated Annealing-------")
    finalSa = []
    sa = SimulatedAnnealing(initialState=initialState)
    final, finalSa = sa.simulate()

    ut = Utils(final)
    ut.printBags()
    print("----------------------------")



if __name__ == '__main__':
    main()
