# Genetic Algorithm
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

    def print_population(self):
        for i in self._population:
            print(i)
            print()
#
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
