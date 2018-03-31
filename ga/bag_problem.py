from random import choice
from random import randint


class BagProblem:
    _nb = 0
    _ni = 0
    _weights = []  # fixo
    _capacities = []  # fixo

    # CONSTRUTOR DA CLASSE
    def __init__(self, nitens, nbags, w, c):

        # Preenche numero de itens e bolsas
        self._nb = nbags
        self._ni = nitens

        # Monta a lista de pesos
        for i in range(nitens):
            self._weights.append(choice(w))

        # Monta a lista de capacidades
        aux = c
        for i in range(nbags):
            # aux é uma copia da lista de capacidades disponíveis
            # Escolhe um valor de capacidade aleatório
            r = choice(aux)
            # inclui em _capacities
            self._capacities.append(r)
            # Remove r de aux para evitar repetição em _capacities
            aux.remove(r)

    # MÉTODOS AUXILIARES
    # Aloca randomicamente outra configuração de itens
    def allocate(self):
        items = []
        for i in range(self._ni):
            items.append(-1)

        for i in range(self._ni):
            items[i] = choice(range(self._nb))

        self.r_desallocate(items)
        return items

    # Desaloca randomicamente até 30% dos itens das bolsas
    def r_desallocate(self, items):
        a = randint(1, round(len(items) * 0.3))
        for i in range(a):
            items[randint(0, len(items) - 1)] = -1

    # Retorna o peso atual de uma configuração de itens
    def get_bags_w(self, items):
        bags = []
        for i in range(self._nb):
            bags.append(0)
        for i in range(self._nb):
            for j in range(self._ni):
                if (items[j] == i):
                    bags[i] += self._weights[j]
        return bags

    # Retorna o espaço vazio em cada uma das bolsas
    # valores negativos indicam que a bolsa ultrapassou sua capacidade
    def left_space(self, items):
        bags = self.get_bags_w(items)
        ls = []
        for i in range(self._nb):
            ls.append(bags[i])

        for i in range(self._nb):
            delta = (self._capacities[i]) - (bags[i])
            ls[i] = delta
        return ls

    # Verifica se a alocação feita é valida, com base no espaço livre na bolsa
    def is_valid(self, items):
        ls = self.left_space(items)
        for i in ls:
            if i < 0:
                return False
        return True

    # GETS E SETS
    def get_weights(self):
        return self._weights

    def get_capacities(self):
        return self._capacities

    def get_num_items(self):
        return len(self._ni)

    def get_num_bags(self):
        return len(self._nb)

    # [ NÃO USADO ]
    # Corrije a sobrecarga nas bolsas
    def correct(self, items):
        ls=self.left_space(items)
        for i in range(len(ls)):
            if ls[i] < 0:
                self.unload(items,i)

    # Descarrega as bolsas que excedem o limite da capacidade
    def unload(self, items, id_bag):
        ls = self.left_space(items)
        while ls[id_bag] < 0:
            aux = []
            for i in range(len(items)):
                if items[i] == id_bag:
                    aux.append(i)
            items[choice(aux)] = -1


    # # Calcula a média ponderada dos pesos nas bolsas
    # def get_medium(self):
    #     a=0
    #     b=0
    #     for i in range(len(self._items)):
    #         a += (self._items[i]+1) * self._weights[i]
    #     for j in self._items:
    #         b += (j+1)
    #     return a / b
