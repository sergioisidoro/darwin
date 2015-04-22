from darwin.models import Individual
from darwin.models import World
from darwin.models import RandomSelection

class IndividualExample(Individual):

    def survival_test(self):
        pass

    def mutate(self):
        pass


adam = IndividualExample([1, 2, 3, 4, 5, 6])
strategy = RandomSelection()
brave_new_world = World(adam, selection_strategy=strategy)

brave_new_world.evolve()
