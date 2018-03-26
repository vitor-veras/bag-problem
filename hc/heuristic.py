#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Heuristic(object):

    #state = [[bagW0, bagW1, bagW2], [(itemW0, inBagX), ...]]
    def __init__(self, state):
        self.state = state
        self.bagState = state[0]
        self.itemState = state[1]

    def bagWeight2(self, indexBag, plusWeight):
        count = plusWeight
        for i in range(len(self.itemState)):
            if self.itemState[i][1] == indexBag:
                count += self.itemState[i][0]
        if self.bagState[indexBag] < count:
            return False

        return True

    #Calcula os pesos das bolsas (considerar bolsa -1 como fora da bolsa)
    def bagWeight(self):
        itemState = self.state[1]
        currentBW = [0]*(len(self.state[0])+1)

        for i in range(len(itemState)):
            currentBW[itemState[i][1]] += itemState[i][0]

        return currentBW

    #Avalia as bolsas para geração de vizinho, quanto mais próximo de 0 melhor
    def evaluateBag(self):
        bagState = self.state[0]

        eval = []

        #Pesos das bolsas
        currentBW = self.bagWeight()

        for i in range(len(bagState)):
            r = bagState[i] + currentBW[i]
            eval.append(abs(r))

        #return eval
        return sum(eval)


    def count(self):
        total = 0
        for i in range(len(self.bagState)):
            total += self.countInBag(i)

        return total

    def countInBag(self, bagIndex):
        eval = 0
        for i in range(len(self.itemState)):
            if self.itemState[i][1] == bagIndex:
                eval += 1
        return eval

    #Lista os pesos dos itens das bolsas
    def listItems(self):
        bagState = self.state[0]
        itemState = self.state[1]


        l1 = []
        l2 = []
        l3 = []
        l4 = []

        L = [l1, l2, l3, l4]

        for j in range(len(bagState) + 1):
            for i in range(len(itemState)):
                if(itemState[i][1] == j):
                    L[j].append(itemState[i][0])



        for i in range(len(bagState)):
            print "Bolsa[C = %s] %s => %s" % (bagState[i], i+1, L[i])

        print "Fora da bolsa => %s " % L[-1]

