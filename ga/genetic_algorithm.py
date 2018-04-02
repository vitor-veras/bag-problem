# -*- coding: utf-8 -*-
from random import random

# indivíduo = 1 cromossomo
# cromossomo = lista de itens
# gene = { cromossomo[i] = valor da bolsa no qual está o item,
#         i = id do item, weights[i] retorna o peso do item com id i}
import random


class GeneticAlgorithm:
    _population = []

    def __init__(self, problem, n_ind):
        self._p = problem
        self._population = self.init_population(n_ind)

    # Gera a população inicial
    def init_population(self, n_ind):
        population = []
        for i in range(n_ind):
            new_ind = self._p.allocate()
            population.append(new_ind)
        return population

    # Corrige a população caso exista indivíduos inviáveis
    def correct(self, population):
        c = []
        for i in range(len(population)):
            c.append(self._p.correct(population[i]))
        # c = (map(lambda x: self._p.correct(x), population))
        return c

    # Retorna uma lista contendo o fitness de cada indivíduo
    def fitness(self, population):
        # fit = 1 - (ls1/c1+c2+c3 + ls2/c1+c2+c3 + ls3/c1+c2+c3)
        # fit = 1 - [((T_ls)/(T_c))*((T_li)/(T_i))]
        aux = (list(map(lambda x: sum(self._p.left_space(x)) / sum((self._p.get_capacities())), population)))
        aux2 = (list(map(lambda x: len(self._p.left_items(x)) / self._p.get_num_items(), population)))
        fit = list(map(lambda x, y: 1 - (x * y), aux, aux2))
        return fit

    # Imprime os pesos e capacidades (FIXO)
    # imprime os indivíduos, seu peso atual e seu espaço livre
    def print_population(self):
        print("WEIGHTS: ", self._p.get_weights(), "CAPACITIES: ", self._p.get_capacities())
        for i in self._population:
            print()
            print("ITEMS: ", i)
            print(" ATUAL W: ", self._p.get_bags_w(i), " LEFT SPACE: ", self._p.left_space(i), " LEFT ITEMS: ",
                  self._p.left_items(i))

    # Retorna a população
    def get_population(self):
        return self._population


    def genetic_algorithm(self, population, f_thres=None, ngen=500, p_mut=0.1, p_sel=0.1):
        n = 0
        a_fitness = self.fitness(population)
        while (n != ngen) and (max(a_fitness) != 1.0):

            new_pop = []
            selected = self.select(population, p_sel)
            for i in range(len(selected)):
                new_pop.append(population[selected[i]])
            new_pop = self.Diff(population, new_pop)

            for i in range(0, len(new_pop), 2):
                cross = self.op_crossover(new_pop[i], new_pop[i + 1])
                p = random.random()
                if p <= p_mut:
                    self.mutate(cross[0])
                    self.mutate(cross[1])
                new_pop[i] = cross[0]
                new_pop[i + 1] = cross[1]
            for i in range(len(selected)):
                new_pop.append(population[selected[i]])
            new_pop = self.correct(new_pop)
            population = new_pop
            a_fitness = self.fitness(population)
            n += 1
        a_fitness = sorted(list(enumerate(self.fitness(population))), key=lambda tup: tup[1], reverse=True)

        print("iteração: ",n)
        print(population)
        print("A_fit: ", a_fitness)
        print("melhor indv: ", population[a_fitness[0][0]])
        print("Fitness: ",a_fitness[0][1])


    def select(self, population, p_sel=0.1):
        sel = []
        aux = sorted(list(enumerate(self.fitness(population))), key=lambda tup: tup[1], reverse=False)
        for i in range(int(p_sel * len(population))):
            sel.append((aux.pop())[0])
        return sel

    def op_crossover(self, x, y):
        n = len(x)
        c = round(n / 2)
        son1 = x[:c] + y[c:]
        son2 = x[c:] + y[:c]
        return list((son1, son2))

    def tp_crossover(self, x, y):
        n = len(x)
        c = round(n / 2) - 1
        print(c)
        son1 = x[:c] + y[c:len(y) - c] + x[len(x) - c:]
        son2 = y[:c] + x[c:len(x) - c] + y[len(y) - c:]

        return list((son1, son2))

    def mutate(self, x):
        aux = self._p.left_items(x)
        max_w = [0, 0]  # max_w[0] -> indica o maior peso / max_w[1] -> indice do maior peso
        for i in aux:
            if self._p.get_weights()[i] > max_w[0]:
                max_w[0] = self._p.get_weights()[i]
                max_w[1] = i
        x[max_w[1]] = random.randint(0, self._p.get_num_bags() - 1)

    # Python code t get difference of two lists
    def Diff(self, li1, li2):
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
        return li_dif
