import random


class SelectionStrategy(object):
    """docstring for SelectionStrategy"""

    population = None

    def __init__(self):
        super(SelectionStrategy, self).__init__()

    def select(self, individual):
        raise NotImplemented("This is an abstract class for slection strategy")

    def update_population(self, population):
        self.population = population


class NormalProbabilitySelection(SelectionStrategy):
    # FIXME: define Normal parameters
    def select(self, individual):
        pass


class RandomSelection(SelectionStrategy):

    def select(self, individual):
        return random.randint(0, 1)


class MatingStrategy(object):
    """docstring for MatingStrategy"""

    population = None

    def __init__(self):
        super(MatingStrategy, self).__init__()

    def select(self, individual):
        raise NotImplemented("This is an abstract class for slection strategy")

    def update_population(self, population):
        self.population = population
