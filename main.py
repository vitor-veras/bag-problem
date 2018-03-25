from bag_problem import bag_problem
from genetic_algorithm import genetic_algorithm
n_items = 10
n_bags = 3

w = [1, 3, 5, 7, 11, 13, 17, 19]
c = [23, 29, 31, 37, 41, 43, 47]
k=bag_problem(n_items, n_bags, w, c)

print("ITENS:",k.get_items(),"PESOS:", k.get_weights())
print("PESO ATUAL DAS BOLSAS:", k.get_bags())
print("CAPACIDADE DAS BOLSAS:", k.get_capacities())
print("ESPAÇO VAZIO:", k.get_ls())
print("É VÁLIDO ?", k.is_valid())

k.allocate(n_items)
print("ITENS:",k.get_items(),"PESOS:", k.get_weights())
print("PESO ATUAL DAS BOLSAS:", k.get_bags())
print("CAPACIDADE DAS BOLSAS:", k.get_capacities())
print("ESPAÇO VAZIO:", k.get_ls())
print("É VÁLIDO ?", k.is_valid())


# ga = genetic_algorithm(5)
# ga.print_population()