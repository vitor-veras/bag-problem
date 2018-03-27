
from hc.heuristic import Heuristic
from hc.neighbor import Neighbor
from hc.utils import Generate, Utils
from hc.hill_climbing import HillClimbing


def main():
    #initialState = [[29, 23], [[1, 1], [19, 2], [17, 2], [13, 0], [19, 1]]]

    initialState = Generate(nBag=3, nItem=30).initState()
    print("Bags: ", initialState[0], " | Weights: ", initialState[1])

    #h = Heuristic(initialState)
    #n = Neighbor(initialState).generateState2()
    #print h.count()
    #print "Bolsa", n[0], "Itens", n[1]

    #print Generate().desalloc(n)[1]
    #ws = h.evaluateBag()
    #print "heuristica %s " % ws
    #h.listItems()
    #print "----------------------------"
    hc = HillClimbing(500, initialState)
    final = hc.hill()

    #h = Heuristic(final)
    #ws = h.evaluateBag()
    #print "heuristica %s " % ws
    #h.listItems()

    print ("----------------------------")
    ut = Utils(final)
    #print initialState[1]
    #print ("Final Bags: ", final[0], " | Weights: ", final[1])
    ut.printBags()



if __name__ == '__main__':
    main()
