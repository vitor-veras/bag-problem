from random import choice
from random import randint

class bag_problem:
    _weights = []
    _capacities = []
    _items=[]
    _bags=[]
    _ls=[]
    # construtor
    def __init__(self, nitens, nbags, w, c):

        # Para o número de bolsas passado, alocar a lista bags[0..nbags]
        for i in range(nbags):
            self._bags.append(0)
        # Inicia as listas de pesos e capacidades
        # _weights=[w0,w1..wN) - onde n é o número de itens e w é escolhido aleatoriamente da lista de w passada
        # _capacities=[c0,c1..cN] - onde n é o número de itens e c é escolhido aleatoriamente da lista de c passada
        for i in range(nitens):
            self._weights.append(choice(w))

        aux = c
        for i in range(nbags):
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
        self.left_space()

    # Aloca randomicamente os itens nas bolsas
    def allocate(self, n_items):
        self._items = []
        for i in range(n_items):
            self._items.append(choice(range(len(self._bags))))
        # nao deu pra pagar
        self.r_desallocate()

        return self._items
    # Desaloca randomicamente até 30% dos itens das bolsas
    def r_desallocate(self):
        a = randint(1, round(len(self._items) * 0.3))
        for i in range(a):
            self._items[randint(0, len(self._items) - 1)] = -1
        self.get_bags_w()
        self.left_space()

    # Retorna a diferença capacidade - peso.atual
    def left_space(self):
        self._ls = []
        for i in range(len(self._bags)):
            delta = (self._capacities[i]) - (self._bags[i])
            self._ls.append(delta)

    # Preenche _bags com a soma dos pesos dos itens
    def get_bags_w(self):
        for i in range(len(self._bags)):
            self._bags[i]=0
        for i in range(len(self._bags)):
            for j in range(len(self._items)):
                if (self._items[j] == i):
                    self._bags[i] += self._weights[j]
        return self._bags


    # Verifica se os parametros gerados são validos
    # Condições de violação
    # - _knaps[i] > _capacities[i]
    def is_valid(self):
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
    def get_ls(self):
        return self._ls


    #   [ NÃO USADO ]
    # # Corrije a sobrecarga nas bolsas
    # def correct(self):
    #     for i in range(len(self._ls)):
    #         if self._ls[i] < 0:
    #             self.unload(i)
    #
    # # Descarrega as bolsas que excedem o limite da capacidade
    # # Descarrega os itens que tem peso acima da média
    # def unload(self, bag):
    #     while self._ls[bag] < 0:
    #         aux = []
    #         for i in range(len(self._items)):
    #             if self._items[i] == bag:
    #                 aux.append(i)
    #         for j in aux:
    #             self._items[choice(aux)] = -1
    #             self.get_bags_w()
    #             self.left_space()
    #             # if self._weights[j] > self.get_medium():
    #             #     self._items[j]=-1
    #             #     self.get_bags_w()
    #             #     self.left_space()
    #
    # # Calcula a média ponderada dos pesos nas bolsas
    # def get_medium(self):
    #     a=0
    #     b=0
    #     for i in range(len(self._items)):
    #         a += (self._items[i]+1) * self._weights[i]
    #     for j in self._items:
    #         b += (j+1)
    #     return a / b