# -*- coding: utf-8 -*-
from random import random


# indivíduo = 1 cromossomo
# cromossomo = lista de itens
# gene = { cromossomo[i] = valor da bolsa no qual está o item,
#         i = id do item, weights[i] retorna o peso do item com id i}

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
        c = (list(map(lambda x: self._p.correct(x), population)))
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

    #     TODO genetic_algorithm(), mutate()
    def genetic_algorithm(self, population, f_thres=None, ngen=500, p_mut=0.1, p_cross=0.9, p_sel=0.1):
        i = 0
        a_fitness = sorted(list(enumerate(self.fitness(population))), key=lambda tup: tup[1])
        while (i != ngen) and (a_fitness != f_thres) and max(a_fitness) != 1:
            a_fitness = sorted(list(enumerate(self.fitness(population))), key=lambda tup: tup[1])
            new_pop = population
            mut = []
            cross = []
            selected = self.select(population, p_sel)
            for i in range(len(selected)):
                del new_pop[selected[0][i]]
            for i in range(len(new_pop), 2):
                cross = self.op_crossover(new_pop[i], new_pop[i + 1])
                p = random.random()
                if p <= p_mut:
                    # TODO MUTATE FUNCTION
                    self.mutate(cross[0])
                    self.mutate(cross[1])
                new_pop[i] = cross[0]
                new_pop[i + 1] = cross[1]
            i += 1
        # a_fitness = self.fitness(population)
        # a_fitness = list(enumerate(a_fitness))
        # a_fitness = sorted(a_fitness, key=lambda tup: tup[1])
        # return "individual: ",population[a_fitness[0][0]]," FITNESS: ",a_fitness[0][1]
        return "papoca"

    def select(self, population, p_sel=0.1):
        sel = []
        aux = sorted(list(enumerate(self.fitness(population))), key=lambda tup: tup[1], reverse=False)
        for i in range(int(p_sel * len(population))):
            sel.append(aux.pop())
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

#     if not f_thres:
#         return None
#
#     fittest_individual = argmax(population, key=fitness_fn)
#     if fitness_fn(fittest_individual) >= f_thres:
#         return fittest_individual
#
#     return None
#
#
# def select(r, population, fitness_fn):
#     fitnesses = map(fitness_fn, population)
#     sampler = weighted_choice(fitnesses)
#     return [sampler() for i in range(r)]
#
#
# def recombine(x, y):
#     n = len(x)
#     c = random.randrange(0, n)
#     return x[:c] + y[c:]
#
#
# def recombine_uniform(x, y):
#     n = len(x)
#     result = [0] * n;
#     indexes = random.sample(range(n), n)
#     for i in range(n):
#         ix = indexes[i]
#         result[ix] = x[ix] if i < n / 2 else y[ix]
#     try:
#         return ''.join(result)
#     except:
#         return result
#
#
# def mutate(x, gene_pool, pmut):
#     if random.uniform(0, 1) >= pmut:
#         return x
#
#     n = len(x)
#     g = len(gene_pool)
#     c = random.randrange(0, n)
#     r = random.randrange(0, g)
#
#     new_gene = gene_pool[r]
#     return x[:c] + [new_gene] + x[c + 1:]
#
