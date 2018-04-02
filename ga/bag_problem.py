# -*- coding: utf-8 -*-
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

    # Corrije a sobrecarga nas bolsas
    def correct(self, items):
        ls = self.left_space(items)
        for i in range(len(ls)):
            if ls[i] < 0:
                self.unload(items, i)
        return items

    # Descarrega a bolsa que excedem o limite da capacidade
    # Descarrega retirando os itens mais leves, pois queremos maximizar o peso dos itens
    def unload(self, items, id_bag):
        ls = self.left_space(items)
        while ls[id_bag] < 0:
            # aux: lista auxiliar que guarda o id dos itens(em [items]) que estão na bolsa sobrecarregada
            # f: lista do valor dos pesos dos itens que pertencem a lista aux
            aux = []
            f = []
            # inicia aux com os id em [items]
            for i in range(len(items)):
                if items[i] == id_bag:
                    aux.append(i)
            # inicia f com os pesos dos itens que estão na bolsa passada(id_bag)
            for i in aux:
                f.append(self._weights[i])

            # RETIRADA DOS ITENS:
            # (1) enumera-se a lista de pesos f[], de forma que teremos:
            #       f[] = [(id_em_aux , peso_do_item), (), ..., ()]
            # (2) Ordena-se f[] de acordo com os pesos, mas mantendo o id_em_aux
            # (3) retira-se o item atribuindo -1 na lista [items]
            #       f[0][0] retorna o id_em_aux do item, neste caso do item de menor peso pois está ordenado
            #       aux[f[0][0]] retorna o id_em_items do item de menor peso no momento
            #       recalcule ls, já que 1 item foi retirado
            f = list(enumerate(f))
            f = sorted(f, key=lambda tup: tup[1])
            items[aux[f[0][0]]] = -1
            ls = self.left_space(items)

    # Dado a lista de itens retorna a quantidade de itens deixados fora da alocação
    def left_items(self, items):
        li = []
        for i in range(len(items)):
            if items[i] == -1:
                li.append(i)
        return li

    # Printa a alocação nas bolsas
    def printBags(self, items):
        bags = self.BagsList(self.get_num_bags())
        outBag = []

        for i in range(len(items)):
            bag_index = items[i]
            if bag_index != -1:
                item = self.get_weights()[i]
                bags[bag_index].append(item)
                continue
            outBag.append(self.get_weights()[i])

        for i in range(len(bags)):
            print('Bag {} = {} | Max Vol. = {} , Allocated = {}'.format(i + 1, bags[i], self.get_capacities()[i],
                                                                        sum(bags[i])))
        print('Items out of bags: {}'.format(outBag))

    def BagsList(self, size):
        bags = list()
        for i in range(0, size):
            bags.append(list())
        return bags

    # GETS
    def get_weights(self):
        return self._weights

    def get_capacities(self):
        return self._capacities

    def get_num_items(self):
        return self._ni

    def get_num_bags(self):
        return self._nb
