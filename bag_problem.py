from random import choice

class bag_problem:
    _weights = []
    _capacities = []
    _items=[]
    _bags=[]
    _ls=[]
    # construtor
    def __init__(self, nitens, nknaps, w, c):

        # Para o número de bolsas passado, alocar a lista knaps[0..nknaps]
        for i in range(nknaps):
            self._bags.append(0)
        # Inicia as listas de pesos e capacidades
        # _weights=[w0,w1..wN) - onde n é o número de itens e w é escolhido aleatoriamente da lista de w passada
        # _capacities=[c0,c1..cN] - onde n é o número de itens e c é escolhido aleatoriamente da lista de c passada
        for i in range(nitens):
            self._weights.append(choice(w))

        aux = c
        for i in range(nknaps):
            # aux é uma copia da lista de capacidades
            # Escolhe um valor de capacidade
            r = choice(aux)
            # inclui em _capacities
            self._capacities.append(r)
            # Remove r de aux para evitar repetição em _capacities
            aux.remove(r)

        # Aloca os itens nas bolsas
        self.allocate(nitens)
        # Calcula o peso atual das bolsas
        self.get_bags_w()
        # Calcula o leftSpace
        self.leftSpace()

    # Aloca os itens nas bolsas de forma que _items[i] indica o indice da bolsa alocada do item i
    def allocate(self, n_items):
        for i in range(n_items):
            self._items.append(choice(range(len(self._bags))))
        return self._items

    # Retorna a diferença capacidade - peso.atual
    def leftSpace(self):
        for i in range(len(self._bags)):
            delta = (self._capacities[i]) - (self._bags[i])
            self._ls.append(delta)


    # Preenche _bags com a soma dos pesos dos itens
    def get_bags_w(self):
        for i in range(len(self._bags)):
            for j in range(len(self._items)):
                if (self._items[j] == i):
                    self._bags[i] += self._weights[j]
        return self._bags


    # Verifica se os parametros gerados são validos
    # Condições de violação
    # - _knaps[i] > _capacities[i]
    def isValid(self):
        for i in self._ls:
            if i<0:
                return False
        return True


    # GETS E SETS
    def get_items(self):
        return self._items
    def get_weights(self):
        return self._weights
    def get_bags(self):
        return self._bags
    def get_capacities(self):
        return self._capacities