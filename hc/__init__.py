
from hc.heuristic import Heuristic
from hc.neighbor import Neighbor
from hc.utils import Utils
from hc.hill_climbing import HillClimbing
from hc.bag_problem import BagProblem


def main():
    # initialState = [[29, 23], [[1, 1], [19, 2], [17, 2], [13, 0], [19, 1]]]

    bagProblem = BagProblem(nBag=3, nItem=30).initState()
    #initialState = Neighbor(bagProblem).generateState()
    initialState = bagProblem

    Utils(initialState).printBags()

    print "----------------------------"
    hc = HillClimbing(500, initialState)
    final = hc.hill()

    print ("----------------------------")
    ut = Utils(final)
    ut.printBags()



if __name__ == '__main__':
    main()
