# Genetic Algorithm
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
    def init_population(self, n_ind):
        population = []
        for i in range(n_ind):
            new_ind = self._p.allocate()
            population.append(new_ind)
        return population

    def correct(self,population):
        c = (list(map(lambda x: self._p.correct(x), population)))
        return c

    def fitness(self, population):
        aux = (list(map(lambda x: sum(self._p.left_space(x))/sum((self._p.get_capacities())), population)))
        # fit = 1 - (((a1 - c1) + (a2 + c2) + (a3 - c3)) / (c1 + c2 + c3))
        fit = list(map(lambda x: 1- x, aux))
        return fit


    def print_population(self):
        print("WEIGHTS: ", self._p.get_weights(),"CAPACITIES: ",self._p.get_capacities())
        for i in self._population:
            print("ITEMS: ", i, " ATUAL W: ",self._p.get_bags_w(i), " LEFT SPACE: ", self._p.left_space(i))

    def get_population(self):
        return self._population
# def genetic_algorithm(population, fitness_fn, f_thres=None, ngen=500, p_mut=0.1, p_cross=0.8, p_sel=0.1):
#     i=0
#     while (i != ngen) and (fittest_individual != f_thres):
#
#     for i in range(ngen):
#         population = [mutate(recombine(*select(2, population, fitness_fn)), gene_pool, pmut)
#                       for i in range(len(population))]
#
#         fittest_individual = fitness_threshold(fitness_fn, f_thres, population)
#         if fittest_individual:
#             return fittest_individual
#
#     return argmax(population, key=fitness_fn)
#
# def fitness_threshold(fitness_fn, f_thres, population):
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
# def weighted_choice(items):
#   """
#   Chooses a random element from items, where items is a list of tuples in
#   the form (item, weight). weight determines the probability of choosing its
#   respective item. Note: this function is borrowed from ActiveState Recipes.
#   """
#   weight_total = sum((item[1] for item in items))
#   n = random.uniform(0, weight_total)
#   for item, weight in items:
#     if n < weight:
#       return item
#     n = n - weight
#   return item
