# Genetic Algorithm
from random import random
from bag_problem import BagProblem

# bag params
n_items = 5
n_bags = 3
w = [1, 3, 5, 7, 11, 13, 17, 19]
c = [23, 29, 31, 37, 41, 43, 47]
k = BagProblem(n_items, n_bags, w, c)

# GA params
n_ind_pop = 5


class GeneticAlgorithm:
    _population = []
    _bp = BagProblem(n_items, n_bags, w, c)

    def __init__(self):
        self.init_population(n_ind_pop)

    def init_population(self, n_ind):
        for i in range(n_ind):
            new_ind = self._bp.allocate(n_items)
            self._population.append(new_ind)

    def print_population(self):
        print(self._population)

# def genetic_algorithm(population, fitness, chromossome, f_thres=None, ngen=1000, p_mut=0.1):
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
# def init_population(pop_number, gene_pool, state_length):
#     """Initializes population for genetic algorithm
#     pop_number  :  Number of individuals in population
#     gene_pool   :  List of possible values for individuals
#     state_length:  The length of each individual"""
#     g = len(gene_pool)
#     population = []
#     for i in range(pop_number):
#         new_individual = [gene_pool[random.randrange(0, g)] for j in range(state_length)]
#         population.append(new_individual)
#
#     return population
#
#
# def select(r, population, fitness_fn):
#     fitnesses = map(fitness_fn, population)
#     sampler = weighted_sampler(population, fitnesses)
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
